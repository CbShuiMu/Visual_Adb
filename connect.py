import os
import re
import sys

from qfluentwidgets import InfoBarPosition, InfoBar

from adb_commond import ADBCMD
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QAbstractItemView, QMenu,QMessageBox,QInputDialog
from PySide6.QtCore import Qt,QThread,Slot,Signal
from PySide6.QtGui import QAction,QShortcut,QKeySequence,QIcon
from PySide6 import QtCore, QtGui, QtWidgets

from ui.connect import Ui_Connect
from adb_commond import ADBCMD

class connect(QWidget,Ui_Connect):

    ADBCMD=ADBCMD()
    ADBCMD.current_interface="connect"
    current_device_changed = Signal(str)
    current_deviceInfo_changed = Signal()
    sucSignal = Signal(str)
    errSignal = Signal(str)
    warnSignal = Signal(str)

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.device_combobox.currentTextChanged.connect(self.ADBCMD.set_device_wait2connect)
        self.connect_button.clicked.connect(self.connect_device)
        self.wirelessConnect_button.clicked.connect(self.connect_device_by_wifi)
        self.sucSignal.connect(self.parent().createSuccessInfoBar)
        self.warnSignal.connect(self.parent().createWarningInfoBar)
        self.errSignal.connect(self.parent().createErrorInfoBar)

    def connect_device(self):
        '''连接设备'''
        if self.device_combobox.currentText():
            self.set_current_device(self.device_combobox.currentText())
            self.sucSignal.emit(f"设备{self.device_combobox.currentText()} 连接成功")
        else:
            self.warnSignal.emit("请选择设备")

    def connect_device_by_wifi(self):
        '''通过WIFI连接设备'''
        message = self.ADBCMD.wifi_connect(self.port_value.text(), self.address_value.text())
        print(message)
        if message:
            self.sucSignal.emit(f"设备{self.ADBCMD.current_device} 无线连接成功")
        else:
            self.errSignal.emit(f"无线连接失败 请检查端口与IP地址是否存在冲突且可用")

    def set_current_device(self,device):
        '''设置当前设备'''
        self.ADBCMD.set_current_device(device)
        self.connect_label.setText(f"当前连接设备:{self.ADBCMD.get_prop_brand()} {device}")
        if device == self.ADBCMD.current_device:
            self.current_device_changed.emit(f"{device}")
            # self.current_deviceInfo_changed.emit()
