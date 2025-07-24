# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fileManager.ui'
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

from qfluentwidgets import (BodyLabel, CaptionLabel, EditableComboBox, LineEdit,
    ProgressBar, PushButton, SearchLineEdit, TableWidget,
    ToolButton,FluentIcon)

class Ui_fileManager(object):
    def setupUi(self, fileManager):
        if not fileManager.objectName():
            fileManager.setObjectName(u"fileManager")
        fileManager.resize(665, 566)
        self.horizontalLayout = QHBoxLayout(fileManager)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(10, -1, -1, -1)
        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 40, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.back_button = ToolButton(fileManager)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setIcon(FluentIcon.RETURN)

        self.horizontalLayout_2.addWidget(self.back_button)

        self.upper_button = ToolButton(fileManager)
        self.upper_button.setObjectName(u"upper_button")
        self.upper_button.setIcon(FluentIcon.UP)

        self.horizontalLayout_2.addWidget(self.upper_button)

        self.innerPath_input = EditableComboBox(fileManager)
        self.innerPath_input.setObjectName(u"innerPath_input")

        self.horizontalLayout_2.addWidget(self.innerPath_input)

        self.refresh_button = ToolButton(fileManager)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setIcon(FluentIcon.SYNC)

        self.horizontalLayout_2.addWidget(self.refresh_button)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(130, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.search_input = SearchLineEdit(fileManager)
        self.search_input.setObjectName(u"search_input")

        self.horizontalLayout_4.addWidget(self.search_input)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.FileTableWidget = TableWidget(fileManager)
        self.FileTableWidget.setObjectName(u"FileTableWidget")

        self.verticalLayout_2.addWidget(self.FileTableWidget)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.number_label = CaptionLabel(fileManager)
        self.number_label.setObjectName(u"number_label")
        self.number_label.setProperty("pixelFontSize", 15)

        self.horizontalLayout_6.addWidget(self.number_label)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.ProgressBar = ProgressBar(fileManager)
        self.ProgressBar.setObjectName(u"ProgressBar")

        self.verticalLayout.addWidget(self.ProgressBar)


        self.horizontalLayout_8.addLayout(self.verticalLayout)

        self.horizontalSpacer_8 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.exPath_label = BodyLabel(fileManager)
        self.exPath_label.setObjectName(u"exPath_label")

        self.horizontalLayout_5.addWidget(self.exPath_label)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.exPath_input = LineEdit(fileManager)
        self.exPath_input.setObjectName(u"exPath_input")

        self.horizontalLayout_5.addWidget(self.exPath_input)

        self.openFile_button = PushButton(fileManager)
        self.openFile_button.setObjectName(u"openFile_button")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openFile_button.sizePolicy().hasHeightForWidth())
        self.openFile_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.openFile_button)

        self.push_button = PushButton(fileManager)
        self.push_button.setObjectName(u"push_button")
        sizePolicy.setHeightForWidth(self.push_button.sizePolicy().hasHeightForWidth())
        self.push_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.push_button)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_9.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)


        self.horizontalLayout.addLayout(self.horizontalLayout_9)


        self.retranslateUi(fileManager)

        QMetaObject.connectSlotsByName(fileManager)
    # setupUi

    def retranslateUi(self, fileManager):
        fileManager.setWindowTitle(QCoreApplication.translate("fileManager", u"Form", None))
        self.number_label.setText(QCoreApplication.translate("fileManager", u"\u6570\u91cf\uff1a0", None))
        self.exPath_label.setText(QCoreApplication.translate("fileManager", u"\u673a\u5916\u8def\u5f84", None))
        self.openFile_button.setText(QCoreApplication.translate("fileManager", u"\u6253\u5f00\u6587\u4ef6", None))
        self.push_button.setText(QCoreApplication.translate("fileManager", u"Push", None))
    # retranslateUi

