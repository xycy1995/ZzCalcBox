# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ParityCheckWidget.ui'
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
        Form.resize(280, 180)
        Form.setMinimumSize(QSize(280, 180))
        Form.setMaximumSize(QSize(280, 180))
        icon = QIcon()
        icon.addFile(u":/ico/ico/ZzCalcBox.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.formLayout = QFormLayout(self.tab_1)
        self.formLayout.setObjectName(u"formLayout")
        self.label_6 = QLabel(self.tab_1)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.label_4 = QLabel(self.tab_1)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.tab1_combo_type = QComboBox(self.tab_1)
        self.tab1_combo_type.addItem("")
        self.tab1_combo_type.addItem("")
        self.tab1_combo_type.setObjectName(u"tab1_combo_type")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.tab1_combo_type)

        self.label_5 = QLabel(self.tab_1)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.tab1_spin_num = QSpinBox(self.tab_1)
        self.tab1_spin_num.setObjectName(u"tab1_spin_num")
        self.tab1_spin_num.setMaximum(255)
        self.tab1_spin_num.setDisplayIntegerBase(2)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.tab1_spin_num)

        self.tab1_btn_calc = QPushButton(self.tab_1)
        self.tab1_btn_calc.setObjectName(u"tab1_btn_calc")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.tab1_btn_calc)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.SpanningRole, self.verticalSpacer_3)

        self.tab1_lineEdit_result = QLineEdit(self.tab_1)
        self.tab1_lineEdit_result.setObjectName(u"tab1_lineEdit_result")
        self.tab1_lineEdit_result.setFrame(False)
        self.tab1_lineEdit_result.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.tab1_lineEdit_result)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.formLayout_2 = QFormLayout(self.tab_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.tab2_spin_num = QSpinBox(self.tab_2)
        self.tab2_spin_num.setObjectName(u"tab2_spin_num")
        self.tab2_spin_num.setMaximum(255)
        self.tab2_spin_num.setDisplayIntegerBase(2)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.tab2_spin_num)

        self.tab2_btn_calc = QPushButton(self.tab_2)
        self.tab2_btn_calc.setObjectName(u"tab2_btn_calc")

        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.tab2_btn_calc)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(2, QFormLayout.SpanningRole, self.verticalSpacer_2)

        self.tab2_lineEdit_result = QLineEdit(self.tab_2)
        self.tab2_lineEdit_result.setObjectName(u"tab2_lineEdit_result")
        self.tab2_lineEdit_result.setFrame(False)
        self.tab2_lineEdit_result.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.tab2_lineEdit_result)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.formLayout_3 = QFormLayout(self.tab_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.tab3_spin_num = QSpinBox(self.tab_3)
        self.tab3_spin_num.setObjectName(u"tab3_spin_num")
        self.tab3_spin_num.setMaximum(127)
        self.tab3_spin_num.setDisplayIntegerBase(2)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.tab3_spin_num)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(3, QFormLayout.SpanningRole, self.verticalSpacer)

        self.tab3_btn_calc = QPushButton(self.tab_3)
        self.tab3_btn_calc.setObjectName(u"tab3_btn_calc")

        self.formLayout_3.setWidget(4, QFormLayout.SpanningRole, self.tab3_btn_calc)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.tab3_combo_type = QComboBox(self.tab_3)
        self.tab3_combo_type.addItem("")
        self.tab3_combo_type.addItem("")
        self.tab3_combo_type.setObjectName(u"tab3_combo_type")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.tab3_combo_type)

        self.tab3_lineEdit_result = QLineEdit(self.tab_3)
        self.tab3_lineEdit_result.setObjectName(u"tab3_lineEdit_result")
        self.tab3_lineEdit_result.setFrame(False)
        self.tab3_lineEdit_result.setReadOnly(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.tab3_lineEdit_result)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)
        self.tab1_btn_calc.clicked.connect(Form.tab1_btn_calc_clicked)
        self.tab2_btn_calc.clicked.connect(Form.tab2_btn_calc_clicked)
        self.tab3_btn_calc.clicked.connect(Form.tab3_btn_calc_clicked)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5947\u5076\u6821\u9a8c\u7801", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u7ed3\u679c", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u7c7b\u578b", None))
        self.tab1_combo_type.setItemText(0, QCoreApplication.translate("Form", u"\u5947\u6821\u9a8c", None))
        self.tab1_combo_type.setItemText(1, QCoreApplication.translate("Form", u"\u5076\u6821\u9a8c", None))

        self.label_5.setText(QCoreApplication.translate("Form", u"\u6570\u503c\uff088\u4f4d\uff09", None))
        self.tab1_btn_calc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.tab1_lineEdit_result.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u663e\u793a\u8ba1\u7b97\u7ed3\u679c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("Form", u"\u5224\u65ad\u6b63\u8bef", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u7ed3\u679c", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u6570\u503c\uff088\u4f4d\uff09", None))
        self.tab2_btn_calc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.tab2_lineEdit_result.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u663e\u793a\u8ba1\u7b97\u7ed3\u679c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u5224\u65ad\u7c7b\u578b", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u7ed3\u679c", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u6570\u503c\uff087\u4f4d\uff09", None))
        self.tab3_btn_calc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7c7b\u578b", None))
        self.tab3_combo_type.setItemText(0, QCoreApplication.translate("Form", u"\u5947\u6821\u9a8c", None))
        self.tab3_combo_type.setItemText(1, QCoreApplication.translate("Form", u"\u5076\u6821\u9a8c", None))

        self.tab3_lineEdit_result.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u663e\u793a\u8ba1\u7b97\u7ed3\u679c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u6c42\u6821\u9a8c\u4f4d", None))
    # retranslateUi

