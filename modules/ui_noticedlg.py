# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noticedlgasdzco.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .resources_rc import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)
        Dialog.setStyleSheet(u"QPushButton#dialog_btn_exit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton#dialog_btn_exit:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#dialog_btn_exit:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}\n"
"\n"
"QPushButton#dialog_btn_reset {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton#dialog_btn_reset:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#dialog_btn_reset:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}")
        self.dialog_label_top_line = QLabel(Dialog)
        self.dialog_label_top_line.setObjectName(u"dialog_label_top_line")
        self.dialog_label_top_line.setGeometry(QRect(0, 0, 641, 51))
        self.dialog_label_top_line.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 1px solid #3498db;")
        self.dialog_label_title = QLabel(Dialog)
        self.dialog_label_title.setObjectName(u"dialog_label_title")
        self.dialog_label_title.setGeometry(QRect(279, 14, 81, 31))
        self.dialog_label_title.setStyleSheet(u"font: 600 13pt \"Segoe UI Variable Small Semibol\";\n"
"color: rgb(232, 232, 232);")
        self.dialog_label_back = QLabel(Dialog)
        self.dialog_label_back.setObjectName(u"dialog_label_back")
        self.dialog_label_back.setGeometry(QRect(0, 10, 641, 471))
        self.dialog_label_back.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.dialog_btn_exit = QPushButton(Dialog)
        self.dialog_btn_exit.setObjectName(u"dialog_btn_exit")
        self.dialog_btn_exit.setGeometry(QRect(534, 430, 101, 31))
        self.dialog_btn_exit.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";\n"
"border: 1px solid yellow;\n"
"color: rgb(232, 232, 232);\n"
"\n"
"")
        self.dialog_listview_notice = QListView(Dialog)
        self.dialog_listview_notice.setObjectName(u"dialog_listview_notice")
        self.dialog_listview_notice.setGeometry(QRect(0, 57, 641, 361))
        self.dialog_listview_notice.setStyleSheet(u"background-color: rgb(31, 35, 41);\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"color: rgb(231, 231, 231);\n"
"font: 600 15pt \"Segoe UI Variable Small Semibol\";")
        self.dialog_btn_reset = QPushButton(Dialog)
        self.dialog_btn_reset.setObjectName(u"dialog_btn_reset")
        self.dialog_btn_reset.setGeometry(QRect(424, 430, 101, 31))
        self.dialog_btn_reset.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";\n"
"border: 1px solid white;\n"
"color: rgb(232, 232, 232);\n"
"\n"
"")
        self.dialog_label_back.raise_()
        self.dialog_label_top_line.raise_()
        self.dialog_label_title.raise_()
        self.dialog_btn_exit.raise_()
        self.dialog_listview_notice.raise_()
        self.dialog_btn_reset.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.dialog_label_top_line.setText("")
        self.dialog_label_title.setText(QCoreApplication.translate("Dialog", u"\u2728\uc54c\ub9bc\u2728", None))
        self.dialog_label_back.setText("")
        self.dialog_btn_exit.setText(QCoreApplication.translate("Dialog", u"\ub098\uac00\uae30", None))
        self.dialog_btn_reset.setText(QCoreApplication.translate("Dialog", u"\ucd08\uae30\ud654", None))
    # retranslateUi

