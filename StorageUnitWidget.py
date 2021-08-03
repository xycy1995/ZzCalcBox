# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StorageUnitWidget.ui'
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
        Form.resize(300, 100)
        Form.setMinimumSize(QSize(300, 100))
        Form.setMaximumSize(QSize(300, 100))
        icon = QIcon()
        icon.addFile(u":/ico/ico/ZzCalcBox.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_convert_befotr = QLineEdit(Form)
        self.lineEdit_convert_befotr.setObjectName(u"lineEdit_convert_befotr")

        self.gridLayout.addWidget(self.lineEdit_convert_befotr, 0, 1, 1, 1)

        self.combo_convent_before = QComboBox(Form)
        self.combo_convent_before.addItem("")
        self.combo_convent_before.addItem("")
        self.combo_convent_before.addItem("")
        self.combo_convent_before.addItem("")
        self.combo_convent_before.addItem("")
        self.combo_convent_before.addItem("")
        self.combo_convent_before.addItem("")
        self.combo_convent_before.addItem("")
        self.combo_convent_before.addItem("")
        self.combo_convent_before.addItem("")
        self.combo_convent_before.addItem("")
        self.combo_convent_before.addItem("")
        self.combo_convent_before.setObjectName(u"combo_convent_before")

        self.gridLayout.addWidget(self.combo_convent_before, 0, 2, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.btn_convert = QPushButton(Form)
        self.btn_convert.setObjectName(u"btn_convert")

        self.gridLayout.addWidget(self.btn_convert, 2, 0, 1, 3)

        self.combo_convent_after = QComboBox(Form)
        self.combo_convent_after.addItem("")
        self.combo_convent_after.addItem("")
        self.combo_convent_after.addItem("")
        self.combo_convent_after.addItem("")
        self.combo_convent_after.addItem("")
        self.combo_convent_after.addItem("")
        self.combo_convent_after.addItem("")
        self.combo_convent_after.addItem("")
        self.combo_convent_after.addItem("")
        self.combo_convent_after.addItem("")
        self.combo_convent_after.addItem("")
        self.combo_convent_after.addItem("")
        self.combo_convent_after.setObjectName(u"combo_convent_after")

        self.gridLayout.addWidget(self.combo_convent_after, 1, 2, 1, 1)

        self.lineEdit_convert_after = QLineEdit(Form)
        self.lineEdit_convert_after.setObjectName(u"lineEdit_convert_after")
        self.lineEdit_convert_after.setFrame(False)
        self.lineEdit_convert_after.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_convert_after, 1, 1, 1, 1)


        self.retranslateUi(Form)
        self.btn_convert.clicked.connect(Form.btn_convert_clicked)

        self.combo_convent_after.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5b58\u50a8\u5355\u4f4d", None))
        self.combo_convent_before.setItemText(0, QCoreApplication.translate("Form", u"b", None))
        self.combo_convent_before.setItemText(1, QCoreApplication.translate("Form", u"B", None))
        self.combo_convent_before.setItemText(2, QCoreApplication.translate("Form", u"KB", None))
        self.combo_convent_before.setItemText(3, QCoreApplication.translate("Form", u"MB", None))
        self.combo_convent_before.setItemText(4, QCoreApplication.translate("Form", u"GB", None))
        self.combo_convent_before.setItemText(5, QCoreApplication.translate("Form", u"TB", None))
        self.combo_convent_before.setItemText(6, QCoreApplication.translate("Form", u"PB", None))
        self.combo_convent_before.setItemText(7, QCoreApplication.translate("Form", u"EB", None))
        self.combo_convent_before.setItemText(8, QCoreApplication.translate("Form", u"ZB", None))
        self.combo_convent_before.setItemText(9, QCoreApplication.translate("Form", u"YB", None))
        self.combo_convent_before.setItemText(10, QCoreApplication.translate("Form", u"NB", None))
        self.combo_convent_before.setItemText(11, QCoreApplication.translate("Form", u"DB", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362\u540e", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362\u524d", None))
        self.btn_convert.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362", None))
        self.combo_convent_after.setItemText(0, QCoreApplication.translate("Form", u"b", None))
        self.combo_convent_after.setItemText(1, QCoreApplication.translate("Form", u"B", None))
        self.combo_convent_after.setItemText(2, QCoreApplication.translate("Form", u"KB", None))
        self.combo_convent_after.setItemText(3, QCoreApplication.translate("Form", u"MB", None))
        self.combo_convent_after.setItemText(4, QCoreApplication.translate("Form", u"GB", None))
        self.combo_convent_after.setItemText(5, QCoreApplication.translate("Form", u"TB", None))
        self.combo_convent_after.setItemText(6, QCoreApplication.translate("Form", u"PB", None))
        self.combo_convent_after.setItemText(7, QCoreApplication.translate("Form", u"EB", None))
        self.combo_convent_after.setItemText(8, QCoreApplication.translate("Form", u"ZB", None))
        self.combo_convent_after.setItemText(9, QCoreApplication.translate("Form", u"YB", None))
        self.combo_convent_after.setItemText(10, QCoreApplication.translate("Form", u"NB", None))
        self.combo_convent_after.setItemText(11, QCoreApplication.translate("Form", u"DB", None))

        self.lineEdit_convert_after.setInputMask("")
        self.lineEdit_convert_after.setText("")
        self.lineEdit_convert_after.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u663e\u793a\u8ba1\u7b97\u7ed3\u679c", None))
    # retranslateUi

