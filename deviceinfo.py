import os
import re
import sys
from adb_commond import ADBCMD
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QAbstractItemView, QMenu,QMessageBox,QInputDialog
from PySide6.QtCore import Qt,QThread,Slot,Signal
from PySide6.QtGui import QAction,QShortcut,QKeySequence,QIcon
from PySide6 import QtCore, QtGui, QtWidgets

from ui.deviceInfo import Ui_deviceInfo
from adb_commond import ADBCMD

class deviceInfo(QWidget,Ui_deviceInfo):

    ADBCMD=ADBCMD()
    ADBCMD.current_interface="deviceInfo"
    sucSignal = Signal(str)
    errSignal = Signal(str)
    warnSignal = Signal(str)

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.sucSignal.connect(self.parent().createSuccessInfoBar)
        self.warnSignal.connect(self.parent().createWarningInfoBar)
        self.errSignal.connect(self.parent().createErrorInfoBar)

    def refresh_info(self):
        '''刷新信息'''
        prop_list=self.ADBCMD.get_device_info()
        self.protocolVersion_value.setText(prop_list[0])
        self.productName_value.setText(prop_list[1])
        self.modelName_value.setText(prop_list[2])
        self.deviceName_value.setText(prop_list[3])
        self.resolution_value.setText(self.ADBCMD.get_resolution())

    def handle_current_device_changed(self,value):
        '''处理当前设备改变'''
        if self.ADBCMD.current_device != value:
            # print(f"handle_current_device_changed {value}")
            self.ADBCMD.set_current_device(value)
            self.refresh_info()