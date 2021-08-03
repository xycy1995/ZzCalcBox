# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MachineDigitWidget.ui'
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
        Form.resize(350, 135)
        Form.setMinimumSize(QSize(350, 135))
        Form.setMaximumSize(QSize(350, 135))
        icon = QIcon()
        icon.addFile(u":/ico/ico/ZzCalcBox.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.spin_truth = QSpinBox(Form)
        self.spin_truth.setObjectName(u"spin_truth")
        self.spin_truth.setMinimum(-128)
        self.spin_truth.setMaximum(127)

        self.gridLayout.addWidget(self.spin_truth, 0, 1, 1, 1)

        self.btn_truth = QPushButton(Form)
        self.btn_truth.setObjectName(u"btn_truth")
        self.btn_truth.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.btn_truth, 0, 2, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.spin_sc = QSpinBox(Form)
        self.spin_sc.setObjectName(u"spin_sc")
        self.spin_sc.setMinimum(0)
        self.spin_sc.setMaximum(255)
        self.spin_sc.setDisplayIntegerBase(2)

        self.gridLayout.addWidget(self.spin_sc, 1, 1, 1, 1)

        self.btn_sc = QPushButton(Form)
        self.btn_sc.setObjectName(u"btn_sc")
        self.btn_sc.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.btn_sc, 1, 2, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.spin_ic = QSpinBox(Form)
        self.spin_ic.setObjectName(u"spin_ic")
        self.spin_ic.setMaximum(255)
        self.spin_ic.setDisplayIntegerBase(2)

        self.gridLayout.addWidget(self.spin_ic, 2, 1, 1, 1)

        self.btn_ic = QPushButton(Form)
        self.btn_ic.setObjectName(u"btn_ic")
        self.btn_ic.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.btn_ic, 2, 2, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.spin_cc = QSpinBox(Form)
        self.spin_cc.setObjectName(u"spin_cc")
        self.spin_cc.setMaximum(255)
        self.spin_cc.setDisplayIntegerBase(2)

        self.gridLayout.addWidget(self.spin_cc, 3, 1, 1, 1)

        self.btn_cc = QPushButton(Form)
        self.btn_cc.setObjectName(u"btn_cc")
        self.btn_cc.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.btn_cc, 3, 2, 1, 1)

        QWidget.setTabOrder(self.btn_truth, self.btn_sc)
        QWidget.setTabOrder(self.btn_sc, self.btn_ic)
        QWidget.setTabOrder(self.btn_ic, self.btn_cc)

        self.retranslateUi(Form)
        self.btn_truth.clicked.connect(Form.btn_truth_clicked)
        self.btn_sc.clicked.connect(Form.btn_sc_clicked)
        self.btn_ic.clicked.connect(Form.btn_ic_clicked)
        self.btn_cc.clicked.connect(Form.btn_cc_clicked)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u539f\u7801/\u53cd\u7801/\u8865\u7801", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u771f\u503c\u6570", None))
        self.btn_truth.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u539f\u7801", None))
        self.btn_sc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u53cd\u7801", None))
        self.btn_ic.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8865\u7801", None))
        self.btn_cc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
    # retranslateUi

