# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import ico_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 320)
        MainWindow.setMinimumSize(QSize(480, 320))
        MainWindow.setMaximumSize(QSize(480, 320))
        MainWindow.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u":/ico/ico/ZzCalcBox.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_memoryAdress = QPushButton(self.centralwidget)
        self.btn_memoryAdress.setObjectName(u"btn_memoryAdress")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_memoryAdress.sizePolicy().hasHeightForWidth())
        self.btn_memoryAdress.setSizePolicy(sizePolicy)
        self.btn_memoryAdress.setMaximumSize(QSize(128, 128))
        self.btn_memoryAdress.setSizeIncrement(QSize(0, 0))
        self.btn_memoryAdress.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_memoryAdress, 0, 2, 1, 1)

        self.btn_audio = QPushButton(self.centralwidget)
        self.btn_audio.setObjectName(u"btn_audio")
        sizePolicy.setHeightForWidth(self.btn_audio.sizePolicy().hasHeightForWidth())
        self.btn_audio.setSizePolicy(sizePolicy)
        self.btn_audio.setMaximumSize(QSize(128, 128))
        self.btn_audio.setSizeIncrement(QSize(0, 0))
        self.btn_audio.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_audio, 2, 2, 1, 1)

        self.btn_bitRate = QPushButton(self.centralwidget)
        self.btn_bitRate.setObjectName(u"btn_bitRate")
        sizePolicy.setHeightForWidth(self.btn_bitRate.sizePolicy().hasHeightForWidth())
        self.btn_bitRate.setSizePolicy(sizePolicy)
        self.btn_bitRate.setMaximumSize(QSize(128, 128))
        self.btn_bitRate.setSizeIncrement(QSize(0, 0))
        self.btn_bitRate.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_bitRate, 2, 0, 1, 1)

        self.btn_radix = QPushButton(self.centralwidget)
        self.btn_radix.setObjectName(u"btn_radix")
        sizePolicy.setHeightForWidth(self.btn_radix.sizePolicy().hasHeightForWidth())
        self.btn_radix.setSizePolicy(sizePolicy)
        self.btn_radix.setMaximumSize(QSize(128, 128))
        self.btn_radix.setSizeIncrement(QSize(0, 0))
        self.btn_radix.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_radix, 0, 1, 1, 1)

        self.btn_machineDigit = QPushButton(self.centralwidget)
        self.btn_machineDigit.setObjectName(u"btn_machineDigit")
        sizePolicy.setHeightForWidth(self.btn_machineDigit.sizePolicy().hasHeightForWidth())
        self.btn_machineDigit.setSizePolicy(sizePolicy)
        self.btn_machineDigit.setMaximumSize(QSize(128, 128))
        self.btn_machineDigit.setSizeIncrement(QSize(0, 0))
        self.btn_machineDigit.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_machineDigit, 0, 3, 1, 1)

        self.btn_gb2312 = QPushButton(self.centralwidget)
        self.btn_gb2312.setObjectName(u"btn_gb2312")
        sizePolicy.setHeightForWidth(self.btn_gb2312.sizePolicy().hasHeightForWidth())
        self.btn_gb2312.setSizePolicy(sizePolicy)
        self.btn_gb2312.setMaximumSize(QSize(128, 128))
        self.btn_gb2312.setSizeIncrement(QSize(0, 0))
        self.btn_gb2312.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_gb2312, 1, 1, 1, 1)

        self.btn_dotMatrix = QPushButton(self.centralwidget)
        self.btn_dotMatrix.setObjectName(u"btn_dotMatrix")
        sizePolicy.setHeightForWidth(self.btn_dotMatrix.sizePolicy().hasHeightForWidth())
        self.btn_dotMatrix.setSizePolicy(sizePolicy)
        self.btn_dotMatrix.setMaximumSize(QSize(128, 128))
        self.btn_dotMatrix.setSizeIncrement(QSize(0, 0))
        self.btn_dotMatrix.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_dotMatrix, 1, 2, 1, 1)

        self.btn_storageUnit = QPushButton(self.centralwidget)
        self.btn_storageUnit.setObjectName(u"btn_storageUnit")
        sizePolicy.setHeightForWidth(self.btn_storageUnit.sizePolicy().hasHeightForWidth())
        self.btn_storageUnit.setSizePolicy(sizePolicy)
        self.btn_storageUnit.setMaximumSize(QSize(128, 128))
        self.btn_storageUnit.setSizeIncrement(QSize(0, 0))
        self.btn_storageUnit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_storageUnit.setMouseTracking(False)
        self.btn_storageUnit.setAcceptDrops(False)

        self.gridLayout.addWidget(self.btn_storageUnit, 0, 0, 1, 1)

        self.btn_ascii = QPushButton(self.centralwidget)
        self.btn_ascii.setObjectName(u"btn_ascii")
        sizePolicy.setHeightForWidth(self.btn_ascii.sizePolicy().hasHeightForWidth())
        self.btn_ascii.setSizePolicy(sizePolicy)
        self.btn_ascii.setMaximumSize(QSize(128, 128))
        self.btn_ascii.setSizeIncrement(QSize(0, 0))
        self.btn_ascii.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_ascii, 1, 0, 1, 1)

        self.btn_parityCheck = QPushButton(self.centralwidget)
        self.btn_parityCheck.setObjectName(u"btn_parityCheck")
        sizePolicy.setHeightForWidth(self.btn_parityCheck.sizePolicy().hasHeightForWidth())
        self.btn_parityCheck.setSizePolicy(sizePolicy)
        self.btn_parityCheck.setMaximumSize(QSize(128, 128))
        self.btn_parityCheck.setSizeIncrement(QSize(0, 0))
        self.btn_parityCheck.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_parityCheck, 1, 3, 1, 1)

        self.btn_image = QPushButton(self.centralwidget)
        self.btn_image.setObjectName(u"btn_image")
        sizePolicy.setHeightForWidth(self.btn_image.sizePolicy().hasHeightForWidth())
        self.btn_image.setSizePolicy(sizePolicy)
        self.btn_image.setMaximumSize(QSize(128, 128))
        self.btn_image.setSizeIncrement(QSize(0, 0))
        self.btn_image.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_image, 2, 1, 1, 1)

        self.btn_about = QPushButton(self.centralwidget)
        self.btn_about.setObjectName(u"btn_about")
        sizePolicy.setHeightForWidth(self.btn_about.sizePolicy().hasHeightForWidth())
        self.btn_about.setSizePolicy(sizePolicy)
        self.btn_about.setMaximumSize(QSize(128, 128))
        self.btn_about.setSizeIncrement(QSize(0, 0))
        self.btn_about.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_about, 2, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.btn_storageUnit.clicked.connect(MainWindow.btn_storage_unit_clicked)
        self.btn_radix.clicked.connect(MainWindow.btn_radix_clicked)
        self.btn_memoryAdress.clicked.connect(MainWindow.btn_memory_address_clicked)
        self.btn_machineDigit.clicked.connect(MainWindow.btn_machine_digit_clicked)
        self.btn_ascii.clicked.connect(MainWindow.btn_ascii_clicked)
        self.btn_gb2312.clicked.connect(MainWindow.btn_gb2312_clicked)
        self.btn_dotMatrix.clicked.connect(MainWindow.btn_dot_matrix_clicked)
        self.btn_parityCheck.clicked.connect(MainWindow.btn_parity_check_clicked)
        self.btn_bitRate.clicked.connect(MainWindow.btn_bit_rate_clicked)
        self.btn_image.clicked.connect(MainWindow.btn_image_clicked)
        self.btn_audio.clicked.connect(MainWindow.btn_audio_clicked)
        self.btn_about.clicked.connect(MainWindow.btn_about_clicked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u3010\u4e2d\u804c\u8ba1\u7b97\u673a\u4e13\u4e1a\u3011\u8ba1\u7b97\u5de5\u5177\u7bb1 - ZzCalcBox", None))
        self.btn_memoryAdress.setText(QCoreApplication.translate("MainWindow", u"\u5185\u5b58\u5730\u5740", None))
        self.btn_audio.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u9891", None))
        self.btn_bitRate.setText(QCoreApplication.translate("MainWindow", u"\u4f20\u8f93\u901f\u7387", None))
        self.btn_radix.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u5236", None))
        self.btn_machineDigit.setText(QCoreApplication.translate("MainWindow", u"\u539f\u7801/\u53cd\u7801/\u8865\u7801", None))
        self.btn_gb2312.setText(QCoreApplication.translate("MainWindow", u"\u6c49\u5b57\uff08GB2312\uff09", None))
        self.btn_dotMatrix.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u7b26\u70b9\u9635", None))
        self.btn_storageUnit.setText(QCoreApplication.translate("MainWindow", u"\u5b58\u50a8\u5355\u4f4d", None))
        self.btn_ascii.setText(QCoreApplication.translate("MainWindow", u"\u897f\u6587\uff08ASCII\uff09", None))
        self.btn_parityCheck.setText(QCoreApplication.translate("MainWindow", u"\u5947\u5076\u6821\u9a8c\u7801", None))
        self.btn_image.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

