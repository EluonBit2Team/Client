# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calldlgDeXGYH.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(638, 471)
        self.dialog_label_back = QLabel(Dialog)
        self.dialog_label_back.setObjectName(u"dialog_label_back")
        self.dialog_label_back.setGeometry(QRect(0, 0, 641, 471))
        self.dialog_label_back.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 70, 581, 71))
        self.label.setStyleSheet(u"border-bottom: 1px solid #FFFFFF;\n"
"border-radius: 0px;")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(460, 80, 151, 31))
        self.label_2.setStyleSheet(u"background-image: url(:/images/images/images/eluonlogo_modified.png);")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(28, 200, 251, 151))
        self.label_3.setStyleSheet(u"\n"
"font: 350 9pt \"Segoe UI Variable Text Semiligh\";\n"
"color: rgb(232, 232, 232);\n"
"background-image: url(:/images/images/images/callimage.png);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.dialog_label_back.setText("")
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
    # retranslateUi

