# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'commandTerminal.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (LineEdit, TextEdit)

class Ui_commandTerminal(object):
    def setupUi(self, commandTerminal):
        if not commandTerminal.objectName():
            commandTerminal.setObjectName(u"commandTerminal")
        commandTerminal.resize(665, 566)
        self.horizontalLayout = QHBoxLayout(commandTerminal)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 40, 10, 10)
        self.command_input = LineEdit(commandTerminal)
        self.command_input.setObjectName(u"command_input")

        self.verticalLayout.addWidget(self.command_input)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.TextEdit = TextEdit(commandTerminal)
        self.TextEdit.setObjectName(u"TextEdit")
        self.TextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.TextEdit)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(commandTerminal)

        QMetaObject.connectSlotsByName(commandTerminal)
    # setupUi

    def retranslateUi(self, commandTerminal):
        commandTerminal.setWindowTitle(QCoreApplication.translate("commandTerminal", u"Form", None))
    # retranslateUi

