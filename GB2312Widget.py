# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GB2312Widget.ui'
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
        self.gridLayout = QGridLayout(self.tab_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tab1_btn_calc = QPushButton(self.tab_1)
        self.tab1_btn_calc.setObjectName(u"tab1_btn_calc")

        self.gridLayout.addWidget(self.tab1_btn_calc, 3, 0, 1, 2)

        self.tab1_spin_num = QSpinBox(self.tab_1)
        self.tab1_spin_num.setObjectName(u"tab1_spin_num")
        self.tab1_spin_num.setMaximum(65535)
        self.tab1_spin_num.setDisplayIntegerBase(16)

        self.gridLayout.addWidget(self.tab1_spin_num, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 2)

        self.label_6 = QLabel(self.tab_1)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.tab1_lineEdit_result = QLineEdit(self.tab_1)
        self.tab1_lineEdit_result.setObjectName(u"tab1_lineEdit_result")
        self.tab1_lineEdit_result.setFrame(False)
        self.tab1_lineEdit_result.setReadOnly(True)

        self.gridLayout.addWidget(self.tab1_lineEdit_result, 0, 1, 1, 1)

        self.label_5 = QLabel(self.tab_1)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tab2_spin_num = QSpinBox(self.tab_2)
        self.tab2_spin_num.setObjectName(u"tab2_spin_num")
        self.tab2_spin_num.setMaximum(9999)
        self.tab2_spin_num.setDisplayIntegerBase(10)

        self.gridLayout_2.addWidget(self.tab2_spin_num, 1, 1, 1, 1)

        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 0, 1, 2)

        self.tab2_lineEdit_result = QLineEdit(self.tab_2)
        self.tab2_lineEdit_result.setObjectName(u"tab2_lineEdit_result")
        self.tab2_lineEdit_result.setFrame(False)
        self.tab2_lineEdit_result.setReadOnly(True)

        self.gridLayout_2.addWidget(self.tab2_lineEdit_result, 0, 1, 1, 1)

        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.tab2_btn_calc = QPushButton(self.tab_2)
        self.tab2_btn_calc.setObjectName(u"tab2_btn_calc")

        self.gridLayout_2.addWidget(self.tab2_btn_calc, 3, 0, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)

        self.tab3_lineEdit_result = QLineEdit(self.tab_3)
        self.tab3_lineEdit_result.setObjectName(u"tab3_lineEdit_result")
        self.tab3_lineEdit_result.setFrame(False)
        self.tab3_lineEdit_result.setReadOnly(True)

        self.gridLayout_4.addWidget(self.tab3_lineEdit_result, 0, 1, 1, 1)

        self.tab3_spin_num = QSpinBox(self.tab_3)
        self.tab3_spin_num.setObjectName(u"tab3_spin_num")
        self.tab3_spin_num.setMaximum(9999)
        self.tab3_spin_num.setDisplayIntegerBase(10)

        self.gridLayout_4.addWidget(self.tab3_spin_num, 1, 1, 1, 1)

        self.tab3_btn_calc = QPushButton(self.tab_3)
        self.tab3_btn_calc.setObjectName(u"tab3_btn_calc")

        self.gridLayout_4.addWidget(self.tab3_btn_calc, 3, 0, 1, 2)

        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 2, 0, 1, 2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_5 = QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(self.tab_4)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.tab4_lineEdit_hanzi1 = QLineEdit(self.tab_4)
        self.tab4_lineEdit_hanzi1.setObjectName(u"tab4_lineEdit_hanzi1")

        self.gridLayout_5.addWidget(self.tab4_lineEdit_hanzi1, 1, 1, 1, 1)

        self.tab4_btn_calc = QPushButton(self.tab_4)
        self.tab4_btn_calc.setObjectName(u"tab4_btn_calc")

        self.gridLayout_5.addWidget(self.tab4_btn_calc, 4, 0, 1, 2)

        self.tab4_lineEdit_result = QLineEdit(self.tab_4)
        self.tab4_lineEdit_result.setObjectName(u"tab4_lineEdit_result")
        self.tab4_lineEdit_result.setFrame(False)
        self.tab4_lineEdit_result.setReadOnly(True)

        self.gridLayout_5.addWidget(self.tab4_lineEdit_result, 0, 1, 1, 1)

        self.label_3 = QLabel(self.tab_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.tab4_lineEdit_hanzi2 = QLineEdit(self.tab_4)
        self.tab4_lineEdit_hanzi2.setObjectName(u"tab4_lineEdit_hanzi2")

        self.gridLayout_5.addWidget(self.tab4_lineEdit_hanzi2, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 3, 0, 1, 2)

        self.label_2 = QLabel(self.tab_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)
        self.tab1_btn_calc.clicked.connect(Form.tab1_btn_calc_clicked)
        self.tab2_btn_calc.clicked.connect(Form.tab2_btn_calc_clicked)
        self.tab3_btn_calc.clicked.connect(Form.tab3_btn_calc_clicked)
        self.tab4_btn_calc.clicked.connect(Form.tab4_btn_calc_clicked)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u6c49\u5b57\uff08GB2312\uff09", None))
        self.tab1_btn_calc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u673a\u5185\u7801\uff08HEX\uff09", None))
        self.tab1_lineEdit_result.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u663e\u793a\u8ba1\u7b97\u7ed3\u679c", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u56fd\u6807\u7801\uff08HEX\uff09", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("Form", u"\u56fd\u6807\u7801 \u8f6c \u673a\u5185\u7801", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u56fd\u6807\u7801\uff08HEX\uff09", None))
        self.tab2_lineEdit_result.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u663e\u793a\u8ba1\u7b97\u7ed3\u679c", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u533a\u4f4d\u7801\uff08DEC\uff09", None))
        self.tab2_btn_calc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u533a\u4f4d\u7801 \u8f6c \u56fd\u6807\u7801", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u533a\u4f4d\u7801\uff08DEC\uff09", None))
        self.tab3_lineEdit_result.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u663e\u793a\u8ba1\u7b97\u7ed3\u679c", None))
        self.tab3_btn_calc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u673a\u5185\u7801\uff08HEX\uff09", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u533a\u4f4d\u7801 \u8f6c \u673a\u5185\u7801", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6c49\u5b571", None))
        self.tab4_btn_calc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.tab4_lineEdit_result.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u663e\u793a\u8ba1\u7b97\u7ed3\u679c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u7ed3\u679c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6c49\u5b572", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u6c49\u5b57\u6bd4\u8f83", None))
    # retranslateUi

