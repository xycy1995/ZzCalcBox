# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MemoryAddressWidget.ui'
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
        Form.resize(300, 200)
        Form.setMinimumSize(QSize(300, 200))
        Form.setMaximumSize(QSize(300, 200))
        icon = QIcon()
        icon.addFile(u":/ico/ico/ZzCalcBox.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout = QGridLayout(self.tab_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tab1_spin_bus = QSpinBox(self.tab_1)
        self.tab1_spin_bus.setObjectName(u"tab1_spin_bus")
        self.tab1_spin_bus.setMaximum(999)

        self.gridLayout.addWidget(self.tab1_spin_bus, 1, 1, 1, 1)

        self.label_2 = QLabel(self.tab_1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label = QLabel(self.tab_1)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.tab1_combo_unit = QComboBox(self.tab_1)
        self.tab1_combo_unit.addItem("")
        self.tab1_combo_unit.addItem("")
        self.tab1_combo_unit.addItem("")
        self.tab1_combo_unit.addItem("")
        self.tab1_combo_unit.addItem("")
        self.tab1_combo_unit.addItem("")
        self.tab1_combo_unit.setObjectName(u"tab1_combo_unit")

        self.gridLayout.addWidget(self.tab1_combo_unit, 0, 2, 1, 1)

        self.tab1_btn_calc = QPushButton(self.tab_1)
        self.tab1_btn_calc.setObjectName(u"tab1_btn_calc")

        self.gridLayout.addWidget(self.tab1_btn_calc, 2, 0, 1, 3)

        self.tab1_lineEdit_memory = QLineEdit(self.tab_1)
        self.tab1_lineEdit_memory.setObjectName(u"tab1_lineEdit_memory")
        self.tab1_lineEdit_memory.setFrame(False)
        self.tab1_lineEdit_memory.setReadOnly(True)

        self.gridLayout.addWidget(self.tab1_lineEdit_memory, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tab2_combo_unit = QComboBox(self.tab_2)
        self.tab2_combo_unit.addItem("")
        self.tab2_combo_unit.addItem("")
        self.tab2_combo_unit.addItem("")
        self.tab2_combo_unit.addItem("")
        self.tab2_combo_unit.addItem("")
        self.tab2_combo_unit.addItem("")
        self.tab2_combo_unit.setObjectName(u"tab2_combo_unit")

        self.gridLayout_3.addWidget(self.tab2_combo_unit, 0, 2, 1, 1)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)

        self.tab2_lineEdit_memory = QLineEdit(self.tab_2)
        self.tab2_lineEdit_memory.setObjectName(u"tab2_lineEdit_memory")
        self.tab2_lineEdit_memory.setFrame(False)
        self.tab2_lineEdit_memory.setReadOnly(True)

        self.gridLayout_3.addWidget(self.tab2_lineEdit_memory, 0, 1, 1, 1)

        self.tab2_btn_calc = QPushButton(self.tab_2)
        self.tab2_btn_calc.setObjectName(u"tab2_btn_calc")

        self.gridLayout_3.addWidget(self.tab2_btn_calc, 6, 0, 1, 3)

        self.tab2_spin_start = QSpinBox(self.tab_2)
        self.tab2_spin_start.setObjectName(u"tab2_spin_start")
        self.tab2_spin_start.setMaximum(65535)
        self.tab2_spin_start.setDisplayIntegerBase(16)

        self.gridLayout_3.addWidget(self.tab2_spin_start, 2, 1, 1, 1)

        self.tab2_spin_end = QSpinBox(self.tab_2)
        self.tab2_spin_end.setObjectName(u"tab2_spin_end")
        self.tab2_spin_end.setMaximum(65535)
        self.tab2_spin_end.setDisplayIntegerBase(16)

        self.gridLayout_3.addWidget(self.tab2_spin_end, 4, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1)

        self.tab3_lineEdit_end = QLineEdit(self.tab_3)
        self.tab3_lineEdit_end.setObjectName(u"tab3_lineEdit_end")
        self.tab3_lineEdit_end.setFrame(False)
        self.tab3_lineEdit_end.setReadOnly(True)

        self.gridLayout_5.addWidget(self.tab3_lineEdit_end, 3, 1, 1, 1)

        self.tab3_btn_calc = QPushButton(self.tab_3)
        self.tab3_btn_calc.setObjectName(u"tab3_btn_calc")

        self.gridLayout_5.addWidget(self.tab3_btn_calc, 4, 0, 1, 3)

        self.tab3_lineEdit_memory = QLineEdit(self.tab_3)
        self.tab3_lineEdit_memory.setObjectName(u"tab3_lineEdit_memory")

        self.gridLayout_5.addWidget(self.tab3_lineEdit_memory, 0, 1, 1, 1)

        self.tab3_combo_unit = QComboBox(self.tab_3)
        self.tab3_combo_unit.addItem("")
        self.tab3_combo_unit.addItem("")
        self.tab3_combo_unit.addItem("")
        self.tab3_combo_unit.addItem("")
        self.tab3_combo_unit.addItem("")
        self.tab3_combo_unit.addItem("")
        self.tab3_combo_unit.setObjectName(u"tab3_combo_unit")

        self.gridLayout_5.addWidget(self.tab3_combo_unit, 0, 2, 1, 1)

        self.label_11 = QLabel(self.tab_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_12 = QLabel(self.tab_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 3, 0, 1, 1)

        self.tab3_spin_start = QSpinBox(self.tab_3)
        self.tab3_spin_start.setObjectName(u"tab3_spin_start")
        self.tab3_spin_start.setMaximum(65535)
        self.tab3_spin_start.setDisplayIntegerBase(16)

        self.gridLayout_5.addWidget(self.tab3_spin_start, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_6 = QGridLayout(self.tab_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tab4_lineEdit_memory = QLineEdit(self.tab_4)
        self.tab4_lineEdit_memory.setObjectName(u"tab4_lineEdit_memory")

        self.gridLayout_6.addWidget(self.tab4_lineEdit_memory, 0, 1, 1, 1)

        self.label_15 = QLabel(self.tab_4)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_6.addWidget(self.label_15, 1, 0, 1, 1)

        self.label_16 = QLabel(self.tab_4)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 0, 0, 1, 1)

        self.tab4_btn_calc = QPushButton(self.tab_4)
        self.tab4_btn_calc.setObjectName(u"tab4_btn_calc")

        self.gridLayout_6.addWidget(self.tab4_btn_calc, 4, 0, 1, 3)

        self.label_14 = QLabel(self.tab_4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 2, 0, 1, 1)

        self.tab4_combo_unit = QComboBox(self.tab_4)
        self.tab4_combo_unit.addItem("")
        self.tab4_combo_unit.addItem("")
        self.tab4_combo_unit.addItem("")
        self.tab4_combo_unit.addItem("")
        self.tab4_combo_unit.addItem("")
        self.tab4_combo_unit.addItem("")
        self.tab4_combo_unit.setObjectName(u"tab4_combo_unit")

        self.gridLayout_6.addWidget(self.tab4_combo_unit, 0, 2, 1, 1)

        self.tab4_lineEdit_start = QLineEdit(self.tab_4)
        self.tab4_lineEdit_start.setObjectName(u"tab4_lineEdit_start")
        self.tab4_lineEdit_start.setFrame(False)
        self.tab4_lineEdit_start.setReadOnly(True)

        self.gridLayout_6.addWidget(self.tab4_lineEdit_start, 1, 1, 1, 1)

        self.tab4_spin_end = QSpinBox(self.tab_4)
        self.tab4_spin_end.setObjectName(u"tab4_spin_end")
        self.tab4_spin_end.setMaximum(65535)
        self.tab4_spin_end.setDisplayIntegerBase(16)

        self.gridLayout_6.addWidget(self.tab4_spin_end, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)
        self.tab4_btn_calc.clicked.connect(Form.tab4_btn_calc_clicked)
        self.tab1_btn_calc.clicked.connect(Form.tab1_btn_calc_clicked)
        self.tab2_btn_calc.clicked.connect(Form.tab2_btn_calc_clicked)
        self.tab3_btn_calc.clicked.connect(Form.tab3_btn_calc_clicked)

        self.tabWidget.setCurrentIndex(0)
        self.tab1_combo_unit.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5185\u5b58\u5730\u5740", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5185\u5b58\u5bb9\u91cf", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5730\u5740\u7ebf\u6570\u91cf", None))
        self.tab1_combo_unit.setItemText(0, QCoreApplication.translate("Form", u"b", None))
        self.tab1_combo_unit.setItemText(1, QCoreApplication.translate("Form", u"B", None))
        self.tab1_combo_unit.setItemText(2, QCoreApplication.translate("Form", u"KB", None))
        self.tab1_combo_unit.setItemText(3, QCoreApplication.translate("Form", u"MB", None))
        self.tab1_combo_unit.setItemText(4, QCoreApplication.translate("Form", u"GB", None))
        self.tab1_combo_unit.setItemText(5, QCoreApplication.translate("Form", u"TB", None))

        self.tab1_btn_calc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.tab1_lineEdit_memory.setInputMask("")
        self.tab1_lineEdit_memory.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u663e\u793a\u8ba1\u7b97\u7ed3\u679c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("Form", u"\u5df2\u77e5\u5730\u5740\u7ebf", None))
        self.tab2_combo_unit.setItemText(0, QCoreApplication.translate("Form", u"b", None))
        self.tab2_combo_unit.setItemText(1, QCoreApplication.translate("Form", u"B", None))
        self.tab2_combo_unit.setItemText(2, QCoreApplication.translate("Form", u"KB", None))
        self.tab2_combo_unit.setItemText(3, QCoreApplication.translate("Form", u"MB", None))
        self.tab2_combo_unit.setItemText(4, QCoreApplication.translate("Form", u"GB", None))
        self.tab2_combo_unit.setItemText(5, QCoreApplication.translate("Form", u"TB", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"\u5185\u5b58\u5bb9\u91cf", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u9996\u5730\u5740", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u672b\u5730\u5740", None))
        self.tab2_lineEdit_memory.setInputMask("")
        self.tab2_lineEdit_memory.setText("")
        self.tab2_lineEdit_memory.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u663e\u793a\u8ba1\u7b97\u7ed3\u679c", None))
        self.tab2_btn_calc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u5df2\u77e5\u9996\u672b\u5730\u5740", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u5185\u5b58\u5bb9\u91cf", None))
        self.tab3_lineEdit_end.setInputMask("")
        self.tab3_lineEdit_end.setText("")
        self.tab3_lineEdit_end.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u663e\u793a\u8ba1\u7b97\u7ed3\u679c", None))
        self.tab3_btn_calc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.tab3_combo_unit.setItemText(0, QCoreApplication.translate("Form", u"b", None))
        self.tab3_combo_unit.setItemText(1, QCoreApplication.translate("Form", u"B", None))
        self.tab3_combo_unit.setItemText(2, QCoreApplication.translate("Form", u"KB", None))
        self.tab3_combo_unit.setItemText(3, QCoreApplication.translate("Form", u"MB", None))
        self.tab3_combo_unit.setItemText(4, QCoreApplication.translate("Form", u"GB", None))
        self.tab3_combo_unit.setItemText(5, QCoreApplication.translate("Form", u"TB", None))

        self.label_11.setText(QCoreApplication.translate("Form", u"\u9996\u5730\u5740", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u672b\u5730\u5740", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u5df2\u77e5\u5bb9\u91cf\u548c\u9996\u5730\u5740", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u9996\u5730\u5740", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u5185\u5b58\u5bb9\u91cf", None))
        self.tab4_btn_calc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u672b\u5730\u5740", None))
        self.tab4_combo_unit.setItemText(0, QCoreApplication.translate("Form", u"b", None))
        self.tab4_combo_unit.setItemText(1, QCoreApplication.translate("Form", u"B", None))
        self.tab4_combo_unit.setItemText(2, QCoreApplication.translate("Form", u"KB", None))
        self.tab4_combo_unit.setItemText(3, QCoreApplication.translate("Form", u"MB", None))
        self.tab4_combo_unit.setItemText(4, QCoreApplication.translate("Form", u"GB", None))
        self.tab4_combo_unit.setItemText(5, QCoreApplication.translate("Form", u"TB", None))

        self.tab4_lineEdit_start.setInputMask("")
        self.tab4_lineEdit_start.setText("")
        self.tab4_lineEdit_start.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u663e\u793a\u8ba1\u7b97\u7ed3\u679c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u5df2\u77e5\u5bb9\u91cf\u548c\u672b\u5730\u5740", None))
    # retranslateUi

