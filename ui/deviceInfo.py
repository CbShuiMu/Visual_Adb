# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deviceInfo.ui'
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

from qfluentwidgets import (BodyLabel, CaptionLabel)

class Ui_deviceInfo(object):
    def setupUi(self, deviceInfo):
        if not deviceInfo.objectName():
            deviceInfo.setObjectName(u"deviceInfo")
        deviceInfo.resize(665, 566)
        self.horizontalLayout_5 = QHBoxLayout(deviceInfo)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 40, 10, 10)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.protocolVersion_intro = CaptionLabel(deviceInfo)
        self.protocolVersion_intro.setObjectName(u"protocolVersion_intro")
        self.protocolVersion_intro.setProperty("pixelFontSize", 15)

        self.verticalLayout.addWidget(self.protocolVersion_intro)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.protocolVersion_label = BodyLabel(deviceInfo)
        self.protocolVersion_label.setObjectName(u"protocolVersion_label")
        self.protocolVersion_label.setProperty("pixelFontSize", 20)

        self.horizontalLayout_8.addWidget(self.protocolVersion_label)

        self.protocolVersion_value = BodyLabel(deviceInfo)
        self.protocolVersion_value.setObjectName(u"protocolVersion_value")
        self.protocolVersion_value.setProperty("pixelFontSize", 20)

        self.horizontalLayout_8.addWidget(self.protocolVersion_value)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_4 = QSpacerItem(10, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.productName_intro = CaptionLabel(deviceInfo)
        self.productName_intro.setObjectName(u"productName_intro")
        self.productName_intro.setProperty("pixelFontSize", 15)

        self.verticalLayout_4.addWidget(self.productName_intro)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.productName_label = BodyLabel(deviceInfo)
        self.productName_label.setObjectName(u"productName_label")
        self.productName_label.setProperty("pixelFontSize", 20)

        self.horizontalLayout_7.addWidget(self.productName_label)

        self.productName_value = BodyLabel(deviceInfo)
        self.productName_value.setObjectName(u"productName_value")
        self.productName_value.setProperty("pixelFontSize", 20)

        self.horizontalLayout_7.addWidget(self.productName_value)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(10, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.modelName_intro = CaptionLabel(deviceInfo)
        self.modelName_intro.setObjectName(u"modelName_intro")
        self.modelName_intro.setProperty("pixelFontSize", 15)

        self.verticalLayout_5.addWidget(self.modelName_intro)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.modelName_label = BodyLabel(deviceInfo)
        self.modelName_label.setObjectName(u"modelName_label")
        self.modelName_label.setProperty("pixelFontSize", 20)

        self.horizontalLayout_4.addWidget(self.modelName_label)

        self.modelName_value = BodyLabel(deviceInfo)
        self.modelName_value.setObjectName(u"modelName_value")
        self.modelName_value.setProperty("pixelFontSize", 20)

        self.horizontalLayout_4.addWidget(self.modelName_value)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(10, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.deviceName_intro = CaptionLabel(deviceInfo)
        self.deviceName_intro.setObjectName(u"deviceName_intro")
        self.deviceName_intro.setProperty("pixelFontSize", 15)

        self.verticalLayout_3.addWidget(self.deviceName_intro)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.deviceName_label = BodyLabel(deviceInfo)
        self.deviceName_label.setObjectName(u"deviceName_label")
        self.deviceName_label.setProperty("pixelFontSize", 20)

        self.horizontalLayout_2.addWidget(self.deviceName_label)

        self.deviceName_value = BodyLabel(deviceInfo)
        self.deviceName_value.setObjectName(u"deviceName_value")
        self.deviceName_value.setProperty("pixelFontSize", 20)

        self.horizontalLayout_2.addWidget(self.deviceName_value)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(10, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.deviceName_intro_2 = CaptionLabel(deviceInfo)
        self.deviceName_intro_2.setObjectName(u"deviceName_intro_2")
        self.deviceName_intro_2.setProperty("pixelFontSize", 15)

        self.verticalLayout_6.addWidget(self.deviceName_intro_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.resolution_label = BodyLabel(deviceInfo)
        self.resolution_label.setObjectName(u"resolution_label")
        self.resolution_label.setProperty("pixelFontSize", 20)

        self.horizontalLayout_3.addWidget(self.resolution_label)

        self.resolution_value = BodyLabel(deviceInfo)
        self.resolution_value.setObjectName(u"resolution_value")
        self.resolution_value.setProperty("pixelFontSize", 20)

        self.horizontalLayout_3.addWidget(self.resolution_value)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)


        self.retranslateUi(deviceInfo)

        QMetaObject.connectSlotsByName(deviceInfo)
    # setupUi

    def retranslateUi(self, deviceInfo):
        deviceInfo.setWindowTitle(QCoreApplication.translate("deviceInfo", u"Form", None))
        self.protocolVersion_intro.setText(QCoreApplication.translate("deviceInfo", u"ADB protocol version decides the packet format between client and server. By now it has 2 versions:\n"
"01000000 used in Android versions until 8 (Oreo)\n"
"01000001 used in Android versions from 9 (Pie)", None))
        self.protocolVersion_label.setText(QCoreApplication.translate("deviceInfo", u"\u534f\u8bae\u7248\u672c:", None))
        self.protocolVersion_value.setText(QCoreApplication.translate("deviceInfo", u"Body label", None))
        self.productName_intro.setText(QCoreApplication.translate("deviceInfo", u"ro.product.name field in Android Build Props", None))
        self.productName_label.setText(QCoreApplication.translate("deviceInfo", u"\u4ea7\u54c1\u540d\u79f0:", None))
        self.productName_value.setText(QCoreApplication.translate("deviceInfo", u"Body label", None))
        self.modelName_intro.setText(QCoreApplication.translate("deviceInfo", u"ro.product.model field in Android Build Props", None))
        self.modelName_label.setText(QCoreApplication.translate("deviceInfo", u"\u6a21\u578b\u540d\u79f0:", None))
        self.modelName_value.setText(QCoreApplication.translate("deviceInfo", u"Body label", None))
        self.deviceName_intro.setText(QCoreApplication.translate("deviceInfo", u"ro.product.device field in Android Build Props", None))
        self.deviceName_label.setText(QCoreApplication.translate("deviceInfo", u"\u8bbe\u5907\u540d\u79f0:", None))
        self.deviceName_value.setText(QCoreApplication.translate("deviceInfo", u"Body label", None))
        self.deviceName_intro_2.setText(QCoreApplication.translate("deviceInfo", u"ro.product.device field in Android Build Props", None))
        self.resolution_label.setText(QCoreApplication.translate("deviceInfo", u"\u5206\u8fa8\u7387:", None))
        self.resolution_value.setText(QCoreApplication.translate("deviceInfo", u"Body label", None))
    # retranslateUi

