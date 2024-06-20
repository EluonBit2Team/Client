# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fooddlgRhjNjR.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView
from . resources_rc import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 482)
        Dialog.setStyleSheet(u"QPushButton#dialog_btn_start {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton#dialog_btn_start:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#dialog_btn_start:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}")
        self.dialog_label_top_line = QLabel(Dialog)
        self.dialog_label_top_line.setObjectName(u"dialog_label_top_line")
        self.dialog_label_top_line.setGeometry(QRect(0, 0, 641, 51))
        self.dialog_label_top_line.setStyleSheet(u"border-radius: 10px;\n"
"border-bottom: 1px solid #3498db;")
        self.dialog_label_title = QLabel(Dialog)
        self.dialog_label_title.setObjectName(u"dialog_label_title")
        self.dialog_label_title.setGeometry(QRect(249, 10, 151, 31))
        self.dialog_label_title.setStyleSheet(u"font: 600 13pt \"Segoe UI Variable Small Semibol\";\n"
"color: rgb(232, 232, 232);")
        self.dialog_label_back = QLabel(Dialog)
        self.dialog_label_back.setObjectName(u"dialog_label_back")
        self.dialog_label_back.setGeometry(QRect(0, 0, 641, 491))
        self.dialog_label_back.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.dialog_btn_start = QPushButton(Dialog)
        self.dialog_btn_start.setObjectName(u"dialog_btn_start")
        self.dialog_btn_start.setGeometry(QRect(4, 433, 631, 31))
        self.dialog_btn_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.dialog_btn_start.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";\n"
"border: 1px solid yellow;\n"
"color: rgb(232, 232, 232);\n"
"\n"
"")
        self.dialog_label_up = QLabel(Dialog)
        self.dialog_label_up.setObjectName(u"dialog_label_up")
        self.dialog_label_up.setGeometry(QRect(290, 370, 61, 51))
        self.dialog_label_up.setStyleSheet(u"background-image: url(:/images/images/images/free-icon-downward-arrow-2268476.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.dialog_label_back.raise_()
        self.dialog_label_top_line.raise_()
        self.dialog_label_title.raise_()
        self.dialog_btn_start.raise_()
        self.dialog_label_up.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.dialog_label_top_line.setText("")
        self.dialog_label_title.setText(QCoreApplication.translate("Dialog", u"\u2728\uc624\ub298\uc758 \uc810\uc2ec\u2728", None))
        self.dialog_label_back.setText("")
        self.dialog_btn_start.setText(QCoreApplication.translate("Dialog", u"\uc2dc\uc791\ud558\uae30", None))
        self.dialog_label_up.setText("")
    # retranslateUi

