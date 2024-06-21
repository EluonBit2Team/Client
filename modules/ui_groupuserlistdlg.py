# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'groupuserlistdlgJvpDDb.ui'
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
        Dialog.resize(640, 479)
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
"}")
        self.dialog_label_titleback = QLabel(Dialog)
        self.dialog_label_titleback.setObjectName(u"dialog_label_titleback")
        self.dialog_label_titleback.setGeometry(QRect(0, 0, 641, 481))
        self.dialog_label_titleback.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.dialog_label_title = QLabel(Dialog)
        self.dialog_label_title.setObjectName(u"dialog_label_title")
        self.dialog_label_title.setGeometry(QRect(236, 19, 141, 16))
        self.dialog_label_title.setStyleSheet(u"font: 600 11pt \"Segoe UI Variable Small Semibol\";\n"
"color: rgb(232, 232, 232);")
        self.dialog_label_top_line = QLabel(Dialog)
        self.dialog_label_top_line.setObjectName(u"dialog_label_top_line")
        self.dialog_label_top_line.setGeometry(QRect(0, 0, 641, 51))
        self.dialog_label_top_line.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 1px solid #3498db;")
        self.dialog_treeview_user = QTreeView(Dialog)
        self.dialog_treeview_user.setObjectName(u"dialog_treeview_user")
        self.dialog_treeview_user.setGeometry(QRect(-2, 52, 641, 371))
        self.dialog_treeview_user.setStyleSheet(u"background-color: rgb(31, 35, 41);\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"color: rgb(231, 231, 231);\n"
"font: 600 15pt \"Segoe UI Variable Small Semibol\";")
        self.dialog_btn_exit = QPushButton(Dialog)
        self.dialog_btn_exit.setObjectName(u"dialog_btn_exit")
        self.dialog_btn_exit.setGeometry(QRect(524, 433, 101, 31))
        self.dialog_btn_exit.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";\n"
"border: 1px solid yellow;\n"
"color: rgb(232, 232, 232);\n"
"\n"
"")
        self.dialog_label_titleback.raise_()
        self.dialog_label_top_line.raise_()
        self.dialog_label_title.raise_()
        self.dialog_treeview_user.raise_()
        self.dialog_btn_exit.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.dialog_label_titleback.setText("")
        self.dialog_label_title.setText(QCoreApplication.translate("Dialog", u"\u2705 \ucc44\ud305\ubc29 \ub300\ud654 \uc0c1\ub300", None))
        self.dialog_label_top_line.setText("")
        self.dialog_btn_exit.setText(QCoreApplication.translate("Dialog", u"\ub098\uac00\uae30", None))
    # retranslateUi

