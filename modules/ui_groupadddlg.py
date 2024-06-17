# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'groupadddlgkDNJju.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .resources_rc import *

class GroupAddDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"QPushButton#dialog_btn_submit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton#dialog_btn_submit:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#dialog_btn_submit:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}")
        self.dialog_label_back = QLabel(Dialog)
        self.dialog_label_back.setObjectName(u"dialog_label_back")
        self.dialog_label_back.setGeometry(QRect(0, 0, 391, 291))
        self.dialog_label_back.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.dialog_label_top_line = QLabel(Dialog)
        self.dialog_label_top_line.setObjectName(u"dialog_label_top_line")
        self.dialog_label_top_line.setGeometry(QRect(0, 0, 391, 41))
        self.dialog_label_top_line.setStyleSheet(u"border-radius: 10px;\n"
"border-bottom: 1px solid #3498db;")
        self.dialog_label_title = QLabel(Dialog)
        self.dialog_label_title.setObjectName(u"dialog_label_title")
        self.dialog_label_title.setGeometry(QRect(140, 10, 131, 21))
        self.dialog_label_title.setStyleSheet(u"font: 600 10pt \"Segoe UI Variable Small Semibol\";\n"
"color: rgb(232, 232, 232);")
        self.dialog_btn_submit = QPushButton(Dialog)
        self.dialog_btn_submit.setObjectName(u"dialog_btn_submit")
        self.dialog_btn_submit.setGeometry(QRect(5, 243, 381, 31))
        self.dialog_btn_submit.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";\n"
"border: 1px solid yellow;\n"
"color: rgb(232, 232, 232);\n"
"\n"
"")
        self.dialog_edit_chattitle = QLineEdit(Dialog)
        self.dialog_edit_chattitle.setObjectName(u"dialog_edit_chattitle")
        self.dialog_edit_chattitle.setGeometry(QRect(30, 130, 331, 31))
        self.dialog_edit_chattitle.setStyleSheet(u"border: none;\n"
"border-bottom: 2px solid #3498db;\n"
"background: transparent;\n"
"color: white;")
        self.dialog_label_chattitle = QLabel(Dialog)
        self.dialog_label_chattitle.setObjectName(u"dialog_label_chattitle")
        self.dialog_label_chattitle.setGeometry(QRect(28, 103, 81, 20))
        self.dialog_label_chattitle.setStyleSheet(u"font: 600 10pt \"Segoe UI Variable Small Semibol\";\n"
"color: rgb(232, 232, 232);")

        self.retranslateUi(Dialog)
        self.dialog_edit_chattitle.returnPressed.connect(self.dialog_btn_submit.click)
        self.dialog_btn_submit.clicked.connect(Dialog.sendGroupReq)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.dialog_label_back.setText("")
        self.dialog_label_top_line.setText("")
        self.dialog_label_title.setText(QCoreApplication.translate("Dialog", u"\u2705 \ucc44\ud305 \uadf8\ub8f9 \ucd94\uac00", None))
        self.dialog_btn_submit.setText(QCoreApplication.translate("Dialog", u"\uc2e0\uccad \ud558\uae30", None))
        self.dialog_label_chattitle.setText(QCoreApplication.translate("Dialog", u"\ucc44\ud305\ubc29 \uc81c\ubaa9", None))
    # retranslateUi
    
    # def sendGroupReq(self, socket):
    #     self.sock = socket
    #     self.msgText = self.main_window.home_lineedit_chatlist_send.text()
    #     self.loginId = "eluon"
    #     self.groupName = "채팅방 1"
    #     try:
    #         msg = {"type": 0,
    #                "id": self.loginId,
    #                "groupname": self.groupName,
    #                "text": self.msgText}
            
    #         packet = jsonParser(msg)
        
    #         if self.sock and msg:
    #             self.sock.sendall(packet)
                
    #         self.main_window.updateMsgDisplay(self.msgText, "sent")
            
    #         return True
    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #         return False
        
        

