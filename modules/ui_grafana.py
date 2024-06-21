# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'expendgrafdlgtsgSZo.ui'
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
        Dialog.resize(1086, 702)
        Dialog.setStyleSheet(u"QPushButton#admin_btn_reload {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton#admin_btn_reload:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#admin_btn_reload:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}")
        self.admin_label_back = QLabel(Dialog)
        self.admin_label_back.setObjectName(u"admin_label_back")
        self.admin_label_back.setGeometry(QRect(0, 0, 1081, 701))
        self.admin_label_back.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.admin_webEn_expendgraf = QWebEngineView(Dialog)
        self.admin_webEn_expendgraf.setObjectName(u"admin_webEn_expendgraf")
        self.admin_webEn_expendgraf.setGeometry(QRect(20, 40, 1041, 641))
        self.admin_webEn_expendgraf.setUrl(QUrl(u"about:blank"))
        self.admin_btn_reload = QPushButton(Dialog)
        self.admin_btn_reload.setObjectName(u"admin_btn_reload")
        self.admin_btn_reload.setGeometry(QRect(20, 5, 41, 30))
        self.admin_btn_reload.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-reload.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.admin_label_back.setText("")
        self.admin_btn_reload.setText("")
    # retranslateUi

