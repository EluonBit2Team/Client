# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'expendgrafdlgDhiLdi.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView
from .resources_rc import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1086, 702)
        self.admin_label_back = QLabel(Dialog)
        self.admin_label_back.setObjectName(u"admin_label_back")
        self.admin_label_back.setGeometry(QRect(0, 0, 1081, 701))
        self.admin_label_back.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.admin_webEn_expendgraf = QWebEngineView(Dialog)
        self.admin_webEn_expendgraf.setObjectName(u"admin_webEn_expendgraf")
        self.admin_webEn_expendgraf.setGeometry(QRect(20, 20, 1041, 661))
        self.admin_webEn_expendgraf.setUrl(QUrl(u"about:blank"))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.admin_label_back.setText("")
    # retranslateUi

