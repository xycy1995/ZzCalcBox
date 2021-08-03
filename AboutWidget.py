# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import ico_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(275, 200)
        Dialog.setMinimumSize(QSize(275, 200))
        Dialog.setMaximumSize(QSize(275, 200))
        icon = QIcon()
        icon.addFile(u":/ico/ico/ZzCalcBox.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 2)

        self.btn_version = QPushButton(Dialog)
        self.btn_version.setObjectName(u"btn_version")
        self.btn_version.setAcceptDrops(False)
        self.btn_version.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/ico/ico/update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_version.setIcon(icon1)
        self.btn_version.setIconSize(QSize(16, 16))
        self.btn_version.setCheckable(False)
        self.btn_version.setAutoRepeat(False)
        self.btn_version.setAutoExclusive(False)
        self.btn_version.setAutoDefault(True)

        self.gridLayout.addWidget(self.btn_version, 4, 1, 1, 1)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.btn_author = QPushButton(Dialog)
        self.btn_author.setObjectName(u"btn_author")
        icon2 = QIcon()
        icon2.addFile(u":/ico/ico/xycy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_author.setIcon(icon2)
        self.btn_author.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.btn_author, 5, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.btn_license = QPushButton(Dialog)
        self.btn_license.setObjectName(u"btn_license")
        icon3 = QIcon()
        icon3.addFile(u":/ico/ico/gnu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_license.setIcon(icon3)
        self.btn_license.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.btn_license, 6, 1, 1, 1)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 700 9pt \"Microsoft YaHei UI\";")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 2)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(32, 32))
        self.label_3.setPixmap(QPixmap(u":/ico/ico/ZzCalcBox.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 2, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.btn_version.clicked.connect(Dialog.btn_version_clicked)
        self.btn_author.clicked.connect(Dialog.btn_author_clicked)
        self.btn_license.clicked.connect(Dialog.btn_license_clicked)

        self.btn_version.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5173\u4e8e", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"ZzCalcBox", None))
        self.btn_version.setText(QCoreApplication.translate("Dialog", u"1.0.0", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u8bb8\u53ef\u8bc1\uff1a", None))
        self.btn_author.setText(QCoreApplication.translate("Dialog", u"\u659c\u5f71\u91cd\u9633xycy", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u3010\u4e2d\u804c\u8ba1\u7b97\u673a\u4e13\u4e1a\u3011\u8ba1\u7b97\u5de5\u5177\u7bb1", None))
        self.btn_license.setText(QCoreApplication.translate("Dialog", u"GPL 3.0", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u4e00\u6b3e\u65b9\u4fbf\u4e2d\u804c\u5b66\u751f\u5b66\u4e60\u7684\u8ba1\u7b97\u5de5\u5177", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u7248\u672c\uff1a", None))
        self.label_3.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u4f5c\u8005\uff1a", None))
    # retranslateUi

