import os
import re
import sys
from adb_commond import ADBCMD
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QAbstractItemView, QMenu,QMessageBox,QInputDialog
from PySide6.QtCore import Qt,QThread,Slot,Signal
from PySide6.QtGui import QAction, QShortcut, QKeySequence, QIcon, QMouseEvent, QImage, QPixmap, QPainter, QColor, \
    QGuiApplication
from PySide6 import QtCore, QtGui, QtWidgets
import scrcpy

from ui.wirelessProjection import Ui_wirelessProjection
from adb_commond import ADBCMD

class wirelessProjection(QWidget,Ui_wirelessProjection):

    ADBCMD=ADBCMD()
    ADBCMD.current_interface="wirelessprojection"
    sucSignal = Signal(str)
    errSignal = Signal(str)
    warnSignal = Signal(str)
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.max_width = 850 # 设置手机投屏宽度
        self.connect_button.clicked.connect(self.start_connectThread)
        self.stop_button.clicked.connect(self.stop_connectThread)
        self.back_button.clicked.connect(self.click_key(scrcpy.KEYCODE_BACK))
        self.back_button.setToolTip("返回")
        self.home_button.clicked.connect(self.click_key(scrcpy.KEYCODE_HOME))
        self.home_button.setToolTip("返回主页面")
        self.recent_button.clicked.connect(self.click_key(scrcpy.KEYCODE_APP_SWITCH))
        self.recent_button.setToolTip("后台")
        self.video.mousePressEvent = self.mouse_event(scrcpy.ACTION_DOWN)
        self.video.mouseMoveEvent = self.mouse_event(scrcpy.ACTION_MOVE)
        self.video.mouseReleaseEvent = self.mouse_event(scrcpy.ACTION_UP)
        self.mouse_thread = self.signThread(self, self.mouse_exe, int, int, int)
        self.sucSignal.connect(self.parent().createSuccessInfoBar)
        self.warnSignal.connect(self.parent().createWarningInfoBar)
        self.errSignal.connect(self.parent().createErrorInfoBar)


    def is_device_loaded(self):
        if self.ADBCMD.current_device:
            return True
        else:
            self.warnSignal.emit("设备未选择")
            return False

    def start_connectThread(self):
        if self.is_device_loaded():
            self.connectthread = self.connectThread(self)
            self.now_client = scrcpy.Client(device=f"{self.ADBCMD.current_device}", bitrate=2000000000)
            self.now_client.add_listener(scrcpy.EVENT_FRAME, self.main_frame)
            self.connectthread.start()
            self.InfoBadge.setText("已连接")
            self.InfoBadge.lightBackgroundColor=QColor(108, 203, 95)
            QGuiApplication.processEvents()

    def stop_connectThread(self):
        if self.is_device_loaded():
            self.connectthread.stop()
            self.InfoBadge.setText("未连接")
            self.InfoBadge.lightBackgroundColor=QColor(255, 0, 0)
            QGuiApplication.processEvents()

    def handle_current_device_changed(self,value):
        if self.ADBCMD.current_device != value:
            # print(f"handle_current_device_changed {value}")
            self.ADBCMD.set_current_device(value)

    def click_key(self, key_value: int):
        """按键事件"""
        def key_event():
            self.now_client.control.keycode(key_value, scrcpy.ACTION_DOWN)
            self.now_client.control.keycode(key_value, scrcpy.ACTION_UP)
        return key_event

    def mouse_exe(self, x, y, action):
        """执行鼠标事件"""
        self.now_client.control.touch(x-310, y, action)

    def mouse_event(self, action=scrcpy.ACTION_DOWN):
        """鼠标事件"""

        def event(evt: QMouseEvent):
            focused_widget = QApplication.focusWidget()
            if focused_widget is not None:
                focused_widget.clearFocus()
            ratio = self.max_width / max(self.now_client.resolution)
            self.mouse_thread.send_sign(evt.position().x() / ratio, evt.position().y() / ratio, action)

        return event

    def main_frame(self, frame):
        """监听设备屏幕数据,设置控制窗口图像"""
        if frame is not None:
            ratio = self.max_width / max(self.now_client.resolution)
            image = QImage(
                frame,
                frame.shape[1],
                frame.shape[0],
                # frame.shape[1] * 3,
                QImage.Format_BGR888,
            )
            pix = QPixmap(image)
            pix.setDevicePixelRatio(1 / ratio)
            self.video.setPixmap(pix)

    class connectThread(QThread):
        resultReady = Signal(str)
        def run(self):
            self.parent().now_client.start()

        def stop(self):
            self.parent().now_client.stop()

    class signThread(QThread):
        """信号线程"""

        def __new__(cls, parent: QWidget, func, *types: type):
            cls.update_date = Signal(*types)
            return super().__new__(cls)

        def __init__(self, parent: QWidget, func, *types: type):
            """信号线程初始化"""
            super().__init__(parent)  # 调用父类构造函数
            self.sign = None
            self.update_date.connect(func)

        def send_sign(self, *args):
            """使用SignThread发送信号"""
            self.sign = args
            self.start()

        def run(self):
            """信号线程执行时执行此函数"""
            self.update_date.emit(*self.sign)