# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chatmemberaddtZVePb.ui'
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
        Dialog.resize(640, 480)
        Dialog.setStyleSheet(u"QPushButton#dialog_btn_insert {\n"
"    border-style: solid;\n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#dialog_btn_delete {\n"
"    border-style: solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#dialog_btn_exit {\n"
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
"QPushButton#dialog_btn_send {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton#dialog_btn_send:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#dialog_btn_send:pressed {\n"
""
                        "    background-color: rgba(25, 25, 112, 1);\n"
"}")
        self.dialog_label_back = QLabel(Dialog)
        self.dialog_label_back.setObjectName(u"dialog_label_back")
        self.dialog_label_back.setGeometry(QRect(0, 0, 641, 481))
        self.dialog_label_back.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.dialog_label_titleback = QLabel(Dialog)
        self.dialog_label_titleback.setObjectName(u"dialog_label_titleback")
        self.dialog_label_titleback.setGeometry(QRect(0, 0, 641, 51))
        self.dialog_label_titleback.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 1px solid #3498db;")
        self.dialog_label_title = QLabel(Dialog)
        self.dialog_label_title.setObjectName(u"dialog_label_title")
        self.dialog_label_title.setGeometry(QRect(240, 14, 161, 21))
        self.dialog_label_title.setStyleSheet(u"font: 600 11pt \"Segoe UI Variable Small Semibol\";\n"
"color: rgb(232, 232, 232);")
        self.dialog_label_lefttitle = QLabel(Dialog)
        self.dialog_label_lefttitle.setObjectName(u"dialog_label_lefttitle")
        self.dialog_label_lefttitle.setGeometry(QRect(118, 82, 91, 21))
        self.dialog_label_lefttitle.setStyleSheet(u"font: 600 10pt \"Segoe UI Variable Small Semibol\";\n"
"color: rgb(232, 232, 232);")
        self.dialog_label_righttitle = QLabel(Dialog)
        self.dialog_label_righttitle.setObjectName(u"dialog_label_righttitle")
        self.dialog_label_righttitle.setGeometry(QRect(436, 82, 81, 21))
        self.dialog_label_righttitle.setStyleSheet(u"font: 600 10pt \"Segoe UI Variable Small Semibol\";\n"
"color: rgb(232, 232, 232);")
        self.dialog_btn_send = QPushButton(Dialog)
        self.dialog_btn_send.setObjectName(u"dialog_btn_send")
        self.dialog_btn_send.setGeometry(QRect(516, 434, 75, 24))
        self.dialog_btn_send.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";\n"
"border: 1px solid white;\n"
"color: rgb(232, 232, 232);\n"
"")
        self.dialog_btn_exit = QPushButton(Dialog)
        self.dialog_btn_exit.setObjectName(u"dialog_btn_exit")
        self.dialog_btn_exit.setGeometry(QRect(428, 434, 75, 24))
        self.dialog_btn_exit.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";\n"
"border: 1px solid yellow;\n"
"color: rgb(232, 232, 232);\n"
"")
        self.dialog_btn_insert = QPushButton(Dialog)
        self.dialog_btn_insert.setObjectName(u"dialog_btn_insert")
        self.dialog_btn_insert.setGeometry(QRect(310, 170, 21, 24))
        self.dialog_btn_insert.setStyleSheet(u"background-image: url(:/images/images/images/right.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.dialog_btn_delete = QPushButton(Dialog)
        self.dialog_btn_delete.setObjectName(u"dialog_btn_delete")
        self.dialog_btn_delete.setGeometry(QRect(310, 220, 21, 24))
        self.dialog_btn_delete.setStyleSheet(u"background-image: url(:/images/images/images/left.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.dialog_treeview_left = QTreeView(Dialog)
        self.dialog_treeview_left.setObjectName(u"dialog_treeview_left")
        self.dialog_treeview_left.setGeometry(QRect(50, 110, 231, 301))
        self.dialog_treeview_left.setStyleSheet(u"background-color: rgb(40, 44, 52);\n"
"border-radius: 10px;\n"
"font: 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.dialog_treeview_right = QTreeView(Dialog)
        self.dialog_treeview_right.setObjectName(u"dialog_treeview_right")
        self.dialog_treeview_right.setGeometry(QRect(370, 110, 231, 301))
        self.dialog_treeview_right.setStyleSheet(u"background-color: rgb(40, 44, 52);\n"
"border-radius: 10px;\n"
"font: 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.dialog_label_back.setText("")
        self.dialog_label_titleback.setText("")
        self.dialog_label_title.setText(QCoreApplication.translate("Dialog", u"\u2705\ub300\ud654 \uc0c1\ub300 \ucd08\ub300\ud558\uae30", None))
        self.dialog_label_lefttitle.setText(QCoreApplication.translate("Dialog", u"\uc720\uc800 \uc0c1\ud0dc \ubaa9\ub85d", None))
        self.dialog_label_righttitle.setText(QCoreApplication.translate("Dialog", u"\uc120\ud0dd \ub41c \uc720\uc800", None))
        self.dialog_btn_send.setText(QCoreApplication.translate("Dialog", u"\uc804\uc1a1", None))
        self.dialog_btn_exit.setText(QCoreApplication.translate("Dialog", u"\ub098\uac00\uae30", None))
        self.dialog_btn_insert.setText("")
        self.dialog_btn_delete.setText("")
    # retranslateUi

