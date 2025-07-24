import os
import re
import sys

from qfluentwidgets import FluentIcon, RoundMenu, Action, InfoBarPosition, InfoBar

from adb_commond import ADBCMD
from PySide6.QtWidgets import QApplication, QWidget,QTableWidgetItem, QFileDialog, QHeaderView,QAbstractItemView, QMenu,QMessageBox,QInputDialog
from PySide6.QtCore import Qt,QThread,Slot,Signal
from PySide6.QtGui import QAction, QShortcut, QKeySequence, QIcon, QColor, QBrush, QGuiApplication, QStandardItemModel, \
    QStandardItem
from PySide6 import QtCore, QtGui, QtWidgets


from ui.logRecord import Ui_logRecord
from adb_commond import ADBCMD

class logRecord(QWidget,Ui_logRecord):

    ADBCMD=ADBCMD()
    ADBCMD.current_interface="logrecord"
    sucSignal = Signal(str)
    warnSignal = Signal(str)
    errSignal = Signal(str)

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.LogRecordModel = QStandardItemModel()
        self.LogRecordTableView.setModel(self.LogRecordModel)
        self.LogRecordModel.setColumnCount(6)
        self.LogRecordModel.setHorizontalHeaderLabels(["时间", "PID", "TID", "优先级", "标签", "消息"])
        self.LogRecordTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.LogRecordTableView.horizontalHeader().setSectionResizeMode(0,QHeaderView.Custom)
        self.LogRecordTableView.horizontalHeader().resizeSection(0,150)
        self.LogRecordTableView.horizontalHeader().setSectionResizeMode(1,QHeaderView.Custom)
        self.LogRecordTableView.horizontalHeader().resizeSection(1,75)
        self.LogRecordTableView.horizontalHeader().setSectionResizeMode(2,QHeaderView.Custom)
        self.LogRecordTableView.horizontalHeader().resizeSection(2,75)
        self.LogRecordTableView.horizontalHeader().setSectionResizeMode(3,QHeaderView.Custom)
        self.LogRecordTableView.horizontalHeader().resizeSection(3,75)
        self.LogRecordTableView.horizontalHeader().setSectionResizeMode(4,QHeaderView.Custom)
        self.LogRecordTableView.horizontalHeader().resizeSection(4,180)
        self.LogRecordTableView.horizontalHeader().setSectionResizeMode(5,QHeaderView.Stretch)
        self.LogRecordTableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.LogRecordTableView.customContextMenuRequested.connect(self.contextMenuEvent)
        self.LogRecordTableView.verticalHeader().setVisible(False)
        self.sucSignal.connect(self.parent().createSuccessInfoBar)
        self.warnSignal.connect(self.parent().createWarningInfoBar)
        self.errSignal.connect(self.parent().createErrorInfoBar)
        self.search_input.searchSignal.connect(self.search)
        self.start_button.clicked.connect(lambda :self.start_logcatThread())
        self.stop_button.clicked.connect(lambda :self.stop_logcatThread())
        self.save_button.clicked.connect(lambda :self.start_savelogcatThread())
        self.copyShorCut = QShortcut(QKeySequence('Ctrl+C'), self)
        self.copyShorCut.activated.connect(self.copy_shortCut)
        QGuiApplication.processEvents()

    def contextMenuEvent(self, event):

        self.menu = RoundMenu(self)

        copyAction = Action(FluentIcon.COPY,'复制')
        copyAction.triggered.connect(self.copySlot)
        self.menu.addAction(copyAction)
        self.menu.popup(QtGui.QCursor.pos())

    def is_device_loaded(self):
        '''设备是否加载'''
        if self.ADBCMD.current_device:
            return True
        else:
            self.warnSignal.emit("设备未选择")
            return False

    def search(self,keyword):
        '''搜索'''
        if self.is_device_loaded():
            items = self.LogRecordModel.findItems(keyword, Qt.MatchFlag.MatchExactly)
            if len(items)>0:
                for item in items:
                    row = item.row()
                    item.setBackground(QBrush(QColor(0, 255, 0)))
                self.sucSignal.emit("已高亮标注")
            else:
                self.errSignal.emit(f"不存在该关键字{keyword}")

    def copySlot(self):
        '''复制槽'''
        selection_model = self.LogRecordTableView.selectionModel()
        selected_indexes = selection_model.selectedRows()
        selected_rows = set(index.row() for index in selected_indexes)
        if selected_indexes:
            if len(selected_rows) == 1:
                print(selected_indexes[0])
                row_strings = []
                for column in range(self.LogRecordModel.columnCount()):
                    item = self.LogRecordModel.item(selected_indexes[0].row(), column)
                    row_strings.append(item.text())
                # 将行字符串连接为一个字符串
                row_text = ' '.join(row_strings)
                # 将行字符串复制到剪贴板
                clipboard = QApplication.clipboard()
                clipboard.setText(row_text)
                self.sucSignal.emit("复制成功")
            else:
                self.warnSignal.emit("请勿选择多行")
        else:
            self.warnSignal.emit("未选中")


    def start_logcatThread(self):
        '''启动日志查看线程'''
        if self.is_device_loaded():
            self.ADBCMD.logcat_clear()
            self.LogRecordModel.setRowCount(0)
            self.logcatthread = self.logcatThread(self)
            print("logcat开始")
            self.logcatthread.start()
            self.start_button.setEnabled(False)

    def stop_logcatThread(self):
        '''停止日志查看线程'''
        if hasattr(self, 'logcatthread'):
            self.logcatthread.stop()
            print("logcat停止")
        if not self.start_button.isEnabled():
            self.start_button.setEnabled(True)

    def start_savelogcatThread(self):
        '''启动保存日志线程'''
        if self.LogRecordModel.rowCount():
            ex_path = QFileDialog.getExistingDirectory(self, "Open Dir", r"C:")
            if ex_path:
                self.savelogcatthread = self.savelogcatThread(self)
                self.savelogcatthread.setExpath(ex_path)
                self.savelogcatthread.start()
                self.sucSignal.emit(f"保存至:{ex_path}")
            else:
                self.warnSignal.emit("未选择保存路径")
                pass
        else:
            self.errSignal.emit("当前页面不存在数据")

    class logcatThread(QThread):
        # logcatSignal=Signal(str)

        def run(self):
            self.process = self.parent().ADBCMD.log_cat()
            for loginfo in self.process.stdout:
                if not loginfo.startswith('-'):
                    row_data=list()
                    row_num = self.parent().LogRecordModel.rowCount()
                    message_list = loginfo.split(": ")
                    num_and_letter_list = re.findall("\S+", message_list[0])
                    # print(message_list)
                    # print(message_list[0])
                    # print(len(num_and_letter_list))
                    # print(num_and_letter_list)
                    if len(num_and_letter_list) == 7:
                        row_data = [f"{num_and_letter_list[0]} {num_and_letter_list[1]}", num_and_letter_list[2],
                                    num_and_letter_list[3], num_and_letter_list[4], num_and_letter_list[5]+" "+num_and_letter_list[6],
                                    message_list[1].rstrip("\n")]
                    elif len(num_and_letter_list)==6:
                        row_data = [f"{num_and_letter_list[0]} {num_and_letter_list[1]}", num_and_letter_list[2],num_and_letter_list[3],num_and_letter_list[4], num_and_letter_list[5], message_list[1].rstrip("\n")]
                    elif len(num_and_letter_list)==5:
                        row_data = [f"{num_and_letter_list[0]} {num_and_letter_list[1]}", num_and_letter_list[2],
                                    num_and_letter_list[3], num_and_letter_list[4], " ",
                                    message_list[1].rstrip("\n")]
                    self.parent().LogRecordModel.setRowCount(row_num + 1)
                    for col_index, cell_data in enumerate(row_data):
                        item = QStandardItem(cell_data)
                        if col_index!=5:
                            item.setTextAlignment(Qt.AlignCenter)
                        self.parent().LogRecordModel.setItem(row_num - 1, col_index, item)

        def stop(self):
            self.process.terminate()

    class savelogcatThread(QThread):
        ex_path = None

        def setExpath(self, ex_path):
            self.ex_path = ex_path

        def run(self):
            with open(os.path.join(self.ex_path,"result.txt"),"w") as output:
                row_count = self.parent().LogRecordModel.rowCount()
                column_count = self.parent().LogRecordModel.columnCount()
                for row in range(row_count):
                    row_data = []
                    for column in range(column_count):
                        item = self.parent().LogRecordModel.item(row, column)
                        if item is not None:
                            cell_data = item.text()
                            row_data.append(cell_data)
                        else:
                            row_data.append("")
                    output.write(" ".join(row_data)+"\n")
            self.quit()
            self.wait()

    def handle_current_device_changed(self,value):
        if self.ADBCMD.current_device != value:
            # print(f"handle_current_device_changed {value}")
            self.ADBCMD.set_current_device(value)

    #快捷键
    def copy_shortCut(self):
        self.copySlot()