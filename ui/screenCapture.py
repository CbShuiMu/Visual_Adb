# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screenCapture.ui'
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

from qfluentwidgets import (ImageLabel, PushButton, SmoothScrollArea,FluentIcon)

class Ui_screenCapture(object):
    def setupUi(self, screenCapture):
        if not screenCapture.objectName():
            screenCapture.setObjectName(u"screenCapture")
        screenCapture.resize(665, 566)
        self.horizontalLayout_2 = QHBoxLayout(screenCapture)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 40, 10, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.capture_button = PushButton(screenCapture)
        self.capture_button.setObjectName(u"capture_button")
        self.capture_button.setProperty("hasIcon", True)
        self.capture_button.setIcon(FluentIcon.CAMERA)

        self.horizontalLayout.addWidget(self.capture_button)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.save_button = PushButton(screenCapture)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setIcon(FluentIcon.SAVE)

        self.horizontalLayout.addWidget(self.save_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.capturephoto_Area = SmoothScrollArea(screenCapture)
        self.capturephoto_Area.setObjectName(u"capturephoto_Area")
        self.capturephoto_Area.setMinimumSize(QSize(600, 430))
        self.capturephoto_Area.setWidgetResizable(True)
        # self.scrollAreaWidgetContents = QWidget()
        # self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        # self.scrollAreaWidgetContents.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.ImageLabel = ImageLabel(self.capturephoto_Area)
        self.ImageLabel.setObjectName(u"ImageLabel")
        self.ImageLabel.setScaledContents(True)
        self.ImageLabel.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.capturephoto_Area.setWidget(self.ImageLabel)
        self.verticalLayout.addWidget(self.capturephoto_Area)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.retranslateUi(screenCapture)

        QMetaObject.connectSlotsByName(screenCapture)
    # setupUi

    def retranslateUi(self, screenCapture):
        screenCapture.setWindowTitle(QCoreApplication.translate("screenCapture", u"Form", None))
        self.capture_button.setText(QCoreApplication.translate("screenCapture", u"截图", None))
        self.save_button.setText(QCoreApplication.translate("screenCapture", u"保存", None))
    # retranslateUi

