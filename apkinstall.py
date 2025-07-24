import os
import shutil
import re
import sys

from functools import partial
from qfluentwidgets import FluentIcon, ToolButton, InfoBarPosition, InfoBar, RoundMenu,Action

from adb_commond import ADBCMD
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QAbstractItemView, QMenu, QMessageBox, QInputDialog, QHeaderView, QTableWidgetItem, QHBoxLayout, QVBoxLayout, QSizePolicy
from PySide6.QtCore import Qt, QThread, Slot, Signal, QCoreApplication
from PySide6.QtGui import QAction, QShortcut, QKeySequence, QIcon, QDragEnterEvent, QDropEvent
from PySide6 import QtCore, QtGui, QtWidgets

from ui.apkInstall import Ui_apkInstall
from adb_commond import ADBCMD

class apkInstall(QWidget,Ui_apkInstall):

    ADBCMD=ADBCMD()
    ADBCMD.current_interface="screenCapture"
    extension_list=[".apk",".zip",".rar",".7z"]
    sucSignal = Signal(str)
    warnSignal = Signal(str)
    errSignal = Signal(str)

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        '''UI设置'''
        self.setupUi(self)
        self.ApkTableWidget.setColumnCount(2)
        self.ApkTableWidget.setHorizontalHeaderLabels(["安装包名", "操作"])
        self.ApkTableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ApkTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ApkTableWidget.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeMode.Stretch)
        self.ApkTableWidget.horizontalHeader().setSectionResizeMode(1,QHeaderView.ResizeMode.Custom)
        self.ApkTableWidget.horizontalHeader().resizeSection(1,200)
        self.ApkTableWidget.verticalHeader().setVisible(False)

        self.ApkTableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ApkTableWidget.customContextMenuRequested.connect(self.contextMenuEvent)
        self.setAcceptDrops(True)
        self.sucSignal.connect(self.parent().createSuccessInfoBar)
        self.warnSignal.connect(self.parent().createWarningInfoBar)
        self.errSignal.connect(self.parent().createErrorInfoBar)
        self.clear_button.clicked.connect(self.clear_TableWidget)
        self.delShorCut = QShortcut(QKeySequence.StandardKey.Delete, self)
        self.delShorCut.activated.connect(self.del_shortCut)

    def contextMenuEvent(self, event):
        '''右键菜单'''
        self.menu = RoundMenu(self)
        delAction = Action(FluentIcon.DELETE,'删除')
        delAction.triggered.connect(self.delSlot)
        self.menu.addAction(delAction)
        self.menu.popup(QtGui.QCursor.pos())

    def delSlot(self):
        '''删除槽'''
        selected_row = self.ApkTableWidget.currentRow()
        self.ApkTableWidget.removeRow(selected_row)
        self.sucSignal.emit("删除成功")

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        url_list=list()
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                if re.findall("\.[A-Za-z0-9]+$",file_path)[-1] in self.extension_list:
                    url_list.append(file_path)
            print(url_list)
            self.set_ApkTableWidget_by_data(url_list)

    def clear_TableWidget(self):
        '''清除Table组件'''
        self.ApkTableWidget.setRowCount(0)

    def set_ApkTableWidget_by_data(self,data):
        '''根据得到的data设置Table组件'''
        row_num=self.ApkTableWidget.rowCount()
        print(row_num)
        self.ApkTableWidget.setRowCount(row_num+len(data))
        for row_index, row_data in enumerate(data):
            #安装包路径
            item = QTableWidgetItem(row_data)
            self.ApkTableWidget.setItem(row_num+row_index, 0, item)
            #按钮
            hLayout = QHBoxLayout()
            vLayout = QVBoxLayout()
            install_button = ToolButton(self.ApkTableWidget)
            install_button.setObjectName(f"install_button_{row_num+row_index}")
            install_button.setIcon(FluentIcon.DOWNLOAD)
            install_button.clicked.connect(partial(self.install,row_num+row_index))
            install_button.setToolTip("安装")
            uninstall_button = ToolButton(self.ApkTableWidget)
            uninstall_button.setObjectName(u"uninstall_button")
            uninstall_button.setIcon(FluentIcon.CANCEL)
            uninstall_button.setToolTip("卸载(暂未实现)")
            # uninstall_button.clicked.connect(self.uninstall)
            hLayout.addWidget(install_button)
            hLayout.addWidget(uninstall_button)
            vLayout.addLayout(hLayout)
            widget = QWidget()
            widget.setLayout(vLayout)
            self.ApkTableWidget.setCellWidget(row_num+row_index, 1, widget)
            #设置列高
            self.ApkTableWidget.verticalHeader().setSectionResizeMode(row_num+row_index, QHeaderView.ResizeMode.Custom)
            self.ApkTableWidget.verticalHeader().resizeSection(row_num+row_index, 70)
            self.ApkTableWidget.repaint()
            QApplication.processEvents()
        for row in range(self.ApkTableWidget.rowCount()):
            item = self.ApkTableWidget.item(row, 0)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    def install(self,row):
        '''安装apk'''
        self.start_installThread(row)

    def start_installThread(self,row):
        '''安装线程'''
        self.installthread = self.installThread(self)
        self.installthread.setRow(row)
        self.installthread.start()

    class installThread(QThread):
        '''安装线程类'''
        row=None

        def setRow(self,Row):
            self.row=Row

        def run(self):
            item = self.parent().ApkTableWidget.item(self.row, 0)
            message = self.parent().ADBCMD.install_apk(item.text())
            if message:
                self.parent().sucSignal.emit("安装成功")
            else:
                self.parent().errSignal.emit("安装失败")
            self.quit()
            self.wait()

    # def uninstall(self):
    #     button = self.sender()  # 获取发送信号的按钮
    #     cell_widget = self.ApkTableWidget.indexAt(button.pos())  # 获取按钮所在的单元格
    #     row = cell_widget.row()  # 获取单元格的行号
    #     col = cell_widget.column()  # 获取单元格的列号
    #     item = self.ApkTableWidget.item(row, 0)
    #     self.ADBCMD.uninstall_apk(item.text())

    def handle_current_device_changed(self,value):
        '''同步当前设备改变'''
        if self.ADBCMD.current_device != value:
            # print(f"handle_current_device_changed {value}")
            self.ADBCMD.set_current_device(value)

    #快捷键
    def del_shortCut(self):
        self.delSlot()

