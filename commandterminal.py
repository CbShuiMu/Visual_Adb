import os
import re
import sys
from adb_commond import ADBCMD
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QAbstractItemView, QMenu,QMessageBox,QInputDialog
from PySide6.QtCore import Qt,QThread,Slot,Signal,QProcess
from PySide6.QtGui import QAction, QShortcut, QKeySequence, QIcon, QColor, QFont
from PySide6 import QtCore, QtGui, QtWidgets

from ui.commandTerminal import Ui_commandTerminal
from adb_commond import ADBCMD

class commandTermianl(QWidget,Ui_commandTerminal):

    ADBCMD=ADBCMD()
    ADBCMD.current_interface="commandterminal"
    current_path=None
    sucSignal = Signal(str)
    warnSignal = Signal(str)
    errSignal = Signal(str)
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.sucSignal.connect(self.parent().createSuccessInfoBar)
        self.warnSignal.connect(self.parent().createWarningInfoBar)
        self.errSignal.connect(self.parent().createErrorInfoBar)
        # self.command_input.returnPressed.connect(lambda:self.execute_command(self.command_input.text()))
        self.TextEdit.setStyleSheet("background-color: black;")
        font = QFont()
        font.setPointSize(14)  # 设置字体大小
        # font.setBold(True)  # 设置字体为粗体
        self.TextEdit.setFont(font)  # 设置字体格式
        self.TextEdit.setTextColor(QColor("green"))
        self.process = QProcess()

        # 将进程输出连接到槽函数
        self.process.readyReadStandardOutput.connect(self.read_output)

        # 将命令行输入框的回车事件连接到槽函数
        self.command_input.returnPressed.connect(self.execute_command)

        # 嵌入 adb shell
        self.embed_adb_shell()

    def is_device_loaded(self):
        '''设备是否加载'''
        if self.ADBCMD.current_device:
            return True
        else:
            self.warnSignal.emit("设备未选择")
            return False

    def embed_adb_shell(self):
        '''嵌入adb shell'''
        self.process.start("adb", ["shell"])
        self.process.waitForStarted()

    def execute_command(self):
        '''执行命令'''
        # 从命令行输入框获取命令
        if self.is_device_loaded():
            command = self.command_input.text()
            if command.startswith("cd /"):
                path = command.lstrip("cd ")
                print(path)
                print(command)
                if self.ADBCMD.is_existed(path) == "存在":
                    path = command.lstrip("cd /")
                    self.current_path = path
                    self.TextEdit.append(f"{self.ADBCMD.get_prop_deviceName()}:/{self.current_path}#")
                elif self.ADBCMD.is_existed(path) == "不存在":
                    self.TextEdit.append("该路径不存在")
                self.command_input.clear()
            elif command == "cd ..":
                self.current_path = ""
                self.TextEdit.append(f"{self.ADBCMD.get_prop_deviceName()}:/{self.current_path}#")
                self.command_input.clear()
            else:
                # 发送命令给 adb shell 进程
                self.process.write(f"cd /{self.current_path}".encode("UTF-8") + b"\n")
                self.process.write(command.encode("UTF-8") + b"\n")
                self.TextEdit.append(
                    f"{self.ADBCMD.get_prop_deviceName()}:/{self.current_path}#{self.command_input.text()}")
                self.command_input.clear()

    def read_output(self):
        '''输出结果(cp936编码)'''
        output = self.process.readAllStandardOutput().data()
        text = output.decode("cp936")
        self.TextEdit.append(text)

    def closeEvent(self, event):
        # 在窗口关闭时终止 adb shell 进程
        self.process.terminate()
        super().closeEvent(event)


    def handle_current_device_changed(self,value):
        if self.ADBCMD.current_device != value:
            # print(f"handle_current_device_changed {value}")
            self.ADBCMD.set_current_device(value)
