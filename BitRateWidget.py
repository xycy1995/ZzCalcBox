# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BitRateWidget.ui'
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
        Form.resize(260, 100)
        Form.setMinimumSize(QSize(260, 100))
        Form.setMaximumSize(QSize(260, 100))
        icon = QIcon()
        icon.addFile(u":/ico/ico/ZzCalcBox.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.combo_convert_before = QComboBox(Form)
        self.combo_convert_before.addItem("")
        self.combo_convert_before.addItem("")
        self.combo_convert_before.addItem("")
        self.combo_convert_before.addItem("")
        self.combo_convert_before.setObjectName(u"combo_convert_before")

        self.gridLayout.addWidget(self.combo_convert_before, 0, 2, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_convert_after = QLineEdit(Form)
        self.lineEdit_convert_after.setObjectName(u"lineEdit_convert_after")
        self.lineEdit_convert_after.setFrame(False)
        self.lineEdit_convert_after.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_convert_after, 1, 1, 1, 1)

        self.combo_convert_after = QComboBox(Form)
        self.combo_convert_after.addItem("")
        self.combo_convert_after.addItem("")
        self.combo_convert_after.addItem("")
        self.combo_convert_after.addItem("")
        self.combo_convert_after.setObjectName(u"combo_convert_after")

        self.gridLayout.addWidget(self.combo_convert_after, 1, 2, 1, 1)

        self.spin_convert_before = QSpinBox(Form)
        self.spin_convert_before.setObjectName(u"spin_convert_before")
        self.spin_convert_before.setMaximum(999999999)

        self.gridLayout.addWidget(self.spin_convert_before, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.btn_calc = QPushButton(Form)
        self.btn_calc.setObjectName(u"btn_calc")

        self.verticalLayout.addWidget(self.btn_calc)


        self.retranslateUi(Form)
        self.btn_calc.clicked.connect(Form.btn_calc_clicked)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u4f20\u8f93\u901f\u7387", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362\u524d", None))
        self.combo_convert_before.setItemText(0, QCoreApplication.translate("Form", u"bps", None))
        self.combo_convert_before.setItemText(1, QCoreApplication.translate("Form", u"Kbps", None))
        self.combo_convert_before.setItemText(2, QCoreApplication.translate("Form", u"Mbps", None))
        self.combo_convert_before.setItemText(3, QCoreApplication.translate("Form", u"Gbps", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362\u540e", None))
        self.lineEdit_convert_after.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u663e\u793a\u8ba1\u7b97\u7ed3\u679c", None))
        self.combo_convert_after.setItemText(0, QCoreApplication.translate("Form", u"B/s", None))
        self.combo_convert_after.setItemText(1, QCoreApplication.translate("Form", u"KB/s", None))
        self.combo_convert_after.setItemText(2, QCoreApplication.translate("Form", u"MB/s", None))
        self.combo_convert_after.setItemText(3, QCoreApplication.translate("Form", u"GB/s", None))

        self.btn_calc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
    # retranslateUi

