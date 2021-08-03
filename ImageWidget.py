# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImageWidget.ui'
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
        Form.resize(300, 150)
        Form.setMinimumSize(QSize(300, 150))
        Form.setMaximumSize(QSize(316, 150))
        icon = QIcon()
        icon.addFile(u":/ico/ico/ZzCalcBox.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.spin_pix_h = QSpinBox(Form)
        self.spin_pix_h.setObjectName(u"spin_pix_h")
        self.spin_pix_h.setMaximum(999999999)

        self.gridLayout.addWidget(self.spin_pix_h, 1, 2, 1, 2)

        self.spin_pix_v = QSpinBox(Form)
        self.spin_pix_v.setObjectName(u"spin_pix_v")
        self.spin_pix_v.setMaximum(999999999)

        self.gridLayout.addWidget(self.spin_pix_v, 2, 2, 1, 2)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.lineEdit_size = QLineEdit(Form)
        self.lineEdit_size.setObjectName(u"lineEdit_size")
        self.lineEdit_size.setFrame(False)
        self.lineEdit_size.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_size, 0, 2, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.combo_unit = QComboBox(Form)
        self.combo_unit.addItem("")
        self.combo_unit.addItem("")
        self.combo_unit.addItem("")
        self.combo_unit.addItem("")
        self.combo_unit.addItem("")
        self.combo_unit.addItem("")
        self.combo_unit.setObjectName(u"combo_unit")

        self.gridLayout.addWidget(self.combo_unit, 0, 3, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.btn_calc = QPushButton(Form)
        self.btn_calc.setObjectName(u"btn_calc")

        self.gridLayout.addWidget(self.btn_calc, 4, 0, 1, 4)

        self.spin_depth = QSpinBox(Form)
        self.spin_depth.setObjectName(u"spin_depth")
        self.spin_depth.setMaximum(999)

        self.gridLayout.addWidget(self.spin_depth, 3, 2, 1, 2)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 3, 1, 1, 1)


        self.retranslateUi(Form)
        self.btn_calc.clicked.connect(Form.btn_calc_clicked)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u56fe\u7247", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u5bb9\u91cf", None))
        self.lineEdit_size.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u663e\u793a\u8ba1\u7b97\u7ed3\u679c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5782\u76f4\u50cf\u7d20", None))
        self.combo_unit.setItemText(0, QCoreApplication.translate("Form", u"b", None))
        self.combo_unit.setItemText(1, QCoreApplication.translate("Form", u"B", None))
        self.combo_unit.setItemText(2, QCoreApplication.translate("Form", u"KB", None))
        self.combo_unit.setItemText(3, QCoreApplication.translate("Form", u"MB", None))
        self.combo_unit.setItemText(4, QCoreApplication.translate("Form", u"GB", None))
        self.combo_unit.setItemText(5, QCoreApplication.translate("Form", u"TB", None))

        self.label.setText(QCoreApplication.translate("Form", u"\u6c34\u5e73\u50cf\u7d20", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u989c\u8272\u6df1\u5ea6", None))
        self.btn_calc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
    # retranslateUi

