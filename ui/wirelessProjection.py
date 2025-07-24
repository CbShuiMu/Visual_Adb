# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wirelessProjection.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (InfoBadge, PushButton)

class Ui_wirelessProjection(object):
    def setupUi(self, wirelessProjection):
        if not wirelessProjection.objectName():
            wirelessProjection.setObjectName(u"wirelessProjection")
        wirelessProjection.resize(665, 566)
        self.horizontalLayout_5 = QHBoxLayout(wirelessProjection)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 40, 10, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.connect_button = PushButton(wirelessProjection)
        self.connect_button.setObjectName(u"connect_button")

        self.horizontalLayout.addWidget(self.connect_button)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.stop_button = PushButton(wirelessProjection)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.stop_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.InfoBadge = InfoBadge(wirelessProjection)
        self.InfoBadge.setObjectName(u"InfoBadge")

        self.horizontalLayout_3.addWidget(self.InfoBadge)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_11)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.video = QLabel(wirelessProjection)
        self.video.setObjectName(u"video")
        self.video.setMinimumSize(QSize(600, 350))
        self.video.setLayoutDirection(Qt.LeftToRight)
        self.video.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.video)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.back_button = PushButton(wirelessProjection)
        self.back_button.setObjectName(u"back_button")

        self.horizontalLayout_2.addWidget(self.back_button)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.home_button = PushButton(wirelessProjection)
        self.home_button.setObjectName(u"home_button")

        self.horizontalLayout_2.addWidget(self.home_button)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.recent_button = PushButton(wirelessProjection)
        self.recent_button.setObjectName(u"recent_button")

        self.horizontalLayout_2.addWidget(self.recent_button)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout)


        self.retranslateUi(wirelessProjection)

        QMetaObject.connectSlotsByName(wirelessProjection)
    # setupUi

    def retranslateUi(self, wirelessProjection):
        wirelessProjection.setWindowTitle(QCoreApplication.translate("wirelessProjection", u"Form", None))
        self.connect_button.setText(QCoreApplication.translate("wirelessProjection", u"\u8fde\u63a5", None))
        self.stop_button.setText(QCoreApplication.translate("wirelessProjection", u"\u7ed3\u675f", None))
        self.InfoBadge.setText(QCoreApplication.translate("wirelessProjection", u"\u672a\u8fde\u63a5", None))
        self.video.setText(QCoreApplication.translate("wirelessProjection", u"\u8bbe\u5907\u5c4f\u5e55\u4fe1\u606f\u52a0\u8f7d......", None))
        self.back_button.setText(QCoreApplication.translate("wirelessProjection", u"BACK", None))
        self.home_button.setText(QCoreApplication.translate("wirelessProjection", u"HOME", None))
        self.recent_button.setText(QCoreApplication.translate("wirelessProjection", u"RECENT", None))
    # retranslateUi

