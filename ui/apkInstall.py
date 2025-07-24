# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'apkInstall.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QSizePolicy,
    QSpacerItem, QTableWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, PushButton, TableWidget,FluentIcon)

class Ui_apkInstall(object):
    def setupUi(self, apkInstall):
        if not apkInstall.objectName():
            apkInstall.setObjectName(u"apkInstall")
        apkInstall.resize(665, 566)
        self.horizontalLayout_3 = QHBoxLayout(apkInstall)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 40, 10, 10)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.clear_button = PushButton(apkInstall)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setIcon(FluentIcon.DELETE)

        self.horizontalLayout_2.addWidget(self.clear_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.hint_label = BodyLabel(apkInstall)
        self.hint_label.setObjectName(u"hint_label")

        self.horizontalLayout.addWidget(self.hint_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.ApkTableWidget = TableWidget(apkInstall)
        self.ApkTableWidget.setObjectName(u"ApkTableWidget")

        self.verticalLayout.addWidget(self.ApkTableWidget)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(apkInstall)

        QMetaObject.connectSlotsByName(apkInstall)
    # setupUi

    def retranslateUi(self, apkInstall):
        apkInstall.setWindowTitle(QCoreApplication.translate("apkInstall", u"Form", None))
        self.clear_button.setText(QCoreApplication.translate("apkInstall", u"\u6e05\u7a7a", None))
        self.hint_label.setText(QCoreApplication.translate("apkInstall", u"\u8bf7\u5c06\u5b89\u88c5\u5305/\u538b\u7f29\u5305\u62d6\u81f3\u4e0b\u65b9", None))
    # retranslateUi

