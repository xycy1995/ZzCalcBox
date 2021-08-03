# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AsciiWidget.ui'
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
        Form.resize(290, 190)
        Form.setMinimumSize(QSize(290, 190))
        Form.setMaximumSize(QSize(290, 190))
        icon = QIcon()
        icon.addFile(u":/ico/ico/ZzCalcBox.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_4 = QGridLayout(self.tab_1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tab1_btn_calc = QPushButton(self.tab_1)
        self.tab1_btn_calc.setObjectName(u"tab1_btn_calc")

        self.gridLayout_4.addWidget(self.tab1_btn_calc, 3, 0, 1, 3)

        self.tab1_lineEdit_code = QLineEdit(self.tab_1)
        self.tab1_lineEdit_code.setObjectName(u"tab1_lineEdit_code")
        self.tab1_lineEdit_code.setMaxLength(1)

        self.gridLayout_4.addWidget(self.tab1_lineEdit_code, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 2, 0, 1, 3)

        self.tab1_lineEdit_result = QLineEdit(self.tab_1)
        self.tab1_lineEdit_result.setObjectName(u"tab1_lineEdit_result")
        self.tab1_lineEdit_result.setFrame(False)
        self.tab1_lineEdit_result.setReadOnly(True)

        self.gridLayout_4.addWidget(self.tab1_lineEdit_result, 0, 2, 1, 1)

        self.label_10 = QLabel(self.tab_1)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_9 = QLabel(self.tab_1)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.tab2_lineEdit_code2 = QLineEdit(self.tab_2)
        self.tab2_lineEdit_code2.setObjectName(u"tab2_lineEdit_code2")

        self.gridLayout_5.addWidget(self.tab2_lineEdit_code2, 2, 1, 1, 1)

        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 3, 0, 1, 2)

        self.tab2_lineEdit_result = QLineEdit(self.tab_2)
        self.tab2_lineEdit_result.setObjectName(u"tab2_lineEdit_result")
        self.tab2_lineEdit_result.setFrame(False)
        self.tab2_lineEdit_result.setReadOnly(True)

        self.gridLayout_5.addWidget(self.tab2_lineEdit_result, 0, 1, 1, 1)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.tab2_lineEdit_code1 = QLineEdit(self.tab_2)
        self.tab2_lineEdit_code1.setObjectName(u"tab2_lineEdit_code1")

        self.gridLayout_5.addWidget(self.tab2_lineEdit_code1, 1, 1, 1, 1)

        self.tab2_btn_calc = QPushButton(self.tab_2)
        self.tab2_btn_calc.setObjectName(u"tab2_btn_calc")

        self.gridLayout_5.addWidget(self.tab2_btn_calc, 4, 0, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)
        self.tab1_btn_calc.clicked.connect(Form.tab1_btn_calc_clicked)
        self.tab2_btn_calc.clicked.connect(Form.tab2_btn_calc_clicked)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u897f\u6587\uff08ASCII\uff09", None))
        self.tab1_btn_calc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.tab1_lineEdit_result.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u663e\u793a\u8ba1\u7b97\u7ed3\u679c", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u7801\u503c", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u5b57\u7b26", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("Form", u"Ascii\u7801\u503c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u7ed3\u679c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5b57\u7b262", None))
        self.tab2_lineEdit_result.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u663e\u793a\u8ba1\u7b97\u7ed3\u679c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5b57\u7b261", None))
        self.tab2_btn_calc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u5b57\u7b26\u6bd4\u8f83", None))
    # retranslateUi

