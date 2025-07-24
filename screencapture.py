import os
import shutil
import re
import sys
from adb_commond import ADBCMD
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QAbstractItemView, QMenu,QMessageBox,QInputDialog
from PySide6.QtCore import Qt,QThread,Slot,Signal
from PySide6.QtGui import QAction,QShortcut,QKeySequence,QIcon
from PySide6 import QtCore, QtGui, QtWidgets

from ui.screenCapture import Ui_screenCapture
from adb_commond import ADBCMD

class screenCapture(QWidget,Ui_screenCapture):

    ADBCMD=ADBCMD()
    ADBCMD.current_interface="screenCapture"
    sucSignal = Signal(str)
    errSignal = Signal(str)
    warnSignal = Signal(str)


    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.capture_button.clicked.connect(self.start_captureThread)
        self.save_button.clicked.connect(self.save_file)
        self.sucSignal.connect(self.parent().createSuccessInfoBar)
        self.warnSignal.connect(self.parent().createWarningInfoBar)
        self.errSignal.connect(self.parent().createErrorInfoBar)

    def is_device_loaded(self):
        '''设备加载'''
        if self.ADBCMD.current_device:
            return True
        else:
            self.warnSignal.emit("设备未选择")
            return False

    def save_file(self):
        '''文件保存'''
        try:
            if self.is_device_loaded():
                save_path = QFileDialog.getExistingDirectory(self, "Open Dir", "C:/")
                if save_path:
                    print("选择的目录:", save_path)
                    shutil.copy(os.path.join(os.getcwd(), "screenshot.png"), save_path)
                else:
                    print("用户取消了选择")
        except TypeError:
            print("用户取消了选择")

    def capture_screen(self,img_path):
        '''截屏'''
        # img_path = self.ADBCMD.capture_screen()
        self.ImageLabel.setImage(img_path)
        self.ImageLabel.adjustSize()

    def start_captureThread(self):
        if self.is_device_loaded():
            self.capturethread = self.captureThread(self)
            self.capturethread.resultReady.connect(self.capture_screen)
            self.capturethread.start()

    def handle_current_device_changed(self,value):
        if self.ADBCMD.current_device != value:
            # print(f"handle_current_device_changed {value}")
            self.ADBCMD.set_current_device(value)

    class captureThread(QThread):
        resultReady = Signal(str)
        def run(self):
            img_path = self.parent().ADBCMD.capture_screen()
            self.resultReady.emit(img_path)
            self.quit()
            self.wait()