# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setlogtimedlggnmMOn.ui'
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
        Dialog.resize(429, 270)
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
        self.dialog_label_top_line.setGeometry(QRect(0, 0, 431, 51))
        self.dialog_label_top_line.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 1px solid #3498db;")
        self.dialog_label_title = QLabel(Dialog)
        self.dialog_label_title.setObjectName(u"dialog_label_title")
        self.dialog_label_title.setGeometry(QRect(10, 10, 101, 31))
        self.dialog_label_title.setStyleSheet(u"font: 600 13pt \"Segoe UI Variable Small Semibol\";\n"
"color: rgb(232, 232, 232);")
        self.dialog_label_back = QLabel(Dialog)
        self.dialog_label_back.setObjectName(u"dialog_label_back")
        self.dialog_label_back.setGeometry(QRect(0, 0, 431, 271))
        self.dialog_label_back.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.dialog_btn_exit = QPushButton(Dialog)
        self.dialog_btn_exit.setObjectName(u"dialog_btn_exit")
        self.dialog_btn_exit.setGeometry(QRect(310, 210, 101, 31))
        self.dialog_btn_exit.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";\n"
"border: 1px solid yellow;\n"
"color: rgb(232, 232, 232);\n"
"\n"
"")
        self.dialog_btn_submit = QPushButton(Dialog)
        self.dialog_btn_submit.setObjectName(u"dialog_btn_submit")
        self.dialog_btn_submit.setGeometry(QRect(180, 210, 101, 31))
        self.dialog_btn_submit.setCursor(QCursor(Qt.PointingHandCursor))
        self.dialog_btn_submit.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";\n"
"border: 1px solid white;\n"
"color: rgb(232, 232, 232);\n"
"\n"
"")
        self.dialog_dateEdit_start = QDateEdit(Dialog)
        self.dialog_dateEdit_start.setObjectName(u"dialog_dateEdit_start")
        self.dialog_dateEdit_start.setGeometry(QRect(20, 80, 141, 31))
        self.dialog_dateEdit_end = QDateEdit(Dialog)
        self.dialog_dateEdit_end.setObjectName(u"dialog_dateEdit_end")
        self.dialog_dateEdit_end.setGeometry(QRect(240, 80, 141, 31))
        self.dialog_label_title_2 = QLabel(Dialog)
        self.dialog_label_title_2.setObjectName(u"dialog_label_title_2")
        self.dialog_label_title_2.setGeometry(QRect(170, 80, 31, 31))
        self.dialog_label_title_2.setStyleSheet(u"font: 600 10pt \"Segoe UI Variable Small Semibol\";\n"
"color: rgb(232, 232, 232);")
        self.dialog_label_title_3 = QLabel(Dialog)
        self.dialog_label_title_3.setObjectName(u"dialog_label_title_3")
        self.dialog_label_title_3.setGeometry(QRect(390, 80, 31, 31))
        self.dialog_label_title_3.setStyleSheet(u"font: 600 10pt \"Segoe UI Variable Small Semibol\";\n"
"color: rgb(232, 232, 232);")
        self.dialog_label_back.raise_()
        self.dialog_label_top_line.raise_()
        self.dialog_label_title.raise_()
        self.dialog_btn_exit.raise_()
        self.dialog_btn_submit.raise_()
        self.dialog_dateEdit_start.raise_()
        self.dialog_dateEdit_end.raise_()
        self.dialog_label_title_2.raise_()
        self.dialog_label_title_3.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.dialog_label_top_line.setText("")
        self.dialog_label_title.setText(QCoreApplication.translate("Dialog", u"\uc2dc\uac04 \uc124\uc815", None))
        self.dialog_label_back.setText("")
        self.dialog_btn_exit.setText(QCoreApplication.translate("Dialog", u"\ub098\uac00\uae30", None))
        self.dialog_btn_submit.setText(QCoreApplication.translate("Dialog", u"\uac80\uc0c9", None))
        self.dialog_label_title_2.setText(QCoreApplication.translate("Dialog", u"\ubd80\ud130", None))
        self.dialog_label_title_3.setText(QCoreApplication.translate("Dialog", u"\uae4c\uc9c0", None))
    # retranslateUi

