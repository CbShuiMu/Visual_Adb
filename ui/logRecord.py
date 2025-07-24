# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logRecord.ui'
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

from qfluentwidgets import (LineEdit, PushButton, SearchLineEdit, TableWidget,FluentIcon,TableView)

class Ui_logRecord(object):
    def setupUi(self, logRecord):
        if not logRecord.objectName():
            logRecord.setObjectName(u"logRecord")
        logRecord.resize(665, 566)
        self.horizontalLayout_2 = QHBoxLayout(logRecord)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 40, 10, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start_button = PushButton(logRecord)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMaximumSize(QSize(200, 16777215))
        self.start_button.setIcon(FluentIcon.PLAY)

        self.horizontalLayout.addWidget(self.start_button)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.stop_button = PushButton(logRecord)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setMaximumSize(QSize(200, 16777215))
        self.stop_button.setIcon(FluentIcon.CLOSE)

        self.horizontalLayout.addWidget(self.stop_button)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.save_button = PushButton(logRecord)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setIcon(FluentIcon.SAVE)

        self.horizontalLayout.addWidget(self.save_button)

        self.horizontalSpacer = QSpacerItem(440, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.search_input = SearchLineEdit(logRecord)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setMinimumSize(QSize(230, 33))

        self.horizontalLayout.addWidget(self.search_input)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.LogRecordTableView = TableView(logRecord)
        self.LogRecordTableView.setObjectName(u"LogRecordWidget")
        self.LogRecordTableView.setMinimumSize(QSize(600, 430))

        self.verticalLayout.addWidget(self.LogRecordTableView)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(logRecord)

        QMetaObject.connectSlotsByName(logRecord)
    # setupUi

    def retranslateUi(self, logRecord):
        logRecord.setWindowTitle(QCoreApplication.translate("logRecord", u"Form", None))
        self.start_button.setText(QCoreApplication.translate("logRecord", u"\u5f00\u59cb", None))
        self.stop_button.setText(QCoreApplication.translate("logRecord", u"\u7ed3\u675f", None))
        self.save_button.setText(QCoreApplication.translate("logRecord", u"\u4fdd\u5b58", None))
    # retranslateUi

