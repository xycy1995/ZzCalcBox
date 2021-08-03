# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RadixWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import ico_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(380, 140)
        Form.setMinimumSize(QSize(380, 140))
        Form.setMaximumSize(QSize(380, 140))
        icon = QIcon()
        icon.addFile(u":/ico/ico/ZzCalcBox.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.btn_oct = QPushButton(Form)
        self.btn_oct.setObjectName(u"btn_oct")

        self.gridLayout.addWidget(self.btn_oct, 1, 2, 1, 1)

        self.btn_bin = QPushButton(Form)
        self.btn_bin.setObjectName(u"btn_bin")

        self.gridLayout.addWidget(self.btn_bin, 0, 2, 1, 1)

        self.btn_dec = QPushButton(Form)
        self.btn_dec.setObjectName(u"btn_dec")

        self.gridLayout.addWidget(self.btn_dec, 2, 2, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.btn_hex = QPushButton(Form)
        self.btn_hex.setObjectName(u"btn_hex")

        self.gridLayout.addWidget(self.btn_hex, 3, 2, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_bin = QLineEdit(Form)
        self.lineEdit_bin.setObjectName(u"lineEdit_bin")

        self.gridLayout.addWidget(self.lineEdit_bin, 0, 1, 1, 1)

        self.lineEdit_oct = QLineEdit(Form)
        self.lineEdit_oct.setObjectName(u"lineEdit_oct")

        self.gridLayout.addWidget(self.lineEdit_oct, 1, 1, 1, 1)

        self.lineEdit_dec = QLineEdit(Form)
        self.lineEdit_dec.setObjectName(u"lineEdit_dec")

        self.gridLayout.addWidget(self.lineEdit_dec, 2, 1, 1, 1)

        self.lineEdit_hex = QLineEdit(Form)
        self.lineEdit_hex.setObjectName(u"lineEdit_hex")

        self.gridLayout.addWidget(self.lineEdit_hex, 3, 1, 1, 1)


        self.retranslateUi(Form)
        self.btn_bin.clicked.connect(Form.btn_bin_clicked)
        self.btn_oct.clicked.connect(Form.btn_oct_clicked)
        self.btn_dec.clicked.connect(Form.btn_dec_clicked)
        self.btn_hex.clicked.connect(Form.btn_hex_clicked)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8fdb\u5236", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u516b\u8fdb\u5236\uff08OCT\uff09", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u4e8c\u8fdb\u5236\uff08BIN\uff09", None))
        self.btn_oct.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362", None))
        self.btn_bin.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362", None))
        self.btn_dec.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5341\u516d\u8fdb\u5236\uff08HEX\uff09", None))
        self.btn_hex.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5341\u8fdb\u5236\uff08DEC\uff09", None))
    # retranslateUi

