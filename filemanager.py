import os
import re
import sys
import time

from adb_commond import ADBCMD
from PySide6.QtWidgets import QApplication,QLabel, QWidget,QTableWidgetItem, QHeaderView,QFileDialog, QAbstractItemView, QMenu,QMessageBox,QInputDialog
from PySide6.QtCore import Qt,QThread,QObject,QRect,Slot,Signal,QUrl
from PySide6.QtGui import QAction, QShortcut, QKeySequence, QIcon, QPixmap, QDragEnterEvent, QDragEnterEvent, \
    QDragMoveEvent, QDropEvent, QGuiApplication
from PySide6 import QtCore, QtGui, QtWidgets
from qfluentwidgets import FluentIcon, BodyLabel, RoundMenu, MessageBox, SubtitleLabel, LineEdit, MessageBoxBase, FolderListDialog, Action, InfoBarPosition, InfoBar,ToolTip

from ui.fileManager import Ui_fileManager


def source_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class fileManager(QWidget,Ui_fileManager):

    ADBCMD = ADBCMD()
    ADBCMD.current_interface="filemanager"
    last_path=""
    current_path=""
    cut=False
    copy2paste_filelist=list()
    copy2paste_dirlist = list()
    progress_max=int()
    progress_per=0
    refreshSignal = Signal()
    sucSignal = Signal(str)
    errSignal = Signal(str)
    warnSignal = Signal(str)


    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.FileTableWidget.setColumnCount(5)
        self.FileTableWidget.setHorizontalHeaderLabels(["类型", "文件名", "权限", "大小", "最近修改时间"])
        self.FileTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.FileTableWidget.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeMode.Custom)
        self.FileTableWidget.horizontalHeader().resizeSection(0,70)
        self.FileTableWidget.horizontalHeader().setSectionResizeMode(2,QHeaderView.ResizeMode.Custom)
        self.FileTableWidget.horizontalHeader().resizeSection(2,120)
        self.FileTableWidget.horizontalHeader().setSectionResizeMode(3,QHeaderView.ResizeMode.Custom)
        self.FileTableWidget.horizontalHeader().resizeSection(3,110)
        self.FileTableWidget.horizontalHeader().setSectionResizeMode(4,QHeaderView.ResizeMode.Custom)
        self.FileTableWidget.horizontalHeader().resizeSection(4,150)
        self.FileTableWidget.horizontalHeader().setSectionResizeMode(1,QHeaderView.ResizeMode.Stretch)
        self.FileTableWidget.verticalHeader().setVisible(False)
        self.FileTableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.FileTableWidget.customContextMenuRequested.connect(self.contextMenuEvent)
        self.FileTableWidget.itemDoubleClicked.connect(self.double_clicked)
        self.setAcceptDrops(True)
        self.innerPath_input.returnPressed.connect(lambda :self.innerPath_returnPressed(self.innerPath_input.text()))
        self.innerPath_input.currentIndexChanged.connect(self.on_combobox_changed)
        # 返回至跳转前目录
        self.back_button.clicked.connect(self.back_upper_dir)
        self.back_button.setToolTip("返回至跳转前目录")
        # 返回至上级目录
        self.upper_button.clicked.connect(self.upper_dir)
        self.upper_button.setToolTip("返回至上级目录")

        self.refresh_button.clicked.connect(self.refreshWidget)
        self.openFile_button.clicked.connect(self.set_expath)
        self.push_button.clicked.connect(self.start_pushThread)
        self.search_input.searchSignal.connect(self.search)
        self.refreshSignal.connect(self.refreshWidget)
        self.sucSignal.connect(self.parent().createSuccessInfoBar)
        self.warnSignal.connect(self.parent().createWarningInfoBar)
        self.errSignal.connect(self.parent().createErrorInfoBar)
        self.copyShorCut = QShortcut(QKeySequence('Ctrl+C'), self)
        self.copyShorCut.activated.connect(self.copy_shortCut)
        self.cutShorCut = QShortcut(QKeySequence('Ctrl+X'), self)
        self.cutShorCut.activated.connect(self.cut_shortCut)
        self.pasteShorCut = QShortcut(QKeySequence('Ctrl+V'), self)
        self.pasteShorCut.activated.connect(self.paste_shortCut)
        self.delShorCut = QShortcut(QKeySequence.StandardKey.Delete, self)
        self.delShorCut.activated.connect(self.del_shortCut)
        self.renameShorCut = QShortcut(QKeySequence('F2'), self)
        self.renameShorCut.activated.connect(self.rename_shortCut)
        self.mkdirShorCut = QShortcut(QKeySequence('Ctrl+Shift+N'), self)
        self.mkdirShorCut.activated.connect(self.mkdir_shortCut)
        self.pullShorCut = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.pullShorCut.activated.connect(self.pull_shortCut)

    # def setup_thread(self):
    #     self.thread1 = QThread(self)  # 创建一个线程
    #     self.thread = self.refresh_fileWidget_Thread()  # 实例化线程类
    #     self.thread.moveToThread(self.thread1)  # 将类移动到线程中运行
    #     # 线程数据传回信号，用add_item函数处理
    #     self.thread.data_signal.connect(self.set_FileTableWidget_by_data)
    #     self.innerPath_input.returnPressed.connect(self.start_Thread)
    #     self.innerPath_input.returnPressed.connect(self.refresh_fileWidget_Thread.run)  # 连接到线程类的函数

    def is_device_loaded(self):
        '''设备是否加载'''
        if self.ADBCMD.current_device:
            return True
        else:
            self.warnSignal.emit("设备未选择")
            return False


    def is_innerPath_existed(self):
        '''内部路径是否存在'''
        if self.innerPath_input:
            result = self.ADBCMD.is_existed(self.innerPath_input.text())
            if result=="存在":
                return True
            # elif result=="不存在":
            else:
                self.errSignal.emit("该机内路径不存在")
                return False
        else:
            return True

    def is_currentPath_existed(self):
        '''当前路径是否存在'''
        if self.current_path:
            result = self.ADBCMD.is_existed(self.current_path)
            if result=="存在":
                return True
            else:
            # elif result=="不存在":
                self.errSignal.emit("该机内路径不存在")
                return False
        else:
            return True

    def set_expath(self):
        '''设置外部路径'''
        expath,_=QFileDialog.getOpenFileName(self, "Open File", r"C:")
        print(expath)
        if expath:
            self.exPath_input.setText(expath)

    def contextMenuEvent(self, event):
        '''右键菜单'''
        self.menu = RoundMenu(self)

        copyAction = Action(FluentIcon.COPY,'复制')
        cutAction = Action(FluentIcon.CUT,'剪切')
        pasteAction = Action(FluentIcon.PASTE,'粘贴')
        delAction = Action(FluentIcon.DELETE,'删除')
        renameAction = Action(FluentIcon.EDIT,'重命名')
        mkdirAction = Action(FluentIcon.FOLDER_ADD,'新建文件夹')
        pullAction = QAction("Pull",self)

        copyAction.triggered.connect(self.copySlot)
        cutAction.triggered.connect(lambda:self.copySlot(cut=True))
        pasteAction.triggered.connect(self.pasteSlot)
        delAction.triggered.connect(self.delSlot)
        renameAction.triggered.connect(self.show_renameDialog)
        mkdirAction.triggered.connect(self.show_mkdirDialog)
        pullAction.triggered.connect(self.start_pullThread)

        self.menu.addAction(copyAction)
        self.menu.addAction(cutAction)
        self.menu.addAction(pasteAction)
        self.menu.addAction(delAction)
        self.menu.addAction(renameAction)
        self.menu.addAction(mkdirAction)
        self.menu.addAction(pullAction)
        self.menu.popup(QtGui.QCursor.pos())

    def update_progressBarValue(self):
        '''更新进度条'''
        self.progress_per += round(1 / self.progress_max,3) * 100
        # print(self.progress_per)
        self.ProgressBar.setVal(round(self.progress_per))

    def filter_filename(self,selected_items):
        '''过滤出文件名'''
        second_column_items=list()
        for item in selected_items:
            if item.column() == 1:
                second_column_items.append(item)
        return second_column_items

    def copySlot(self,cut=False):
        '''复制槽'''
        selected_items=self.FileTableWidget.selectedItems()
        self.copy2paste_filelist.clear()
        self.copy2paste_dirlist.clear()
        second_column_items=list()#文件名
        third_column_items = list()#L,D,F
        for item in selected_items:
            if item.column() == 1:  # 列索引为 1 表示第二列
                second_column_items.append(item)
            elif item.column()== 2:
                third_column_items.append(item)
        for index, item in enumerate(third_column_items):
            if item.text().startswith("-"):
                self.copy2paste_filelist.append(f"{self.current_path}/{second_column_items[index].text()}")
            else:
                self.copy2paste_dirlist.append(f"{self.current_path}/{second_column_items[index].text()}")
        print(f"copySlot copy2paste_dirlist:{self.copy2paste_dirlist}")
        print(f"copySlot copy2paste_filelist{self.copy2paste_filelist}")
        if cut:
            self.cut=True
            if len(selected_items)!=0:
                self.sucSignal.emit("剪切成功")
            else:
                self.warnSignal.emit("请选择文件")
        else:
            self.cut=False
            if len(selected_items) != 0:
                self.sucSignal.emit("复制成功")
            else:
                self.warnSignal.emit("请选择文件")

    def pasteSlot(self):
        '''粘贴槽'''
        self.pastethread = self.pasteThread(self)
        self.pastethread.start()
        self.pastethread.wait()
        if self.cut:
            self.start_delThread_after_paste(self.copy2paste_dirlist + self.copy2paste_filelist)


    def delSlot(self):
        '''删除槽'''
        selected_items = self.FileTableWidget.selectedItems()
        self.is_del = MessageBox("警告","是否删除",self)
        self.is_del.yesSignal.connect(lambda: self.start_delThread(selected_items))
        self.is_del.show()

    def show_renameDialog(self):
        '''重命名对话框'''
        selected_items = self.FileTableWidget.selectedItems()
        selected_items = self.filter_filename(selected_items)
        if len(selected_items) == 1:
            self.newname_dialog = self.renameDialog("重命名","请输入新文件名(为空则视为不改名,不得含有空格)",self)
            self.newname_dialog.set_LineEdit(selected_items[0].text())
            self.newname_dialog.show()
        elif len(selected_items) == 0:
            self.errSignal.emit("请选择需要修改的文件/文件夹")
            # self.reminder = MessageBox("提示", "请选择需要修改的文件夹", self)
            # self.reminder.show()
        else:
            self.errSignal.emit("不可同时重命名多个文件夹")
            # self.reminder = MessageBox("提示", "不可同时重命名多个文件夹", self)
            # self.reminder.show()

    def renameSlot(self,old_name,new_name):
        '''重命名槽'''
        if new_name:
            self.ADBCMD.renameFileOrDir(f"{self.current_path}", old_name, new_name)
            self.sucSignal.emit("重命名成功")
            self.refreshWidget()
        else:
            self.warnSignal.emit("新文件/文件夹名为空")

    def show_mkdirDialog(self):
        '''创建文件夹对话框'''
        self.newname_dialog = self.mkdirDialog("创建文件夹", "请输入新文件/文件夹名(为空则视为不新建,不得含有空格)", self)
        self.newname_dialog.show()

    def mkdirSlot(self,folder_name):
        '''创建文件夹槽'''
        if folder_name:
            self.ADBCMD.mkDir(self.current_path, folder_name)
            self.sucSignal.emit(f"文件夹{folder_name}创建成功")
            self.refreshWidget()
        else:
            self.warnSignal.emit("新文件夹名不得为空")

    def start_pasteThread(self):
        '''启动粘贴线程'''
        self.pastethread=self.pasteThread(self)
        self.pastethread.start()

    def start_delThread(self,selected_items):
        '''启动删除线程'''
        self.delthread=self.delThread(self)
        self.delthread.setItem(self.filter_filename(selected_items))
        self.delthread.start()

    def start_delThread_after_paste(self,selected_items):
        '''启动粘贴之后的删除线程'''
        self.delthread=self.delThread(self)
        self.delthread.setItem(selected_items)
        self.delthread.setCut(self.cut)
        self.delthread.start()

    def start_pushThread(self):
        '''启动push线程'''
        if os.path.exists(self.exPath_input.text()):
            self.pushthread = self.pushThread(self)
            self.pushthread.start()
        else:
            self.errSignal.emit("该机外路径不存在")

    def start_pullThread(self):
        '''启动pull线程'''
        selected_items = self.FileTableWidget.selectedItems()
        selected_items=self.filter_filename(selected_items)
        if len(selected_items):
            # ex_path, _ = QFileDialog.getOpenFileName(self, "Open File", r"C:")
            ex_path = QFileDialog.getExistingDirectory(self,"Open Dir",r"C:")
            if ex_path:
                self.pullthread = self.pullThread(self)
                self.pullthread.setItem(selected_items)
                self.pullthread.setExpath(ex_path)
                self.pullthread.start()
            else:
                pass
        else:
            self.warnSignal.emit("请先选择文件")
            # self.reminder = MessageBox("提示", "请选择目标路径", self)
            # self.reminder.show()

    def double_clicked(self):
        '''双击'''
        second_column_items = []
        selected_items=self.FileTableWidget.selectedItems()
        propert = None
        for item in selected_items:
            if item.column() == 1:  # 列索引为 1 表示第二列
                second_column_items.append(item)
            if item.column() == 2:
                propert = item.text()[0]
        # if len(re.findall("\.[0-9a-zA-Z]+", second_column_items[0].text())) == 1:
        if propert == "d":
            self.innerPath_returnPressed(f"{self.current_path}/{second_column_items[0].text()}")
        elif propert == "l":
            self.innerPath_returnPressed(f"{self.current_path}/{second_column_items[0].text()}")
        elif propert == "-":
            print("这是文件")
            self.warnSignal.emit("这是文件")

    def convert_size(self,b):
        '''转换大小'''
        suffixes = ['B', 'KB', 'MB', 'GB']
        suffix_index = 0
        while b >= 1024 and suffix_index < len(suffixes) - 1:
            b /= 1024
            suffix_index += 1
        # 格式化结果并添加单位后缀
        converted_size = '{:.2f} {}'.format(b, suffixes[suffix_index])
        return converted_size

    def on_combobox_changed(self,index):
        self.innerPath_returnPressed(self.innerPath_input.currentText())


    def back_upper_dir(self):
        '''返回至前一个目录'''
        if self.is_device_loaded():
            if self.is_innerPath_existed():
                self.innerPath_input.setText(self.last_path)
                self.cd_and_return(self.last_path)
                self.current_path=self.last_path


    def upper_dir(self):
        '''返回至上级目录'''
        if self.is_device_loaded():
            if self.is_innerPath_existed():
                upper_dir_path = self.current_path.split("/")
                upper_dir_path.pop(-1)
                upper_dir_path = "/".join(upper_dir_path)
                self.innerPath_input.setText(upper_dir_path)
                self.cd_and_return(upper_dir_path)
                self.current_path = upper_dir_path

    def innerPath_returnPressed(self,path):
        '''内部路径'''
        print(path)
        if self.is_device_loaded():
            if self.is_currentPath_existed():
                if self.ADBCMD.is_existed(path)=="存在":
                    self.last_path = self.current_path
                    self.innerPath_input.setText(path)
                    self.current_path = path
                    self.cd_and_return(path)
                else:
                    self.errSignal.emit("无法找到该路径")
            else:
                self.errSignal.emit("当前路径已不存在")


    def search(self,keyword):
        '''搜索'''
        if self.is_device_loaded():
            if self.is_innerPath_existed():
                self.cd_and_return(self.innerPath_input.text(), keyword)

    def cd_and_return(self,path,keyword=""):
        '''加载路径并返回路径下文件'''
        is_keyword_existed=False
        if keyword:
            is_keyword_existed=True
        data=list()
        information = self.ADBCMD.cd_and_return(path)
        information = information.split("\r\n")
        information.pop()
        # print(f"information:{information}")
        if information[0][0] == "t":#total x
            '''初始目录'''
            information.pop(0)
            for info in information:#['drwxr-xr-x', '1', 'root', 'root', '3488', '2023-12-12', '11:17', 'product']
                info_list = re.findall("\S+", info)
                if is_keyword_existed:
                    if re.search(keyword, info_list[-1]):
                        if info_list[0][0] == 'l':
                            info_list.pop()
                            info_list.pop()
                            if re.search(keyword, info_list[-1]):
                                data.append(
                                    ["link", info_list[-1], info_list[0], self.convert_size(int(info_list[4])),
                                     info_list[5]])
                        elif info_list[0][0] == 'd':
                            data.append(
                                ["dir", info_list[-1], info_list[0], self.convert_size(int(info_list[4])),
                                 info_list[5]])
                        elif info_list[0][0] == '-':
                            data.append(
                                ["file", info_list[-1], info_list[0], self.convert_size(int(info_list[4])),
                                 info_list[5]])
                else:
                    # print(info_list)
                    if info_list[0][0] == 'l':
                        info_list.pop()
                        info_list.pop()
                        data.append(
                            ["link", info_list[-1], info_list[0], self.convert_size(int(info_list[4])),
                             info_list[5]])
                    elif info_list[0][0] == 'd':
                        data.append(
                            ["dir", info_list[-1], info_list[0], self.convert_size(int(info_list[4])),
                             info_list[5]])
                    elif info_list[0][0] == '-':
                        data.append(
                            ["file", info_list[-1], info_list[0], self.convert_size(int(info_list[4])),
                             info_list[5]])
                QGuiApplication.processEvents()
            self.number_label.setText(f"数量：更新中")
            self.set_FileTableWidget_by_data(data)
            self.number_label.setText(f"数量：{self.FileTableWidget.rowCount()}")
        else:#['lrw-r--r--', '1', 'root', 'root', '21', '2009-01-01', '08:00', 'sdcard', '->', '/storage/self/primary']
            info_list = re.findall("\S+", information[0])
            link = info_list[-1]
            true_path = self.find_true_path(link)
            return self.cd_and_return(true_path,keyword=keyword)



    def refreshWidget(self):
        '''刷新组件'''
        if self.is_device_loaded():
            self.cd_and_return(self.current_path)


    def find_true_path(self,link_path):
        '''寻找真实路径'''
        information = self.ADBCMD.cd_and_return(link_path)
        information = information.split("\r\n")
        information.pop()
        info_list = re.findall("\S+", information[0])
        if info_list[0][0] == "t":
            return link_path
        elif info_list[0][0] == "l":
            # 继续找
            return info_list[-1]
        elif info_list[0][0] == "-":
            self.warnSignal.emit("这是链接文件")
            print("这是链接文件")
            #死循环 前往该文件所在目录
            dir_where_file_in = re.findall("/[A-Za-z0-9]+",info_list[-1])
            print(dir_where_file_in)
            dir_where_file_in.pop()
            dir_where_file_in = "".join(dir_where_file_in)
            print(f"This is dir_where_file_in{dir_where_file_in}")
            return dir_where_file_in

    def set_FileTableWidget_by_data(self,data):
        '''根据data设置Table组件'''
        self.FileTableWidget.setRowCount(0)
        self.FileTableWidget.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for col_index, cell_data in enumerate(row_data):
                if col_index:
                    item = QTableWidgetItem(cell_data)
                    if col_index in range(2,5):
                        item.setTextAlignment(Qt.AlignCenter)
                    self.FileTableWidget.setItem(row_index, col_index, item)
                else:
                    Icon_label = BodyLabel(self)
                    # Icon_label.setFixedSize(80,20)
                    Icon_label.setPixmap(QPixmap(source_path(f"icon/{cell_data}.png")))
                    Icon_label.setAlignment(Qt.AlignCenter)
                    self.FileTableWidget.setCellWidget(row_index, col_index, Icon_label)
                QGuiApplication.processEvents()
        for row in range(self.FileTableWidget.rowCount()):
            for col in range(1, 5):  # 第2至第5列
                item = self.FileTableWidget.item(row, col)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.FileTableWidget.repaint()

    def handle_current_device_changed(self,value):
        '''处理当前设备改变'''
        if self.ADBCMD.current_device != value:
            print(f"handle_current_device_changed {value}")
            self.ADBCMD.set_current_device(value)

    class pasteThread(QThread):
        def copy_Dir(self, src_path, dst_path):
            self.parent().ADBCMD.copy_Dir(src_path, dst_path)
            self.parent().update_progressBarValue()
            # self.parent().cd_and_return(self.parent().current_path)

        def copy_File(self, src_path, dst_path):
            self.parent().ADBCMD.copy_File(src_path, dst_path)
            self.parent().update_progressBarValue()
            # self.parent().cd_and_return(self.parent().current_path)

        def run(self):
            self.parent().progress_max = len(self.parent().copy2paste_dirlist) + len(self.parent().copy2paste_filelist)
            self.parent().progress_per = 0
            # print(self.parent().current_path)
            if len(self.parent().copy2paste_dirlist) + len(self.parent().copy2paste_filelist):
                if len(self.parent().copy2paste_dirlist):
                    for dir_path in self.parent().copy2paste_dirlist:
                        self.copy_Dir(dir_path, f"{self.parent().current_path}")
                if len(self.parent().copy2paste_filelist):
                    for file_path in self.parent().copy2paste_filelist:
                        self.copy_File(file_path, f"{self.parent().current_path}")
                self.parent().sucSignal.emit("粘贴成功")
                self.quit()
                self.wait()
                self.parent().refreshSignal.emit()
            else:
                self.parent().warnSignal.emit("请先复制/剪切文件")
                self.quit()
                self.wait()

    class delThread(QThread):

        items=None
        cut=False

        def setItem(self,selected_items):
            self.items=selected_items

        def setCut(self,Cut):
            self.cut=Cut

        def run(self):
            if len(self.items):
                if not self.cut:
                    if len(self.items) <= int(self.parent().ADBCMD.get_num(self.parent().current_path)):
                        self.parent().progress_max = len(self.items)
                        self.parent().progress_per = 0
                        for item in self.items:
                            self.parent().ADBCMD.delete_dir_or_file(f"{self.parent().current_path}/{item.text()}")
                            self.parent().update_progressBarValue()
                        self.parent().sucSignal.emit("删除成功")
                    else:
                        print("error")
                else:
                    self.parent().progress_max = len(self.items)
                    self.parent().progress_per = 0
                    for item in self.items:
                        self.parent().ADBCMD.delete_dir_or_file(f"{item}")
                        self.parent().update_progressBarValue()
                    self.parent().sucSignal.emit("删除成功")
            else:
                self.parent().warnSignal.emit("请先选择文件")
            self.cut=False
            self.parent().cut=False
            self.quit()
            self.wait()
            self.parent().refreshSignal.emit()

    class pullThread(QThread):

        items=None
        ex_path=None

        def setItem(self,selected_items):
            self.items=selected_items

        def setExpath(self,ex_path):
            self.ex_path=ex_path

        def run(self):
            self.parent().progress_max = len(self.items)
            self.parent().progress_per = 0
            if len(self.items) == int(self.parent().ADBCMD.get_num(self.parent().current_path)):
                # print("全拉")
                self.parent().ADBCMD.pull(f"{self.parent().current_path}", f"{self.ex_path}")
                self.parent().ProgressBar.setValue(100)
                self.parent().sucSignal.emit("Pull成功")
            else:
                # print("1个个拉")
                self.parent().progress_max = len(self.items)
                for item in self.items:
                    self.parent().ADBCMD.pull(f"{self.parent().current_path}/{item.text()}",
                                              f"{self.ex_path}/{item.text()}")
                    self.parent().update_progressBarValue()
                self.parent().ProgressBar.setValue(100)
                self.parent().sucSignal.emit("Pull成功")
            self.quit()
            self.wait()
            self.parent().refreshSignal.emit()

    class pushThread(QThread):

        ex_path=None

        def run(self):
            self.parent().progress_max = 1
            self.parent().progress_per = 0
            self.parent().ADBCMD.push(f"{self.parent().exPath_input.text()}",f"{self.parent().current_path}/{os.path.basename(self.parent().exPath_input.text())}")
            self.parent().update_progressBarValue()
            self.quit()
            self.wait()
            self.parent().refreshSignal.emit()

    class drop2pushThread(QThread):

        urls=None

        def setUrls(self,selected_urls):
            self.urls=selected_urls

        def run(self):
            self.parent().progress_max = len(self.urls)
            self.parent().progress_per = 0
            if len(self.urls)==1:
                self.parent().ADBCMD.push(f"{self.urls[0]}", f"{self.parent().current_path}/{os.path.basename(self.urls[0])}")
                self.parent().update_progressBarValue()
            elif len(self.urls)>=1:
                for url in self.urls:
                    self.parent().ADBCMD.push(f"{url}", f"{self.parent().current_path}/{os.path.basename(url)}")
                    self.parent().update_progressBarValue()
            self.quit()
            self.wait()
            self.parent().refreshSignal.emit()


    class renameDialog(MessageBoxBase):
        """重命名对话框类"""
        yesSignal = Signal(str)
        cancelSignal = Signal()
        old_name=None

        def __init__(self,title: str, content: str,parent=None):
            super().__init__(parent)
            self.titleLabel = SubtitleLabel(title, self)
            self.nameLineEdit = LineEdit(self)

            self.nameLineEdit.setPlaceholderText(content)
            self.nameLineEdit.setClearButtonEnabled(True)

            self.viewLayout.addWidget(self.titleLabel)
            self.viewLayout.addWidget(self.nameLineEdit)

            self.yesButton.setText('确认')
            self.cancelButton.setText('取消')

            self.widget.setMinimumWidth(450)
            self.nameLineEdit.returnPressed.connect(self.yesButton.click)
            self.yesButton.clicked.connect(lambda :self.parent().renameSlot(self.old_name,self.nameLineEdit.text()))
            # self.hideYesButton()

        def set_LineEdit(self,old_name):
            self.nameLineEdit.setText(old_name)
            self.old_name=old_name

    class mkdirDialog(MessageBoxBase):

        yesSignal = Signal(str)
        cancelSignal = Signal()

        def __init__(self,title: str, content: str,parent=None):
            super().__init__(parent)
            self.titleLabel = SubtitleLabel(title, self)
            self.nameLineEdit = LineEdit(self)

            self.nameLineEdit.setPlaceholderText(content)
            self.nameLineEdit.setClearButtonEnabled(True)

            self.viewLayout.addWidget(self.titleLabel)
            self.viewLayout.addWidget(self.nameLineEdit)

            self.yesButton.setText('确认')
            self.cancelButton.setText('取消')

            self.widget.setMinimumWidth(450)
            self.nameLineEdit.returnPressed.connect(self.yesButton.click)
            self.yesButton.clicked.connect(lambda :self.parent().mkdirSlot(self.nameLineEdit.text()))
            # self.hideYesButton()

    '''拖放'''

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        url_list=list()
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                url_list.append(file_path)
            self.drop2pushthread = self.drop2pushThread(self)
            self.drop2pushthread.setUrls(url_list)
            self.drop2pushthread.start()

    '''快捷键'''
    def copy_shortCut(self):
        self.copySlot()

    def cut_shortCut(self):
        self.copySlot(cut=True)

    def paste_shortCut(self):
        self.pasteSlot()

    def del_shortCut(self):
        self.delSlot()

    def rename_shortCut(self):
        self.show_renameDialog()

    def mkdir_shortCut(self):
        self.show_mkdirDialog()

    def pull_shortCut(self):
        self.start_pullThread()

    def back_shortCut(self):
        self.back_upper_dir()

    def refresh_shortCut(self):
        self.refreshWidget()

