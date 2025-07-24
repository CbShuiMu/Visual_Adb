# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connect.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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

from qfluentwidgets import (BodyLabel, ComboBox, LineEdit, ToolButton,FluentIcon)

class Ui_Connect(object):
    def setupUi(self, Connect):
        if not Connect.objectName():
            Connect.setObjectName(u"Connect")
        Connect.resize(665, 566)
        self.horizontalLayout_6 = QHBoxLayout(Connect)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 40, -1, -1)
        self.connect_label = BodyLabel(Connect)
        self.connect_label.setObjectName(u"connect_label")
        self.connect_label.setProperty("pixelFontSize", 25)

        self.verticalLayout_3.addWidget(self.connect_label)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.device_combobox = ComboBox(Connect)
        self.device_combobox.setObjectName(u"device_combobox")

        self.horizontalLayout.addWidget(self.device_combobox)

        self.connect_button = ToolButton(Connect)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setIcon(FluentIcon.ACCEPT_MEDIUM)

        self.horizontalLayout.addWidget(self.connect_button)

        self.horizontalSpacer = QSpacerItem(350, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.wirelessConnect_label = BodyLabel(Connect)
        self.wirelessConnect_label.setObjectName(u"wirelessConnect_label")
        self.wirelessConnect_label.setProperty("pixelFontSize", 25)

        self.verticalLayout_3.addWidget(self.wirelessConnect_label)

        self.verticalSpacer_3 = QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.port_label = BodyLabel(Connect)
        self.port_label.setObjectName(u"port_label")
        self.port_label.setProperty("pixelFontSize", 20)

        self.verticalLayout.addWidget(self.port_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.port_value = LineEdit(Connect)
        self.port_value.setObjectName(u"port_value")

        self.horizontalLayout_2.addWidget(self.port_value)

        self.horizontalSpacer_2 = QSpacerItem(480, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.address_label = BodyLabel(Connect)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setProperty("pixelFontSize", 20)

        self.verticalLayout_2.addWidget(self.address_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.address_value = LineEdit(Connect)
        self.address_value.setObjectName(u"address_value")

        self.horizontalLayout_3.addWidget(self.address_value)

        self.wirelessConnect_button = ToolButton(Connect)
        self.wirelessConnect_button.setObjectName(u"wirelessConnect_button")
        self.wirelessConnect_button.setIcon(FluentIcon.WIFI)

        self.horizontalLayout_3.addWidget(self.wirelessConnect_button)

        self.horizontalSpacer_3 = QSpacerItem(405, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)


        self.retranslateUi(Connect)

        QMetaObject.connectSlotsByName(Connect)
    # setupUi

    def retranslateUi(self, Connect):
        Connect.setWindowTitle(QCoreApplication.translate("Connect", u"Form", None))
        self.connect_label.setText(QCoreApplication.translate("Connect", u"\u5f53\u524d\u8fde\u63a5\u8bbe\u5907", None))
        self.wirelessConnect_label.setText(QCoreApplication.translate("Connect", u"\u65e0\u7ebf\u8fde\u63a5", None))
        self.port_label.setText(QCoreApplication.translate("Connect", u"\u7aef\u53e3", None))
        self.address_label.setText(QCoreApplication.translate("Connect", u"IP\u5730\u5740", None))
    # retranslateUi

