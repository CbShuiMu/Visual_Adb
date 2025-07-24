import os
import re
import sys
from adb_commond import ADBCMD
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QAbstractItemView, QMenu,QMessageBox,QInputDialog
from PySide6.QtCore import Qt,QThread,Slot,Signal
from PySide6.QtGui import QAction,QShortcut,QKeySequence,QIcon,QDragEnterEvent,QDropEvent
from PySide6 import QtCore, QtGui, QtWidgets

from qfluentwidgets import SplitFluentWindow, FluentIcon, InfoBar, InfoBarPosition
from adb_commond import ADBCMD
from connect import connect
from deviceinfo import deviceInfo
from filemanager import fileManager
from commandterminal import commandTermianl
from screencapture import screenCapture
from logrecord import logRecord
from wirelessprojection import wirelessProjection
from apkinstall import apkInstall

class Demo(SplitFluentWindow):
    ADBCMD = ADBCMD()
    def __init__(self):
        super().__init__()
        # self.setAcceptDrops(True)
        self.setWindowTitle('Visual ADB by CbShuiMu')
        self.setWindowIcon(QIcon(""))
        self.connect_Interface = connect(self)
        self.deviceInfo_Interface = deviceInfo(self)
        self.fileManager_Interface = fileManager(self)
        self.apkInstall_Interface = apkInstall(self)
        self.commandTerminal_Interface = commandTermianl(self)
        self.screenCapture_Interface = screenCapture(self)
        self.logRecord_Interface = logRecord(self)
        self.wirelessprojection_Interface=wirelessProjection(self)
        self.addSubInterface(self.connect_Interface,FluentIcon.CONNECT,"Connect")
        self.addSubInterface(self.deviceInfo_Interface,FluentIcon.INFO,"Device Info")
        self.addSubInterface(self.fileManager_Interface, FluentIcon.FOLDER, "File Manager")
        self.addSubInterface(self.apkInstall_Interface, FluentIcon.DOWNLOAD, "Install")
        self.addSubInterface(self.commandTerminal_Interface,FluentIcon.COMMAND_PROMPT,"Command Terminal")
        self.addSubInterface(self.wirelessprojection_Interface,FluentIcon.PROJECTOR,"Wireless Projection")
        self.addSubInterface(self.logRecord_Interface,FluentIcon.DICTIONARY,"Log Record")
        self.addSubInterface(self.screenCapture_Interface, FluentIcon.CAMERA, "Screen Capture")
        # self.navigationInterface.addWidget(
        #     routeKey='device',
        #     widget=NavigationWidget(self),
        #     position=NavigationItemPosition.BOTTOM
        # )

    def createErrorInfoBar(self,content):
        '''Error message notification'''
        self.errorInfoBar = InfoBar.error(
            title='错误',
            content=f"{content}",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,    # won't disappear automatically
            parent=self
        )

    def createWarningInfoBar(self,content):
        '''Warning message notification'''
        InfoBar.warning(
            title='提示',
            content=f"{content}",
            orient=Qt.Horizontal,
            isClosable=False,   # disable close button
            position=InfoBarPosition.BOTTOM_RIGHT,
            duration=2000,
            parent=self
        )

    def createSuccessInfoBar(self,content):
        '''Success message notification'''
        InfoBar.success(
            title='成功',
            content=f"{content}",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self
        )

    def refresh_combobox(self):
        '''Refresh combobox options'''
        combobox_device_list=list()
        for item in self.connect_Interface.device_combobox.items:
            combobox_device_list.append(item.text)
        ADB_deviceName_list=self.ADBCMD.get_deviceName()
        if len(ADB_deviceName_list) == 1 and self.connect_Interface.ADBCMD.current_device!=ADB_deviceName_list[0]:
            self.connect_Interface.device_combobox.clear()
            self.connect_Interface.device_combobox.addItems(ADB_deviceName_list)
            self.connect_Interface.set_current_device(ADB_deviceName_list[0])
        elif len(ADB_deviceName_list) == 0:
            self.connect_Interface.set_current_device("")
        else:
            if (combobox_device_list == ADB_deviceName_list):
                pass
            else:
                self.connect_Interface.device_combobox.clear()
                self.connect_Interface.device_combobox.addItems(ADB_deviceName_list)

    class refresh_device_Thread(QThread):
        '''Device refresh thread'''
        def run(self):
            while True:
                self.parent().refresh_combobox()

    # '''Drag and drop'''
    #
    # def dragEnterEvent(self, event: QDragEnterEvent):
    #     if event.mimeData().hasUrls():
    #         event.acceptProposedAction()
    #
    # def dropEvent(self, event: QDropEvent):
    #     if event.mimeData().hasUrls():
    #         for url in event.mimeData().urls():
    #             file_path = url.toLocalFile()
    #             print("Dropped file:", file_path)

if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    # QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    '''信号与槽'''
    w.connect_Interface.current_device_changed.connect(w.deviceInfo_Interface.handle_current_device_changed)
    w.connect_Interface.current_device_changed.connect(w.fileManager_Interface.handle_current_device_changed)
    w.connect_Interface.current_device_changed.connect(w.apkInstall_Interface.handle_current_device_changed)
    w.connect_Interface.current_device_changed.connect(w.commandTerminal_Interface.handle_current_device_changed)
    w.connect_Interface.current_device_changed.connect(w.screenCapture_Interface.handle_current_device_changed)
    w.connect_Interface.current_device_changed.connect(w.logRecord_Interface.handle_current_device_changed)
    w.connect_Interface.current_device_changed.connect(w.wirelessprojection_Interface.handle_current_device_changed)
    '''QThread'''
    refreshDeviceThread = Demo.refresh_device_Thread(w)
    refreshDeviceThread.start()
    app.exec()