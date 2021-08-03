# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NoticeWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import ico_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(303, 206)
        Dialog.setMinimumSize(QSize(303, 206))
        Dialog.setMaximumSize(QSize(303, 206))
        icon = QIcon()
        icon.addFile(u":/ico/ico/ZzCalcBox.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 9, -1, -1)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFrameShape(QFrame.StyledPanel)
        self.textEdit.setFrameShadow(QFrame.Sunken)
        self.textEdit.setLineWidth(1)
        self.textEdit.setLineWrapMode(QTextEdit.WidgetWidth)
        self.textEdit.setReadOnly(True)
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setCursorWidth(1)

        self.verticalLayout.addWidget(self.textEdit)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u63d0\u793a", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u901a\u77e5", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">        \u8f6f\u4ef6\u4ecd\u5904\u4e8e\u6d4b\u8bd5\u9636\u6bb5\uff0c\u5b58\u5728\u4e00\u5b9a\u6570\u91cf\u7684BUG\uff0c\u4f7f\u7528\u65f6\u8bf7\u8f93\u5165\u6b63\u5e38\u8303\u56f4\u5185\u7684\u6570\u503c\uff0c\u5e76\u6309\u7167\u5e38\u89c4\u6b65\u9aa4\u8fdb\u884c\u64cd\u4f5c\uff0c\u5426\u5219\u5c06\u5bfc\u81f4\u4e0d\u786e\u5b9a\u7684\u7ed3\u679c\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span styl"
                        "e=\" font-size:12pt;\">        \u5982\u9047\u95ee\u9898\u6216\u4e0a\u62a5BUG\uff0c\u8bf7\u8054\u7cfbBilibili@\u659c\u5f71\u91cd\u9633xycy\uff0c\u8c22\u8c22\u5408\u4f5c\u3002</span></p></body></html>", None))
    # retranslateUi

