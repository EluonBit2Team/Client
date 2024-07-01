# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainknCLrv.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1085, 700)
        MainWindow.setMinimumSize(QSize(1085, 700))
        MainWindow.setMaximumSize(QSize(1085, 700))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setMaximumSize(QSize(1085, 700))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	backg"
                        "round-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"/*\uc67c\ucabd \ubc84\ud2bc*/\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:p"
                        "ressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/*\uc124\uc815 \ubc84\ud2bc*/\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button \uba54\ub274 \ubc84\ud2bc */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:"
                        "hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141,"
                        " 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none"
                        ";  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
""
                        "}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
""
                        "}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	bord"
                        "er-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-"
                        "bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-l"
                        "eft-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:"
                        "checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	bord"
                        "er: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);"
                        "\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* ////////////////////"
                        "/////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setStyleSheet(u"")
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setStyleSheet(u"")
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 4, 42, 42))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topLogo.sizePolicy().hasHeightForWidth())
        self.topLogo.setSizePolicy(sizePolicy)
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-image: url(:/images/images/images/eluonlogo.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(49, 10, 161, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setStyleSheet(u"background-image: url(:/images/images/images/LUON.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"font-weight: normal;\n"
"height: 42px;")
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-speech.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_admin = QPushButton(self.topMenu)
        self.btn_admin.setObjectName(u"btn_admin")
        sizePolicy1.setHeightForWidth(self.btn_admin.sizePolicy().hasHeightForWidth())
        self.btn_admin.setSizePolicy(sizePolicy1)
        self.btn_admin.setMinimumSize(QSize(0, 45))
        self.btn_admin.setFont(font)
        self.btn_admin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_admin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_admin.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user-female.png);")

        self.verticalLayout_8.addWidget(self.btn_admin)

        self.btn_login = QPushButton(self.topMenu)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy1.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy1)
        self.btn_login.setMinimumSize(QSize(0, 45))
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_login.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-lock-locked.png);")

        self.verticalLayout_8.addWidget(self.btn_login)

        self.btn_notice = QPushButton(self.topMenu)
        self.btn_notice.setObjectName(u"btn_notice")
        sizePolicy1.setHeightForWidth(self.btn_notice.sizePolicy().hasHeightForWidth())
        self.btn_notice.setSizePolicy(sizePolicy1)
        self.btn_notice.setMinimumSize(QSize(0, 45))
        self.btn_notice.setFont(font)
        self.btn_notice.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_notice.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_notice.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-lightbulb.png);")

        self.verticalLayout_8.addWidget(self.btn_notice)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))
        self.extraLabel.setStyleSheet(u"")

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy1.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy1)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy1.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy1)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy1.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy1)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Variable Small Semibol"])
        font2.setPointSize(9)
        font2.setWeight(QFont.DemiBold)
        font2.setItalic(False)
        self.titleRightInfo.setFont(font2)
        self.titleRightInfo.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";")
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;\n"
"\n"
"")
        self.loginpage = QWidget()
        self.loginpage.setObjectName(u"loginpage")
        self.loginpage.setStyleSheet(u"QPushButton#login_btn_login {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton#login_btn_signup {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton#login_btn_mail {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton#login_btn_call {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#login_btn_login {\n"
"   background-color: rgba(70, 130, 180, 0.25);\n"
"}\n"
"\n"
"QPushButton#login_btn_login:hover {\n"
"    background-"
                        "color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#login_btn_login:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}\n"
"\n"
"QPushButton#login_btn_signup {\n"
"    background-color: rgba(255, 105, 180, 0.25);\n"
"}\n"
"\n"
"QPushButton#login_btn_signup:hover {\n"
"    background-color: rgba(255, 105, 180, 1);\n"
"}\n"
"\n"
"QPushButton#login_btn_signup:pressed {\n"
"    background-color: rgba(139, 0, 139, 1);\n"
"}\n"
"\n"
"QPushButton#login_btn_mail {\n"
"    background-color: rgba(70, 130, 180, 0.25);\n"
"}\n"
"\n"
"QPushButton#login_btn_mail:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#login_btn_mail:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}\n"
"\n"
"QPushButton#login_btn_call {\n"
"    background-color: rgba(34, 139, 34, 0.25);\n"
"}\n"
"\n"
"QPushButton#login_btn_call:hover {\n"
"    background-color: rgba(34, 139, 34, 1);\n"
"}\n"
"\n"
"QPushButton#login_btn_call:pressed {\n"
"    background-color: rgba(0, 100, 0, 1);\n"
"}"
                        "\n"
"\n"
"")
        self.verticalLayout_20 = QVBoxLayout(self.loginpage)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWidget(self.loginpage)
        self.widget.setObjectName(u"widget")
        self.login_label_back = QLabel(self.widget)
        self.login_label_back.setObjectName(u"login_label_back")
        self.login_label_back.setGeometry(QRect(10, 10, 941, 541))
        self.login_label_back.setStyleSheet(u"background-image: url(:/images/images/images/loginbackground.jpg);\n"
"border-radius: 20px;\n"
"")
        self.login_label_logo = QLabel(self.widget)
        self.login_label_logo.setObjectName(u"login_label_logo")
        self.login_label_logo.setGeometry(QRect(380, 70, 201, 61))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(28)
        font3.setWeight(QFont.ExtraLight)
        font3.setItalic(False)
        self.login_label_logo.setFont(font3)
        self.login_label_logo.setStyleSheet(u"font: 28pt \"Segoe UI\";\n"
"font-weight: 200;\n"
"color: rgb(255, 255, 255);")
        self.login_input_id = QLineEdit(self.widget)
        self.login_input_id.setObjectName(u"login_input_id")
        self.login_input_id.setGeometry(QRect(240, 180, 491, 41))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        self.login_input_id.setFont(font4)
        self.login_input_id.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255, 255, 255, 120);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;\n"
"font: 12pt \"Segoe UI\";\n"
"border-radius: none;")
        self.login_input_pw = QLineEdit(self.widget)
        self.login_input_pw.setObjectName(u"login_input_pw")
        self.login_input_pw.setGeometry(QRect(240, 240, 491, 41))
        self.login_input_pw.setFont(font4)
        self.login_input_pw.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255, 255, 255, 120);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;\n"
"font: 12pt \"Segoe UI\";\n"
"border-radius: none;")
        self.login_input_pw.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_label_cover = QLabel(self.widget)
        self.login_label_cover.setObjectName(u"login_label_cover")
        self.login_label_cover.setGeometry(QRect(130, 10, 701, 541))
        self.login_label_cover.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 30), stop:1 rgba(255, 255, 255, 255));")
        self.login_btn_login = QPushButton(self.widget)
        self.login_btn_login.setObjectName(u"login_btn_login")
        self.login_btn_login.setGeometry(QRect(330, 330, 321, 41))
        self.login_btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_btn_login.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgba(255, 255, 255, 180);\n"
"")
        self.login_btn_signup = QPushButton(self.widget)
        self.login_btn_signup.setObjectName(u"login_btn_signup")
        self.login_btn_signup.setGeometry(QRect(330, 380, 321, 31))
        self.login_btn_signup.setFont(font)
        self.login_btn_signup.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_btn_signup.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"color:rgba(255, 255, 255, 180);")
        self.login_label_disc = QLabel(self.widget)
        self.login_label_disc.setObjectName(u"login_label_disc")
        self.login_label_disc.setGeometry(QRect(330, 430, 351, 16))
        self.login_label_disc.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"color:rgba(255, 255, 255, 130);")
        self.horizontalLayoutWidget = QWidget(self.widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(410, 480, 156, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.login_btn_mail = QPushButton(self.horizontalLayoutWidget)
        self.login_btn_mail.setObjectName(u"login_btn_mail")
        self.login_btn_mail.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_btn_mail.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-closed.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border-radius: 14px;\n"
"margin-right: 10px;\n"
"margin-left:10px;")

        self.horizontalLayout_6.addWidget(self.login_btn_mail)

        self.login_btn_call = QPushButton(self.horizontalLayoutWidget)
        self.login_btn_call.setObjectName(u"login_btn_call")
        self.login_btn_call.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_btn_call.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-phone.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border-radius: 14px;\n"
"margin-right: 10px;\n"
"margin-left:10px;")

        self.horizontalLayout_6.addWidget(self.login_btn_call)

        self.login_btn_qrlogin = QPushButton(self.widget)
        self.login_btn_qrlogin.setObjectName(u"login_btn_qrlogin")
        self.login_btn_qrlogin.setGeometry(QRect(650, 330, 61, 41))
        self.login_btn_qrlogin.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_btn_qrlogin.setStyleSheet(u"background-repeat: no-repeat;\n"
"background-image: url(:/images/images/images/qr-code-scan.png);\n"
"background-position: center;\n"
"border-radius: 14px;\n"
"margin-right: 10px;\n"
"margin-left:10px;")
        self.login_label_back.raise_()
        self.login_label_cover.raise_()
        self.login_input_id.raise_()
        self.login_input_pw.raise_()
        self.login_label_logo.raise_()
        self.login_btn_login.raise_()
        self.login_btn_signup.raise_()
        self.login_label_disc.raise_()
        self.horizontalLayoutWidget.raise_()
        self.login_btn_qrlogin.raise_()

        self.gridLayout_3.addWidget(self.widget, 1, 0, 1, 1)


        self.verticalLayout_20.addLayout(self.gridLayout_3)

        self.stackedWidget.addWidget(self.loginpage)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-position: center;\n"
"background-repeat: no-repeat;\n"
"\n"
"")
        self.home_label_chatback = QLabel(self.home)
        self.home_label_chatback.setObjectName(u"home_label_chatback")
        self.home_label_chatback.setGeometry(QRect(190, 20, 771, 491))
        self.home_label_chatback.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;\n"
"")
        self.home_label_left1back = QLabel(self.home)
        self.home_label_left1back.setObjectName(u"home_label_left1back")
        self.home_label_left1back.setGeometry(QRect(20, 20, 151, 181))
        self.home_label_left1back.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.home_label_left2back = QLabel(self.home)
        self.home_label_left2back.setObjectName(u"home_label_left2back")
        self.home_label_left2back.setGeometry(QRect(20, 220, 151, 341))
        self.home_label_left2back.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.home_label_chatgroup = QLabel(self.home)
        self.home_label_chatgroup.setObjectName(u"home_label_chatgroup")
        self.home_label_chatgroup.setGeometry(QRect(64, 39, 91, 16))
        self.home_label_chatgroup.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";")
        self.home_label_chatgroup_pic = QLabel(self.home)
        self.home_label_chatgroup_pic.setObjectName(u"home_label_chatgroup_pic")
        self.home_label_chatgroup_pic.setGeometry(QRect(31, 37, 31, 21))
        self.home_label_chatgroup_pic.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chat-bubble.png);")
        self.home_label_userstate = QLabel(self.home)
        self.home_label_userstate.setObjectName(u"home_label_userstate")
        self.home_label_userstate.setGeometry(QRect(64, 240, 91, 16))
        self.home_label_userstate.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";")
        self.home_label_userstate_pic = QLabel(self.home)
        self.home_label_userstate_pic.setObjectName(u"home_label_userstate_pic")
        self.home_label_userstate_pic.setGeometry(QRect(31, 238, 31, 21))
        self.home_label_userstate_pic.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-people.png);")
        self.home_listview_chatgroup = QListView(self.home)
        self.home_listview_chatgroup.setObjectName(u"home_listview_chatgroup")
        self.home_listview_chatgroup.setGeometry(QRect(30, 70, 131, 91))
        self.home_listview_chatgroup.setStyleSheet(u"background-color: rgb(31, 35, 41);\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"font: 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.home_btn_chatgroup = QPushButton(self.home)
        self.home_btn_chatgroup.setObjectName(u"home_btn_chatgroup")
        self.home_btn_chatgroup.setGeometry(QRect(57, 170, 31, 24))
        self.home_btn_chatgroup.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_chatgroup.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-plus.png);\n"
"border:none;\n"
"")
        self.home_label_chatlist_title = QLabel(self.home)
        self.home_label_chatlist_title.setObjectName(u"home_label_chatlist_title")
        self.home_label_chatlist_title.setGeometry(QRect(220, 39, 91, 16))
        self.home_label_chatlist_title.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";")
        self.home_treeview_userlist = QTreeView(self.home)
        self.home_treeview_userlist.setObjectName(u"home_treeview_userlist")
        self.home_treeview_userlist.setGeometry(QRect(30, 270, 131, 251))
        self.home_treeview_userlist.setStyleSheet(u"background-color: rgb(31, 35, 41);\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"font: 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.home_lineedit_chatlist_send = QLineEdit(self.home)
        self.home_lineedit_chatlist_send.setObjectName(u"home_lineedit_chatlist_send")
        self.home_lineedit_chatlist_send.setGeometry(QRect(190, 519, 711, 41))
        self.home_lineedit_chatlist_send.setStyleSheet(u"border: 1px solid #497AA3;\n"
"border-radius: 10px;\n"
"padding-left: 30px; /* \uc67c\ucabd \uacf5\ubc31 */\n"
"background-color: rgb(33, 37, 43);\n"
"font: 600 \"Segoe UI Variable Small Semibol\";\n"
"font-size: 13px; /* \ud3f0\ud2b8 \ud06c\uae30 */\n"
"color: rgb(255, 255, 255); /* \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 */")
        self.home_listview_chatlist = QListView(self.home)
        self.home_listview_chatlist.setObjectName(u"home_listview_chatlist")
        self.home_listview_chatlist.setGeometry(QRect(220, 70, 711, 421))
        self.home_listview_chatlist.setStyleSheet(u"background-color: rgb(31, 35, 41);\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"font: 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.home_btn_chatlist_send = QPushButton(self.home)
        self.home_btn_chatlist_send.setObjectName(u"home_btn_chatlist_send")
        self.home_btn_chatlist_send.setGeometry(QRect(914, 520, 41, 41))
        self.home_btn_chatlist_send.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_chatlist_send.setStyleSheet(u"background-image: url(:/images/images/images/free-icon-send-button-12439334.png);\n"
"border: none;")
        self.home_btn_left = QPushButton(self.home)
        self.home_btn_left.setObjectName(u"home_btn_left")
        self.home_btn_left.setGeometry(QRect(30, 522, 31, 31))
        self.home_btn_left.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_left.setStyleSheet(u"background-image: url(:/images/images/images/left.png);\n"
"")
        self.home_btn_right = QPushButton(self.home)
        self.home_btn_right.setObjectName(u"home_btn_right")
        self.home_btn_right.setGeometry(QRect(130, 522, 31, 31))
        self.home_btn_right.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_right.setStyleSheet(u"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-image: url(:/images/images/images/right.png);\n"
"")
        self.home_btn_add_member = QPushButton(self.home)
        self.home_btn_add_member.setObjectName(u"home_btn_add_member")
        self.home_btn_add_member.setGeometry(QRect(908, 34, 31, 24))
        self.home_btn_add_member.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_add_member.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user-follow.png);\n"
"border:none;\n"
"")
        self.home_btn_groupmemberlist = QPushButton(self.home)
        self.home_btn_groupmemberlist.setObjectName(u"home_btn_groupmemberlist")
        self.home_btn_groupmemberlist.setGeometry(QRect(870, 34, 31, 24))
        self.home_btn_groupmemberlist.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_groupmemberlist.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user.png);\n"
"border:none;\n"
"")
        self.home_btn_groupdelete = QPushButton(self.home)
        self.home_btn_groupdelete.setObjectName(u"home_btn_groupdelete")
        self.home_btn_groupdelete.setGeometry(QRect(103, 170, 31, 24))
        self.home_btn_groupdelete.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_groupdelete.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user-unfollow.png);")
        self.stackedWidget.addWidget(self.home)
        self.adminpage = QWidget()
        self.adminpage.setObjectName(u"adminpage")
        self.adminpage.setStyleSheet(u"QPushButton#admin_btn_accept {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton#admin_btn_accept:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#admin_btn_accept:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}\n"
"\n"
"QPushButton#admin_btn_reject {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton#admin_btn_reject:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#admin_btn_reject:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}\n"
"\n"
"QPushButton#admin_btn_reload {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    pa"
                        "dding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton#admin_btn_reload:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#admin_btn_reload:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}")
        self.admin_label_leftback = QLabel(self.adminpage)
        self.admin_label_leftback.setObjectName(u"admin_label_leftback")
        self.admin_label_leftback.setGeometry(QRect(20, 20, 681, 541))
        self.admin_label_leftback.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;\n"
"border: 1px solid #3498db;\n"
"")
        self.admin_label_rightback1 = QLabel(self.adminpage)
        self.admin_label_rightback1.setObjectName(u"admin_label_rightback1")
        self.admin_label_rightback1.setGeometry(QRect(720, 20, 241, 541))
        self.admin_label_rightback1.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.admin_listView_status = QListView(self.adminpage)
        self.admin_listView_status.setObjectName(u"admin_listView_status")
        self.admin_listView_status.setGeometry(QRect(40, 70, 641, 431))
        self.admin_listView_status.setStyleSheet(u"background-color: rgb(31, 35, 41);\n"
"border-radius: 10px;\n"
"font: 600 10pt \"Segoe UI Variable Small Semibol\";")
        self.admin_label_status = QLabel(self.adminpage)
        self.admin_label_status.setObjectName(u"admin_label_status")
        self.admin_label_status.setGeometry(QRect(40, 40, 141, 21))
        self.admin_label_status.setStyleSheet(u"font: 600 10pt \"Segoe UI Variable Small Semibol\";")
        self.admin_btn_accept = QPushButton(self.adminpage)
        self.admin_btn_accept.setObjectName(u"admin_btn_accept")
        self.admin_btn_accept.setGeometry(QRect(510, 516, 81, 31))
        self.admin_btn_accept.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin_btn_accept.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";\n"
"border: 1px solid yellow;")
        self.admin_btn_reject = QPushButton(self.adminpage)
        self.admin_btn_reject.setObjectName(u"admin_btn_reject")
        self.admin_btn_reject.setGeometry(QRect(600, 516, 81, 31))
        self.admin_btn_reject.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin_btn_reject.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";\n"
"border: 1px solid white;\n"
"")
        self.admin_combo_dept = QComboBox(self.adminpage)
        self.admin_combo_dept.addItem("")
        self.admin_combo_dept.addItem("")
        self.admin_combo_dept.addItem("")
        self.admin_combo_dept.addItem("")
        self.admin_combo_dept.addItem("")
        self.admin_combo_dept.setObjectName(u"admin_combo_dept")
        self.admin_combo_dept.setGeometry(QRect(750, 70, 186, 33))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(8)
        font5.setWeight(QFont.ExtraLight)
        font5.setItalic(False)
        self.admin_combo_dept.setFont(font5)
        self.admin_combo_dept.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin_combo_dept.setAutoFillBackground(False)
        self.admin_combo_dept.setStyleSheet(u"\n"
"font: 8pt \"Segoe UI\";\n"
"font-weight: 200;\n"
"background-color: rgb(27, 29, 35);\n"
"")
        self.admin_combo_dept.setIconSize(QSize(16, 16))
        self.admin_combo_dept.setFrame(True)
        self.admin_combo_position = QComboBox(self.adminpage)
        self.admin_combo_position.addItem("")
        self.admin_combo_position.addItem("")
        self.admin_combo_position.addItem("")
        self.admin_combo_position.addItem("")
        self.admin_combo_position.addItem("")
        self.admin_combo_position.addItem("")
        self.admin_combo_position.addItem("")
        self.admin_combo_position.setObjectName(u"admin_combo_position")
        self.admin_combo_position.setGeometry(QRect(750, 190, 186, 33))
        self.admin_combo_position.setFont(font5)
        self.admin_combo_position.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin_combo_position.setAutoFillBackground(False)
        self.admin_combo_position.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"\n"
"font: 8pt \"Segoe UI\";\n"
"font-weight: 200;")
        self.admin_combo_position.setIconSize(QSize(16, 16))
        self.admin_combo_position.setFrame(True)
        self.admin_combo_role = QComboBox(self.adminpage)
        self.admin_combo_role.addItem("")
        self.admin_combo_role.addItem("")
        self.admin_combo_role.addItem("")
        self.admin_combo_role.setObjectName(u"admin_combo_role")
        self.admin_combo_role.setGeometry(QRect(750, 150, 186, 33))
        sizePolicy.setHeightForWidth(self.admin_combo_role.sizePolicy().hasHeightForWidth())
        self.admin_combo_role.setSizePolicy(sizePolicy)
        self.admin_combo_role.setFont(font5)
        self.admin_combo_role.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin_combo_role.setAutoFillBackground(False)
        self.admin_combo_role.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"\n"
"font: 8pt \"Segoe UI\";\n"
"font-weight: 200;")
        self.admin_combo_role.setIconSize(QSize(16, 16))
        self.admin_combo_role.setFrame(True)
        self.admin_combo_tps = QComboBox(self.adminpage)
        self.admin_combo_tps.addItem("")
        self.admin_combo_tps.addItem("")
        self.admin_combo_tps.addItem("")
        self.admin_combo_tps.addItem("")
        self.admin_combo_tps.setObjectName(u"admin_combo_tps")
        self.admin_combo_tps.setGeometry(QRect(750, 110, 186, 33))
        sizePolicy.setHeightForWidth(self.admin_combo_tps.sizePolicy().hasHeightForWidth())
        self.admin_combo_tps.setSizePolicy(sizePolicy)
        self.admin_combo_tps.setFont(font5)
        self.admin_combo_tps.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin_combo_tps.setAutoFillBackground(False)
        self.admin_combo_tps.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"\n"
"font: 8pt \"Segoe UI\";\n"
"font-weight: 200;")
        self.admin_combo_tps.setIconSize(QSize(16, 16))
        self.admin_combo_tps.setFrame(True)
        self.admin_btn_useredit = QPushButton(self.adminpage)
        self.admin_btn_useredit.setObjectName(u"admin_btn_useredit")
        self.admin_btn_useredit.setGeometry(QRect(744, 278, 41, 31))
        self.admin_btn_useredit.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin_btn_useredit.setStyleSheet(u"background-image: url(:/images/images/images/user-profile.png);\n"
"background-position: centered;\n"
"background-repeat: no-repeat;\n"
"")
        self.admin_btn_food = QPushButton(self.adminpage)
        self.admin_btn_food.setObjectName(u"admin_btn_food")
        self.admin_btn_food.setGeometry(QRect(820, 277, 41, 31))
        self.admin_btn_food.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin_btn_food.setStyleSheet(u"background-image: url(:/images/images/images/console (1).png);\n"
"background-position: centered;\n"
"background-repeat: no-repeat;")
        self.admin_label_one = QLabel(self.adminpage)
        self.admin_label_one.setObjectName(u"admin_label_one")
        self.admin_label_one.setGeometry(QRect(728, 265, 71, 71))
        self.admin_label_one.setStyleSheet(u"background-color: rgb(43, 47, 53);\n"
"border-radius: 10px;")
        self.admin_label_two = QLabel(self.adminpage)
        self.admin_label_two.setObjectName(u"admin_label_two")
        self.admin_label_two.setGeometry(QRect(805, 265, 71, 71))
        self.admin_label_two.setStyleSheet(u"background-color: rgb(43, 47, 53);\n"
"border-radius: 10px;")
        self.admin_label_three = QLabel(self.adminpage)
        self.admin_label_three.setObjectName(u"admin_label_three")
        self.admin_label_three.setGeometry(QRect(882, 265, 71, 71))
        self.admin_label_three.setStyleSheet(u"background-color: rgb(43, 47, 53);\n"
"border-radius: 10px;")
        self.admin_label_four = QLabel(self.adminpage)
        self.admin_label_four.setObjectName(u"admin_label_four")
        self.admin_label_four.setGeometry(QRect(728, 343, 71, 71))
        self.admin_label_four.setStyleSheet(u"background-color: rgb(43, 47, 53);\n"
"border-radius: 10px;")
        self.admin_label_five = QLabel(self.adminpage)
        self.admin_label_five.setObjectName(u"admin_label_five")
        self.admin_label_five.setGeometry(QRect(805, 343, 71, 71))
        self.admin_label_five.setStyleSheet(u"background-color: rgb(43, 47, 53);\n"
"border-radius: 10px;")
        self.admin_label_six = QLabel(self.adminpage)
        self.admin_label_six.setObjectName(u"admin_label_six")
        self.admin_label_six.setGeometry(QRect(882, 343, 71, 71))
        self.admin_label_six.setStyleSheet(u"background-color: rgb(43, 47, 53);\n"
"border-radius: 10px;")
        self.admin_label_seven = QLabel(self.adminpage)
        self.admin_label_seven.setObjectName(u"admin_label_seven")
        self.admin_label_seven.setGeometry(QRect(728, 420, 71, 71))
        self.admin_label_seven.setStyleSheet(u"background-color: rgb(43, 47, 53);\n"
"border-radius: 10px;")
        self.admin_label_eight = QLabel(self.adminpage)
        self.admin_label_eight.setObjectName(u"admin_label_eight")
        self.admin_label_eight.setGeometry(QRect(805, 421, 71, 71))
        self.admin_label_eight.setStyleSheet(u"background-color: rgb(43, 47, 53);\n"
"border-radius: 10px;")
        self.admin_label_nine = QLabel(self.adminpage)
        self.admin_label_nine.setObjectName(u"admin_label_nine")
        self.admin_label_nine.setGeometry(QRect(882, 421, 71, 71))
        self.admin_label_nine.setStyleSheet(u"background-color: rgb(43, 47, 53);\n"
"border-radius: 10px;")
        self.admin_label_infoedit = QLabel(self.adminpage)
        self.admin_label_infoedit.setObjectName(u"admin_label_infoedit")
        self.admin_label_infoedit.setGeometry(QRect(735, 313, 61, 16))
        self.admin_label_infoedit.setStyleSheet(u"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"background-color: rgb(40, 44, 50);\n"
"font: 9pt \"\uc0c8\uad74\ub9bc\";\n"
"\n"
"\n"
"")
        self.admin_label_game = QLabel(self.adminpage)
        self.admin_label_game.setObjectName(u"admin_label_game")
        self.admin_label_game.setGeometry(QRect(807, 314, 61, 16))
        self.admin_label_game.setStyleSheet(u"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"background-color: rgb(40, 44, 50);\n"
"font: 9pt \"\uc0c8\uad74\ub9bc\";")
        self.admin_btn_log = QPushButton(self.adminpage)
        self.admin_btn_log.setObjectName(u"admin_btn_log")
        self.admin_btn_log.setGeometry(QRect(897, 275, 41, 41))
        self.admin_btn_log.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin_btn_log.setStyleSheet(u"background-image: url(:/images/images/images/log-file.png);\n"
"background-position: centered;\n"
"background-repeat: no-repeat;")
        self.admin_label_log = QLabel(self.adminpage)
        self.admin_label_log.setObjectName(u"admin_label_log")
        self.admin_label_log.setGeometry(QRect(892, 313, 51, 20))
        self.admin_label_log.setStyleSheet(u"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"background-color: rgb(40, 44, 50);\n"
"font: 9pt \"\uc0c8\uad74\ub9bc\";")
        self.admin_btn_server = QPushButton(self.adminpage)
        self.admin_btn_server.setObjectName(u"admin_btn_server")
        self.admin_btn_server.setGeometry(QRect(745, 350, 41, 41))
        self.admin_btn_server.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin_btn_server.setStyleSheet(u"background-image: url(:/images/images/images/servers.png);\n"
"background-position: centered;\n"
"background-repeat: no-repeat;")
        self.admin_label_server = QLabel(self.adminpage)
        self.admin_label_server.setObjectName(u"admin_label_server")
        self.admin_label_server.setGeometry(QRect(739, 390, 51, 20))
        self.admin_label_server.setStyleSheet(u"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"background-color: rgb(40, 44, 50);\n"
"font: 9pt \"\uc0c8\uad74\ub9bc\";")
        self.stackedWidget.addWidget(self.adminpage)
        self.admin_label_rightback1.raise_()
        self.admin_label_leftback.raise_()
        self.admin_listView_status.raise_()
        self.admin_label_status.raise_()
        self.admin_btn_accept.raise_()
        self.admin_btn_reject.raise_()
        self.admin_combo_dept.raise_()
        self.admin_combo_position.raise_()
        self.admin_combo_role.raise_()
        self.admin_combo_tps.raise_()
        self.admin_label_one.raise_()
        self.admin_btn_useredit.raise_()
        self.admin_label_two.raise_()
        self.admin_btn_food.raise_()
        self.admin_label_three.raise_()
        self.admin_label_four.raise_()
        self.admin_label_five.raise_()
        self.admin_label_six.raise_()
        self.admin_label_seven.raise_()
        self.admin_label_eight.raise_()
        self.admin_label_nine.raise_()
        self.admin_label_infoedit.raise_()
        self.admin_label_game.raise_()
        self.admin_btn_log.raise_()
        self.admin_label_log.raise_()
        self.admin_btn_server.raise_()
        self.admin_label_server.raise_()
        self.serverlogpage = QWidget()
        self.serverlogpage.setObjectName(u"serverlogpage")
        self.serverlogpage.setStyleSheet(u"QPushButton#log_btn_search {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton#log_btn_search:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#log_btn_search:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}\n"
"\n"
"QPushButton#log_btn_back {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton#log_btn_back:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#log_btn_back:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}")
        self.log_treview_log = QTreeView(self.serverlogpage)
        self.log_treview_log.setObjectName(u"log_treview_log")
        self.log_treview_log.setGeometry(QRect(40, 70, 481, 471))
        self.log_treview_log.setStyleSheet(u"background-color: rgb(31, 35, 41);\n"
"border-radius: 10px;\n"
"font: 600 10pt \"Segoe UI Variable Small Semibol\";")
        self.log_calendarwidget_cal = QCalendarWidget(self.serverlogpage)
        self.log_calendarwidget_cal.setObjectName(u"log_calendarwidget_cal")
        self.log_calendarwidget_cal.setGeometry(QRect(565, 140, 381, 241))
        self.log_calendarwidget_cal.setStyleSheet(u"\n"
"/* \uc804\uccb4 \uc704\uc82f \ubc30\uacbd \uc0c9\uc0c1 \ubc0f \ubc30\uacbd \uc774\ubbf8\uc9c0 */\n"
"QCalendarWidget {\n"
"    background-color: #2e2e2e;\n"
"    border: 1px solid #444;\n"
"    border-radius: 5px;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"/* \ud5e4\ub354(\uc6d4/\uc5f0\ub3c4 \uc120\ud0dd \uc601\uc5ed) \uc2a4\ud0c0\uc77c\ub9c1 */\n"
"QCalendarWidget QToolButton {\n"
"    border: none; /* \ubc84\ud2bc\uc758 \ud14c\ub450\ub9ac \uc81c\uac70 */\n"
"    background-color: transparent; /* \ubc30\uacbd\uc0c9 \ud22c\uba85\ud558\uac8c \uc124\uc815 */\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    height: 30px;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"	font: 600 10pt \"Segoe UI Variable Small Semibol\";\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::hover {\n"
"    background-color: rgba(102, 102, 102, 0.8); /* \ud22c\uba85\ub3c4 \uc801\uc6a9 */\n"
"}\n"
"\n"
"/* \ud5e4\ub354\uc758 \ud654\uc0b4\ud45c \ubc84\ud2bc \uc2a4\ud0c0\uc77c\ub9c1"
                        " */\n"
"QCalendarWidget QToolButton#qt_calendar_prevmonth {\n"
"	\n"
"	\n"
"	background-position: center; /* \uc774\ubbf8\uc9c0\uac00 \uac00\uc6b4\ub370 \uc624\ub3c4\ub85d \uc124\uc815 */\n"
"    background-repeat: no-repeat;\n"
"    width: 30px; /* \ubc84\ud2bc\uc758 \ub108\ube44 \uc9c0\uc815 */\n"
"    height: 30px; /* \ubc84\ud2bc\uc758 \ub192\uc774 \uc9c0\uc815 */\n"
"    border: none; /* \ubc84\ud2bc\uc758 \ud14c\ub450\ub9ac \uc81c\uac70 */\n"
"    background-color: transparent; /* \ubc30\uacbd\uc0c9 \ud22c\uba85\ud558\uac8c \uc124\uc815 */\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_nextmonth {\n"
"	\n"
"	background-position: center; /* \uc774\ubbf8\uc9c0\uac00 \uac00\uc6b4\ub370 \uc624\ub3c4\ub85d \uc124\uc815 */\n"
"    background-repeat: no-repeat;\n"
"    width: 30px; /* \ubc84\ud2bc\uc758 \ub108\ube44 \uc9c0\uc815 */\n"
"    height: 30px; /* \ubc84\ud2bc\uc758 \ub192\uc774 \uc9c0\uc815 */\n"
"    border: none; /* \ubc84\ud2bc\uc758 \ud14c\ub450\ub9ac \uc81c\uac70 */\n"
"    background-col"
                        "or: transparent; /* \ubc30\uacbd\uc0c9 \ud22c\uba85\ud558\uac8c \uc124\uc815 */\n"
"}\n"
"\n"
"/* \ub0a0\uc9dc \uc140 \uc2a4\ud0c0\uc77c\ub9c1 */\n"
"QCalendarWidget QAbstractItemView {\n"
"\n"
"    background-color: rgba(58, 58, 58, 0.8); /* \ud22c\uba85\ub3c4 \uc801\uc6a9 */\n"
"    selection-background-color: #4CAF50;\n"
"    selection-color: white;\n"
"    border: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView::item {\n"
"    height: 30px;\n"
"    width: 30px;\n"
"    margin: 3px;\n"
"    color: white;\n"
"    background-color: rgba(58, 58, 58, 0.6); /* \uc140 \ubc30\uacbd\uc5d0 \ud22c\uba85\ub3c4 \uc801\uc6a9 */\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView::item:selected {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"/* \uc624\ub298 \ub0a0\uc9dc \uc2a4\ud0c0\uc77c\ub9c1 */\n"
"QCalendarWidget QWidget#qt_calendar_calendarview .QWidget {\n"
"    color: white;\n"
"    background-color: #FF5722;\n"
"    border-radius: 15px"
                        ";\n"
"}\n"
"\n"
"/* \uc694\uc77c \ud5e4\ub354 \uc2a4\ud0c0\uc77c\ub9c1 */\n"
"QCalendarWidget QTableView QHeaderView::section {\n"
"    background-color: rgba(85, 85, 85, 0.8); /* \ud22c\uba85\ub3c4 \uc801\uc6a9 */\n"
"    color: #888; /* \uc694\uc77c \uae00\uc790 \uc0c9\uc0c1\uc744 \uc5b4\ub450\uc6b4 \ud68c\uc0c9\uc73c\ub85c \ubcc0\uacbd */\n"
"    font-size: 14px;\n"
"    border: none;\n"
"    height: 30px;\n"
"}\n"
"\n"
"/* \ud604\uc7ac \uc6d4\uc5d0 \uc18d\ud558\uc9c0 \uc54a\ub294 \ub0a0\uc9dc \uc140 \uc2a4\ud0c0\uc77c\ub9c1 */\n"
"QCalendarWidget QAbstractItemView::item:disabled {\n"
"    background-color: rgba(30, 30, 30, 0.6); /* \ud604\uc7ac \uc6d4\uc5d0 \uc18d\ud558\uc9c0 \uc54a\ub294 \ub0a0\uc9dc\uc758 \ubc30\uacbd \uc0c9\uc0c1 */\n"
"    color: rgba(255, 255, 255, 0.5); /* \ud604\uc7ac \uc6d4\uc5d0 \uc18d\ud558\uc9c0 \uc54a\ub294 \ub0a0\uc9dc\uc758 \uae00\uc790 \uc0c9\uc0c1 */\n"
"}\n"
"")
        self.log_btn_back = QPushButton(self.serverlogpage)
        self.log_btn_back.setObjectName(u"log_btn_back")
        self.log_btn_back.setGeometry(QRect(910, 40, 31, 31))
        self.log_btn_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.log_btn_back.setStyleSheet(u"background-image: url(:/images/images/icons/free-icon-back-button-5708793 (1).png);\n"
"background-position: centered;\n"
"background-repeat: no-repeat;\n"
"border:none;\n"
"")
        self.log_label_leftback = QLabel(self.serverlogpage)
        self.log_label_leftback.setObjectName(u"log_label_leftback")
        self.log_label_leftback.setGeometry(QRect(20, 20, 521, 541))
        self.log_label_leftback.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;\n"
"border: 1px solid #3498db;\n"
"")
        self.log_label_title = QLabel(self.serverlogpage)
        self.log_label_title.setObjectName(u"log_label_title")
        self.log_label_title.setGeometry(QRect(40, 40, 141, 21))
        self.log_label_title.setStyleSheet(u"font: 600 10pt \"Segoe UI Variable Small Semibol\";")
        self.log_label_rightback = QLabel(self.serverlogpage)
        self.log_label_rightback.setObjectName(u"log_label_rightback")
        self.log_label_rightback.setGeometry(QRect(550, 20, 411, 541))
        self.log_label_rightback.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.stackedWidget.addWidget(self.serverlogpage)
        self.log_label_rightback.raise_()
        self.log_label_leftback.raise_()
        self.log_treview_log.raise_()
        self.log_btn_back.raise_()
        self.log_label_title.raise_()
        self.log_calendarwidget_cal.raise_()
        self.serverstatepage = QWidget()
        self.serverstatepage.setObjectName(u"serverstatepage")
        self.serverstatepage.setStyleSheet(u"QPushButton#serverstate_btn_reload {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    color: white;\n"
"	border-right: none;\n"
"	border-top: none;\n"
"	border-left: none;\n"
"	\n"
"}\n"
"\n"
"\n"
"QPushButton#serverstate_btn_reload:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#serverstate_btn_reload:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}\n"
"\n"
"QPushButton#serverstate_btn_back {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"}\n"
"QPushButton#serverstate_btn_back:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#serverstate_btn_back:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}\n"
"\n"
"QPushButton#serverstate_btn_grafana {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"	border-ri"
                        "ght: none;\n"
"	border-top: none;\n"
"	border-left: none;\n"
"\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton#serverstate_btn_grafana:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#serverstate_btn_grafana:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}")
        self.serverstate_label_back = QLabel(self.serverstatepage)
        self.serverstate_label_back.setObjectName(u"serverstate_label_back")
        self.serverstate_label_back.setGeometry(QRect(20, 20, 941, 541))
        self.serverstate_label_back.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.serverstate_label_topback = QLabel(self.serverstatepage)
        self.serverstate_label_topback.setObjectName(u"serverstate_label_topback")
        self.serverstate_label_topback.setGeometry(QRect(50, 100, 881, 121))
        self.serverstate_label_topback.setStyleSheet(u"background-color: rgb(31, 35, 41);\n"
"border-radius: 10px;")
        self.serverstate_label_toptitle = QLabel(self.serverstatepage)
        self.serverstate_label_toptitle.setObjectName(u"serverstate_label_toptitle")
        self.serverstate_label_toptitle.setGeometry(QRect(68, 111, 111, 21))
        self.serverstate_label_toptitle.setStyleSheet(u"font: 600 10pt \"Segoe UI Variable Small Semibol\";")
        self.serverstate_label_midback = QLabel(self.serverstatepage)
        self.serverstate_label_midback.setObjectName(u"serverstate_label_midback")
        self.serverstate_label_midback.setGeometry(QRect(50, 249, 881, 131))
        self.serverstate_label_midback.setStyleSheet(u"background-color: rgb(31, 35, 41);\n"
"border-radius: 10px;")
        self.serverstate_label_midtitle = QLabel(self.serverstatepage)
        self.serverstate_label_midtitle.setObjectName(u"serverstate_label_midtitle")
        self.serverstate_label_midtitle.setGeometry(QRect(68, 260, 181, 21))
        self.serverstate_label_midtitle.setStyleSheet(u"font: 600 10pt \"Segoe UI Variable Small Semibol\";")
        self.serverstate_label_botback = QLabel(self.serverstatepage)
        self.serverstate_label_botback.setObjectName(u"serverstate_label_botback")
        self.serverstate_label_botback.setGeometry(QRect(50, 409, 881, 121))
        self.serverstate_label_botback.setStyleSheet(u"background-color: rgb(31, 35, 41);\n"
"border-radius: 10px;")
        self.serverstate_label_bottomtitle = QLabel(self.serverstatepage)
        self.serverstate_label_bottomtitle.setObjectName(u"serverstate_label_bottomtitle")
        self.serverstate_label_bottomtitle.setGeometry(QRect(68, 420, 231, 21))
        self.serverstate_label_bottomtitle.setStyleSheet(u"font: 600 10pt \"Segoe UI Variable Small Semibol\";")
        self.serverstate_btn_back = QPushButton(self.serverstatepage)
        self.serverstate_btn_back.setObjectName(u"serverstate_btn_back")
        self.serverstate_btn_back.setGeometry(QRect(910, 40, 31, 31))
        self.serverstate_btn_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.serverstate_btn_back.setStyleSheet(u"background-image: url(:/images/images/icons/free-icon-back-button-5708793 (1).png);\n"
"background-position: centered;\n"
"background-repeat: no-repeat;\n"
"border:none;\n"
"")
        self.serverstate_btn_reload = QPushButton(self.serverstatepage)
        self.serverstate_btn_reload.setObjectName(u"serverstate_btn_reload")
        self.serverstate_btn_reload.setGeometry(QRect(50, 40, 41, 31))
        self.serverstate_btn_reload.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-reload.png);\n"
"background-position: center; /* \uc774\ubbf8\uc9c0\uac00 \uac00\uc6b4\ub370 \uc624\ub3c4\ub85d \uc124\uc815 */\n"
"background-repeat: no-repeat;\n"
"width: 30px; /* \ubc84\ud2bc\uc758 \ub108\ube44 \uc9c0\uc815 */\n"
"height: 30px; /* \ubc84\ud2bc\uc758 \ub192\uc774 \uc9c0\uc815 */\n"
"")
        self.serverstate_btn_grafana = QPushButton(self.serverstatepage)
        self.serverstate_btn_grafana.setObjectName(u"serverstate_btn_grafana")
        self.serverstate_btn_grafana.setGeometry(QRect(110, 40, 41, 31))
        self.serverstate_btn_grafana.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart-line.png);\n"
"background-position: center; /* \uc774\ubbf8\uc9c0\uac00 \uac00\uc6b4\ub370 \uc624\ub3c4\ub85d \uc124\uc815 */\n"
"background-repeat: no-repeat;\n"
"width: 30px; /* \ubc84\ud2bc\uc758 \ub108\ube44 \uc9c0\uc815 */\n"
"height: 30px; /* \ubc84\ud2bc\uc758 \ub192\uc774 \uc9c0\uc815 */\n"
"")
        self.serverstate_listview_mem = QListView(self.serverstatepage)
        self.serverstate_listview_mem.setObjectName(u"serverstate_listview_mem")
        self.serverstate_listview_mem.setGeometry(QRect(70, 150, 841, 41))
        self.serverstate_listview_numuser = QListView(self.serverstatepage)
        self.serverstate_listview_numuser.setObjectName(u"serverstate_listview_numuser")
        self.serverstate_listview_numuser.setGeometry(QRect(70, 300, 841, 41))
        self.serverstate_listview_packet = QListView(self.serverstatepage)
        self.serverstate_listview_packet.setObjectName(u"serverstate_listview_packet")
        self.serverstate_listview_packet.setGeometry(QRect(70, 460, 841, 41))
        self.stackedWidget.addWidget(self.serverstatepage)
        self.qrlogin = QWidget()
        self.qrlogin.setObjectName(u"qrlogin")
        self.qrlogin_label_waiting = QLabel(self.qrlogin)
        self.qrlogin_label_waiting.setObjectName(u"qrlogin_label_waiting")
        self.qrlogin_label_waiting.setGeometry(QRect(280, 90, 431, 411))
        self.qrlogin_btn_back = QPushButton(self.qrlogin)
        self.qrlogin_btn_back.setObjectName(u"qrlogin_btn_back")
        self.qrlogin_btn_back.setGeometry(QRect(753, 80, 31, 31))
        self.qrlogin_btn_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.qrlogin_btn_back.setStyleSheet(u"background-image: url(:/images/images/icons/free-icon-back-button-5708793 (1).png);\n"
"background-position: centered;\n"
"background-repeat: no-repeat;\n"
"border:none;\n"
"")
        self.qrlogin_label_back = QLabel(self.qrlogin)
        self.qrlogin_label_back.setObjectName(u"qrlogin_label_back")
        self.qrlogin_label_back.setGeometry(QRect(20, 20, 941, 541))
        self.qrlogin_label_back.setStyleSheet(u"background-image: url(:/images/images/images/loginbackground.jpg);\n"
"border-radius: 20px;\n"
"")
        self.stackedWidget.addWidget(self.qrlogin)
        self.qrlogin_label_back.raise_()
        self.qrlogin_label_waiting.raise_()
        self.qrlogin_btn_back.raise_()
        self.signuppage = QWidget()
        self.signuppage.setObjectName(u"signuppage")
        self.signuppage.setStyleSheet(u"QPushButton#signup_btn_submit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton#signup_btn_submit:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#signup_btn_submit:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}\n"
"\n"
"QPushButton#signup_btn_back {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton#signup_btn_back:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#signup_btn_back:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}")
        self.signup_label_back = QLabel(self.signuppage)
        self.signup_label_back.setObjectName(u"signup_label_back")
        self.signup_label_back.setGeometry(QRect(20, 20, 941, 541))
        self.signup_label_back.setStyleSheet(u"background-image: url(:/images/images/images/loginbackground.jpg);\n"
"border-radius: 20px;\n"
"")
        self.signup_input_id = QLineEdit(self.signuppage)
        self.signup_input_id.setObjectName(u"signup_input_id")
        self.signup_input_id.setGeometry(QRect(280, 130, 421, 31))
        self.signup_input_id.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255, 255, 255, 120);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;\n"
"font: 12pt \"Segoe UI\";\n"
"border-radius: none;")
        self.signup_input_pw = QLineEdit(self.signuppage)
        self.signup_input_pw.setObjectName(u"signup_input_pw")
        self.signup_input_pw.setGeometry(QRect(280, 180, 421, 31))
        self.signup_input_pw.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255, 255, 255, 120);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;\n"
"font: 12pt \"Segoe UI\";\n"
"border-radius: none;")
        self.signup_input_pw.setEchoMode(QLineEdit.EchoMode.Password)
        self.signup_input_name = QLineEdit(self.signuppage)
        self.signup_input_name.setObjectName(u"signup_input_name")
        self.signup_input_name.setGeometry(QRect(280, 230, 421, 31))
        self.signup_input_name.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255, 255, 255, 120);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;\n"
"font: 12pt \"Segoe UI\";\n"
"border-radius: none;")
        self.signup_input_phone = QLineEdit(self.signuppage)
        self.signup_input_phone.setObjectName(u"signup_input_phone")
        self.signup_input_phone.setGeometry(QRect(280, 280, 421, 31))
        self.signup_input_phone.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255, 255, 255, 120);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;\n"
"font: 12pt \"Segoe UI\";\n"
"border-radius: none;")
        self.signup_input_email = QLineEdit(self.signuppage)
        self.signup_input_email.setObjectName(u"signup_input_email")
        self.signup_input_email.setGeometry(QRect(280, 330, 421, 31))
        self.signup_input_email.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255, 255, 255, 120);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;\n"
"font: 12pt \"Segoe UI\";\n"
"border-radius: none;")
        self.signup_btn_submit = QPushButton(self.signuppage)
        self.signup_btn_submit.setObjectName(u"signup_btn_submit")
        self.signup_btn_submit.setGeometry(QRect(330, 450, 331, 41))
        self.signup_btn_submit.setCursor(QCursor(Qt.PointingHandCursor))
        self.signup_btn_submit.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"")
        self.signup_checkbox_agree = QCheckBox(self.signuppage)
        self.signup_checkbox_agree.setObjectName(u"signup_checkbox_agree")
        self.signup_checkbox_agree.setGeometry(QRect(340, 420, 21, 20))
        self.signup_checkbox_agree.setCursor(QCursor(Qt.PointingHandCursor))
        self.signup_label_useagree = QLabel(self.signuppage)
        self.signup_label_useagree.setObjectName(u"signup_label_useagree")
        self.signup_label_useagree.setGeometry(QRect(370, 422, 51, 16))
        self.signup_label_useagree.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"font-weight: 200;")
        self.signup_label_infoagree = QLabel(self.signuppage)
        self.signup_label_infoagree.setObjectName(u"signup_label_infoagree")
        self.signup_label_infoagree.setGeometry(QRect(424, 422, 241, 16))
        self.signup_label_infoagree.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"font-weight: 200;")
        self.signup_btn_back = QPushButton(self.signuppage)
        self.signup_btn_back.setObjectName(u"signup_btn_back")
        self.signup_btn_back.setGeometry(QRect(753, 80, 31, 31))
        self.signup_btn_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.signup_btn_back.setStyleSheet(u"background-image: url(:/images/images/icons/free-icon-back-button-5708793 (1).png);\n"
"background-position: centered;\n"
"background-repeat: no-repeat;\n"
"border:none;\n"
"")
        self.stackedWidget.addWidget(self.signuppage)
        self.infoeditpage = QWidget()
        self.infoeditpage.setObjectName(u"infoeditpage")
        self.infoeditpage.setStyleSheet(u"QPushButton#useredit_btn_reset {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton#useredit_btn_reset:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#useredit_btn_reset:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}\n"
"\n"
"QPushButton#useredit_btn_send {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton#useredit_btn_send:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#useredit_btn_send:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}\n"
"\n"
"QPushButton#useredit_btn_back {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;"
                        "\n"
"    padding: 5px 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton#useredit_btn_back:hover {\n"
"    background-color: rgba(70, 130, 180, 1);\n"
"}\n"
"\n"
"QPushButton#useredit_btn_back:pressed {\n"
"    background-color: rgba(25, 25, 112, 1);\n"
"}")
        self.useredit_label_back = QLabel(self.infoeditpage)
        self.useredit_label_back.setObjectName(u"useredit_label_back")
        self.useredit_label_back.setGeometry(QRect(20, 20, 941, 541))
        self.useredit_label_back.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;\n"
"")
        self.useredit_label_title = QLabel(self.infoeditpage)
        self.useredit_label_title.setObjectName(u"useredit_label_title")
        self.useredit_label_title.setGeometry(QRect(380, 61, 211, 41))
        self.useredit_label_title.setStyleSheet(u"background-image: url(:/images/images/images/\uc2a4\ud06c\ub9b0\uc0f7 2024-06-26 110605.png);\n"
"background-position: centered;\n"
"background-repeat: no-repeat;")
        self.useredit_label_upline = QLabel(self.infoeditpage)
        self.useredit_label_upline.setObjectName(u"useredit_label_upline")
        self.useredit_label_upline.setGeometry(QRect(50, 110, 881, 16))
        self.useredit_label_upline.setStyleSheet(u"border-bottom:2px solid rgba(255, 255, 255, 150);")
        self.useredit_label_id = QLabel(self.infoeditpage)
        self.useredit_label_id.setObjectName(u"useredit_label_id")
        self.useredit_label_id.setGeometry(QRect(488, 199, 51, 21))
        self.useredit_label_id.setStyleSheet(u"font: 600 12pt \"Segoe UI Variable Small Semibol\";\n"
"background-position: centered;\n"
"background-repeat: no-repeat;")
        self.useredit_label_name = QLabel(self.infoeditpage)
        self.useredit_label_name.setObjectName(u"useredit_label_name")
        self.useredit_label_name.setGeometry(QRect(495, 236, 41, 31))
        self.useredit_label_name.setStyleSheet(u"font: 600 12pt \"Segoe UI Variable Small Semibol\";\n"
"background-position: centered;\n"
"background-repeat: no-repeat;")
        self.useredit_label_phone = QLabel(self.infoeditpage)
        self.useredit_label_phone.setObjectName(u"useredit_label_phone")
        self.useredit_label_phone.setGeometry(QRect(480, 276, 71, 31))
        self.useredit_label_phone.setStyleSheet(u"font: 600 12pt \"Segoe UI Variable Small Semibol\";\n"
"background-position: centered;\n"
"background-repeat: no-repeat;")
        self.useredit_label_email = QLabel(self.infoeditpage)
        self.useredit_label_email.setObjectName(u"useredit_label_email")
        self.useredit_label_email.setGeometry(QRect(487, 316, 51, 31))
        self.useredit_label_email.setStyleSheet(u"font: 600 12pt \"Segoe UI Variable Small Semibol\";\n"
"background-position: centered;\n"
"background-repeat: no-repeat;")
        self.useredit_label_downline = QLabel(self.infoeditpage)
        self.useredit_label_downline.setObjectName(u"useredit_label_downline")
        self.useredit_label_downline.setGeometry(QRect(50, 460, 881, 16))
        self.useredit_label_downline.setStyleSheet(u"border-bottom:2px solid rgba(255, 255, 255, 150);")
        self.useredit_btn_back = QPushButton(self.infoeditpage)
        self.useredit_btn_back.setObjectName(u"useredit_btn_back")
        self.useredit_btn_back.setGeometry(QRect(900, 66, 31, 31))
        self.useredit_btn_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.useredit_btn_back.setStyleSheet(u"background-image: url(:/images/images/icons/free-icon-back-button-5708793 (1).png);\n"
"background-position: centered;\n"
"background-repeat: no-repeat;\n"
"border:none;\n"
"")
        self.useredit_btn_reset = QPushButton(self.infoeditpage)
        self.useredit_btn_reset.setObjectName(u"useredit_btn_reset")
        self.useredit_btn_reset.setGeometry(QRect(400, 504, 75, 24))
        self.useredit_btn_reset.setCursor(QCursor(Qt.PointingHandCursor))
        self.useredit_btn_reset.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";\n"
"border: 1px solid white;\n"
"")
        self.useredit_btn_send = QPushButton(self.infoeditpage)
        self.useredit_btn_send.setObjectName(u"useredit_btn_send")
        self.useredit_btn_send.setGeometry(QRect(510, 504, 75, 24))
        self.useredit_btn_send.setCursor(QCursor(Qt.PointingHandCursor))
        self.useredit_btn_send.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";\n"
"border: 1px solid yellow;\n"
"")
        self.useredit_edit_id = QLineEdit(self.infoeditpage)
        self.useredit_edit_id.setObjectName(u"useredit_edit_id")
        self.useredit_edit_id.setEnabled(False)
        self.useredit_edit_id.setGeometry(QRect(560, 187, 281, 41))
        self.useredit_edit_id.setStyleSheet(u"border-bottom:1px solid rgba(255, 255, 255, 120);\n"
"border-top: none;\n"
"border-right: none;\n"
"border-left: none;\n"
"font: 600 10pt \"Segoe UI Variable Small Semibol\";\n"
"border-radius: none;")
        self.useredit_edit_name = QLineEdit(self.infoeditpage)
        self.useredit_edit_name.setObjectName(u"useredit_edit_name")
        self.useredit_edit_name.setGeometry(QRect(560, 224, 281, 41))
        self.useredit_edit_name.setStyleSheet(u"border-bottom:1px solid rgba(255, 255, 255, 120);\n"
"border-top: none;\n"
"border-right: none;\n"
"border-left: none;\n"
"font: 600 10pt \"Segoe UI Variable Small Semibol\";\n"
"border-radius: none;")
        self.useredit_edit_phone = QLineEdit(self.infoeditpage)
        self.useredit_edit_phone.setObjectName(u"useredit_edit_phone")
        self.useredit_edit_phone.setGeometry(QRect(560, 264, 281, 41))
        self.useredit_edit_phone.setStyleSheet(u"border-bottom:1px solid rgba(255, 255, 255, 120);\n"
"border-top: none;\n"
"border-right: none;\n"
"border-left: none;\n"
"font: 600 10pt \"Segoe UI Variable Small Semibol\";\n"
"border-radius: none;")
        self.useredit_edit_email = QLineEdit(self.infoeditpage)
        self.useredit_edit_email.setObjectName(u"useredit_edit_email")
        self.useredit_edit_email.setGeometry(QRect(560, 304, 281, 41))
        self.useredit_edit_email.setStyleSheet(u"border-bottom:1px solid rgba(255, 255, 255, 120);\n"
"border-top: none;\n"
"border-right: none;\n"
"border-left: none;\n"
"font: 600 10pt \"Segoe UI Variable Small Semibol\";\n"
"border-radius: none;")
        self.useredit_combo_dept = QComboBox(self.infoeditpage)
        self.useredit_combo_dept.addItem("")
        self.useredit_combo_dept.addItem("")
        self.useredit_combo_dept.addItem("")
        self.useredit_combo_dept.addItem("")
        self.useredit_combo_dept.addItem("")
        self.useredit_combo_dept.setObjectName(u"useredit_combo_dept")
        self.useredit_combo_dept.setGeometry(QRect(558, 377, 141, 33))
        self.useredit_combo_dept.setFont(font5)
        self.useredit_combo_dept.setCursor(QCursor(Qt.PointingHandCursor))
        self.useredit_combo_dept.setAutoFillBackground(False)
        self.useredit_combo_dept.setStyleSheet(u"\n"
"font: 8pt \"Segoe UI\";\n"
"font-weight: 200;\n"
"background-color: rgb(27, 29, 35);\n"
"")
        self.useredit_combo_dept.setIconSize(QSize(16, 16))
        self.useredit_combo_dept.setFrame(True)
        self.useredit_combo_position = QComboBox(self.infoeditpage)
        self.useredit_combo_position.addItem("")
        self.useredit_combo_position.addItem("")
        self.useredit_combo_position.addItem("")
        self.useredit_combo_position.addItem("")
        self.useredit_combo_position.addItem("")
        self.useredit_combo_position.addItem("")
        self.useredit_combo_position.addItem("")
        self.useredit_combo_position.setObjectName(u"useredit_combo_position")
        self.useredit_combo_position.setGeometry(QRect(700, 377, 141, 33))
        self.useredit_combo_position.setFont(font5)
        self.useredit_combo_position.setCursor(QCursor(Qt.PointingHandCursor))
        self.useredit_combo_position.setAutoFillBackground(False)
        self.useredit_combo_position.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"font: 8pt \"Segoe UI\";\n"
"font-weight: 200;")
        self.useredit_combo_position.setIconSize(QSize(16, 16))
        self.useredit_combo_position.setFrame(True)
        self.useredit_treeview_userlist = QTreeView(self.infoeditpage)
        self.useredit_treeview_userlist.setObjectName(u"useredit_treeview_userlist")
        self.useredit_treeview_userlist.setGeometry(QRect(50, 170, 391, 281))
        self.useredit_treeview_userlist.setStyleSheet(u"background-color: rgb(31, 35, 41);\n"
"font: 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.useredit_combo_role = QComboBox(self.infoeditpage)
        self.useredit_combo_role.addItem("")
        self.useredit_combo_role.addItem("")
        self.useredit_combo_role.addItem("")
        self.useredit_combo_role.setObjectName(u"useredit_combo_role")
        self.useredit_combo_role.setGeometry(QRect(700, 417, 141, 33))
        sizePolicy.setHeightForWidth(self.useredit_combo_role.sizePolicy().hasHeightForWidth())
        self.useredit_combo_role.setSizePolicy(sizePolicy)
        self.useredit_combo_role.setFont(font5)
        self.useredit_combo_role.setCursor(QCursor(Qt.PointingHandCursor))
        self.useredit_combo_role.setAutoFillBackground(False)
        self.useredit_combo_role.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"\n"
"font: 8pt \"Segoe UI\";\n"
"font-weight: 200;")
        self.useredit_combo_role.setIconSize(QSize(16, 16))
        self.useredit_combo_role.setFrame(True)
        self.useredit_combo_tps = QComboBox(self.infoeditpage)
        self.useredit_combo_tps.addItem("")
        self.useredit_combo_tps.addItem("")
        self.useredit_combo_tps.addItem("")
        self.useredit_combo_tps.addItem("")
        self.useredit_combo_tps.setObjectName(u"useredit_combo_tps")
        self.useredit_combo_tps.setGeometry(QRect(557, 417, 141, 33))
        sizePolicy.setHeightForWidth(self.useredit_combo_tps.sizePolicy().hasHeightForWidth())
        self.useredit_combo_tps.setSizePolicy(sizePolicy)
        self.useredit_combo_tps.setFont(font5)
        self.useredit_combo_tps.setCursor(QCursor(Qt.PointingHandCursor))
        self.useredit_combo_tps.setAutoFillBackground(False)
        self.useredit_combo_tps.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"\n"
"font: 8pt \"Segoe UI\";\n"
"font-weight: 200;")
        self.useredit_combo_tps.setIconSize(QSize(16, 16))
        self.useredit_combo_tps.setFrame(True)
        self.label = QLabel(self.infoeditpage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 140, 81, 20))
        self.label.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small Semibol\";")
        self.stackedWidget.addWidget(self.infoeditpage)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy1.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy1)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy1.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy1)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)
        self.signup_input_id.returnPressed.connect(self.signup_btn_submit.click)
        self.signup_input_pw.returnPressed.connect(self.signup_btn_submit.click)
        self.signup_input_name.returnPressed.connect(self.signup_btn_submit.click)
        self.signup_input_phone.returnPressed.connect(self.signup_btn_submit.click)
        self.signup_input_email.returnPressed.connect(self.signup_btn_submit.click)
        self.signup_btn_submit.clicked.connect(MainWindow.signUpRequest)
        self.login_input_id.returnPressed.connect(self.login_btn_login.click)
        self.login_input_pw.returnPressed.connect(self.login_btn_login.click)
        self.login_btn_login.clicked.connect(MainWindow.loginRequest)
        self.signup_checkbox_agree.stateChanged.connect(MainWindow.toggleButton)
        self.home_lineedit_chatlist_send.returnPressed.connect(self.home_btn_chatlist_send.click)
        self.home_btn_chatlist_send.clicked.connect(MainWindow.sendMsg)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Chat", None))
        self.btn_admin.setText(QCoreApplication.translate("MainWindow", u"Manager", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_notice.setText(QCoreApplication.translate("MainWindow", u"Notice", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zen"
                        "o Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Talk Talk :: \uc138\uc0c1 \ubaa8\ub4e0 \uac83\uc744 \uc5f0\uacb0\ud558\ub2e4.", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.login_label_back.setText("")
        self.login_label_logo.setText(QCoreApplication.translate("MainWindow", u"\u2728 LOGIN", None))
        self.login_input_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.login_input_pw.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.login_label_cover.setText("")
        self.login_btn_login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.login_btn_signup.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.login_label_disc.setText(QCoreApplication.translate("MainWindow", u"forget your password, please contact the administrator.", None))
        self.login_btn_mail.setText("")
        self.login_btn_call.setText("")
        self.login_btn_qrlogin.setText("")
        self.home_label_chatback.setText("")
        self.home_label_left1back.setText("")
        self.home_label_left2back.setText("")
        self.home_label_chatgroup.setText(QCoreApplication.translate("MainWindow", u"\ucc44\ud305 \uadf8\ub8f9 \ubaa9\ub85d", None))
        self.home_label_chatgroup_pic.setText("")
        self.home_label_userstate.setText(QCoreApplication.translate("MainWindow", u"\uc720\uc800 \uc0c1\ud0dc \ubaa9\ub85d", None))
        self.home_label_userstate_pic.setText("")
        self.home_btn_chatgroup.setText("")
        self.home_label_chatlist_title.setText(QCoreApplication.translate("MainWindow", u"\ucc44\ud305 \uadf8\ub8f9 \uba85", None))
        self.home_btn_chatlist_send.setText("")
        self.home_btn_left.setText("")
        self.home_btn_right.setText("")
        self.home_btn_add_member.setText("")
        self.home_btn_groupmemberlist.setText("")
        self.home_btn_groupdelete.setText("")
        self.admin_label_leftback.setText("")
        self.admin_label_rightback1.setText("")
        self.admin_label_status.setText(QCoreApplication.translate("MainWindow", u"\ud68c\uc6d0 \ub4f1\ub85d / \ud68c\uc6d0 \uc0c1\ud0dc", None))
        self.admin_btn_accept.setText(QCoreApplication.translate("MainWindow", u"\uc218\ub77d", None))
        self.admin_btn_reject.setText(QCoreApplication.translate("MainWindow", u"\uac70\uc808", None))
        self.admin_combo_dept.setItemText(0, QCoreApplication.translate("MainWindow", u"\ubd80\uc11c\ub97c \uc120\ud0dd\ud558\uc138\uc694.", None))
        self.admin_combo_dept.setItemText(1, QCoreApplication.translate("MainWindow", u" 1\ud300", None))
        self.admin_combo_dept.setItemText(2, QCoreApplication.translate("MainWindow", u" 2\ud300", None))
        self.admin_combo_dept.setItemText(3, QCoreApplication.translate("MainWindow", u" 3\ud300", None))
        self.admin_combo_dept.setItemText(4, QCoreApplication.translate("MainWindow", u" \uc194\ub8e8\uc158\ud300", None))

        self.admin_combo_dept.setCurrentText(QCoreApplication.translate("MainWindow", u"\ubd80\uc11c\ub97c \uc120\ud0dd\ud558\uc138\uc694.", None))
        self.admin_combo_position.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc9c1\uae09\uc744 \uc120\ud0dd\ud558\uc138\uc694.", None))
        self.admin_combo_position.setItemText(1, QCoreApplication.translate("MainWindow", u"\ud68c\uc7a5", None))
        self.admin_combo_position.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc0ac\uc7a5", None))
        self.admin_combo_position.setItemText(3, QCoreApplication.translate("MainWindow", u"\ucc28\uc7a5", None))
        self.admin_combo_position.setItemText(4, QCoreApplication.translate("MainWindow", u"\uacfc\uc7a5", None))
        self.admin_combo_position.setItemText(5, QCoreApplication.translate("MainWindow", u"\ub300\ub9ac", None))
        self.admin_combo_position.setItemText(6, QCoreApplication.translate("MainWindow", u"\uc0ac\uc6d0", None))

        self.admin_combo_position.setCurrentText(QCoreApplication.translate("MainWindow", u"\uc9c1\uae09\uc744 \uc120\ud0dd\ud558\uc138\uc694.", None))
        self.admin_combo_role.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc5ed\ud560\uc744 \uc120\ud0dd\ud558\uc138\uc694", None))
        self.admin_combo_role.setItemText(1, QCoreApplication.translate("MainWindow", u"0", None))
        self.admin_combo_role.setItemText(2, QCoreApplication.translate("MainWindow", u"1", None))

        self.admin_combo_role.setCurrentText(QCoreApplication.translate("MainWindow", u"\uc5ed\ud560\uc744 \uc120\ud0dd\ud558\uc138\uc694", None))
        self.admin_combo_tps.setItemText(0, QCoreApplication.translate("MainWindow", u"tps\ub97c \uc120\ud0dd\ud558\uc138\uc694", None))
        self.admin_combo_tps.setItemText(1, QCoreApplication.translate("MainWindow", u"5", None))
        self.admin_combo_tps.setItemText(2, QCoreApplication.translate("MainWindow", u"30", None))
        self.admin_combo_tps.setItemText(3, QCoreApplication.translate("MainWindow", u"100", None))

        self.admin_combo_tps.setCurrentText(QCoreApplication.translate("MainWindow", u"tps\ub97c \uc120\ud0dd\ud558\uc138\uc694", None))
        self.admin_btn_useredit.setText("")
        self.admin_btn_food.setText("")
        self.admin_label_one.setText("")
        self.admin_label_two.setText("")
        self.admin_label_three.setText("")
        self.admin_label_four.setText("")
        self.admin_label_five.setText("")
        self.admin_label_six.setText("")
        self.admin_label_seven.setText("")
        self.admin_label_eight.setText("")
        self.admin_label_nine.setText("")
        self.admin_label_infoedit.setText(QCoreApplication.translate("MainWindow", u" \uc815\ubcf4 \uc218\uc815", None))
        self.admin_label_game.setText(QCoreApplication.translate("MainWindow", u"  \uc810\uc2ec \ub8f0\ub81b", None))
        self.admin_btn_log.setText("")
        self.admin_label_log.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8 \ubcf4\uae30", None))
        self.admin_btn_server.setText("")
        self.admin_label_server.setText(QCoreApplication.translate("MainWindow", u"\uc11c\ubc84 \uc815\ubcf4", None))
        self.log_btn_back.setText("")
        self.log_label_leftback.setText("")
        self.log_label_title.setText(QCoreApplication.translate("MainWindow", u"\uc11c\ubc84 \ub85c\uadf8 \ubaa9\ub85d", None))
        self.log_label_rightback.setText("")
        self.serverstate_label_back.setText("")
        self.serverstate_label_topback.setText("")
        self.serverstate_label_toptitle.setText(QCoreApplication.translate("MainWindow", u"Memory (\uba54\ubaa8\ub9ac)", None))
        self.serverstate_label_midback.setText("")
        self.serverstate_label_midtitle.setText(QCoreApplication.translate("MainWindow", u"Number of users (\uc0ac\uc6a9\uc790 \uc218)", None))
        self.serverstate_label_botback.setText("")
        self.serverstate_label_bottomtitle.setText(QCoreApplication.translate("MainWindow", u"Packets per minute (\ubd84\ub2f9 \ud328\ud0b7 \uc218)", None))
        self.serverstate_btn_back.setText("")
        self.serverstate_btn_reload.setText("")
        self.serverstate_btn_grafana.setText("")
        self.qrlogin_label_waiting.setText("")
        self.qrlogin_btn_back.setText("")
        self.qrlogin_label_back.setText("")
        self.signup_label_back.setText("")
        self.signup_input_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.signup_input_pw.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.signup_input_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.signup_input_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.signup_input_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.signup_btn_submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.signup_checkbox_agree.setText("")
        self.signup_label_useagree.setText(QCoreApplication.translate("MainWindow", u"\uc774\uc6a9\uc57d\uad00", None))
        self.signup_label_infoagree.setText(QCoreApplication.translate("MainWindow", u"\uac1c\uc778\uc815\ubcf4 \uc218\uc9d1 \ubc0f \uc774\uc6a9\uc5d0 \ubaa8\ub450 \ub3d9\uc758\ud569\ub2c8\ub2e4.", None))
        self.signup_btn_back.setText("")
        self.useredit_label_back.setText("")
        self.useredit_label_title.setText("")
        self.useredit_label_upline.setText("")
        self.useredit_label_id.setText(QCoreApplication.translate("MainWindow", u"\uc544\uc774\ub514", None))
        self.useredit_label_name.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub984", None))
        self.useredit_label_phone.setText(QCoreApplication.translate("MainWindow", u"\ud734\ub300\uc804\ud654", None))
        self.useredit_label_email.setText(QCoreApplication.translate("MainWindow", u"\uc774\uba54\uc77c", None))
        self.useredit_label_downline.setText("")
        self.useredit_btn_back.setText("")
        self.useredit_btn_reset.setText(QCoreApplication.translate("MainWindow", u"\ucd08\uae30\ud654", None))
        self.useredit_btn_send.setText(QCoreApplication.translate("MainWindow", u"\ud655\uc778", None))
        self.useredit_combo_dept.setItemText(0, QCoreApplication.translate("MainWindow", u"\ubd80\uc11c\ub97c \uc120\ud0dd\ud558\uc138\uc694.", None))
        self.useredit_combo_dept.setItemText(1, QCoreApplication.translate("MainWindow", u" 1\ud300", None))
        self.useredit_combo_dept.setItemText(2, QCoreApplication.translate("MainWindow", u" 2\ud300", None))
        self.useredit_combo_dept.setItemText(3, QCoreApplication.translate("MainWindow", u" 3\ud300", None))
        self.useredit_combo_dept.setItemText(4, QCoreApplication.translate("MainWindow", u" \uc194\ub8e8\uc158\ud300", None))

        self.useredit_combo_dept.setCurrentText(QCoreApplication.translate("MainWindow", u"\ubd80\uc11c\ub97c \uc120\ud0dd\ud558\uc138\uc694.", None))
        self.useredit_combo_position.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc9c1\uae09\uc744 \uc120\ud0dd\ud558\uc138\uc694.", None))
        self.useredit_combo_position.setItemText(1, QCoreApplication.translate("MainWindow", u"\ud68c\uc7a5", None))
        self.useredit_combo_position.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc0ac\uc7a5", None))
        self.useredit_combo_position.setItemText(3, QCoreApplication.translate("MainWindow", u"\ucc28\uc7a5", None))
        self.useredit_combo_position.setItemText(4, QCoreApplication.translate("MainWindow", u"\uacfc\uc7a5", None))
        self.useredit_combo_position.setItemText(5, QCoreApplication.translate("MainWindow", u"\ub300\ub9ac", None))
        self.useredit_combo_position.setItemText(6, QCoreApplication.translate("MainWindow", u"\uc0ac\uc6d0", None))

        self.useredit_combo_position.setCurrentText(QCoreApplication.translate("MainWindow", u"\uc9c1\uae09\uc744 \uc120\ud0dd\ud558\uc138\uc694.", None))
        self.useredit_combo_role.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc5ed\ud560\uc744 \uc120\ud0dd\ud558\uc138\uc694.", None))
        self.useredit_combo_role.setItemText(1, QCoreApplication.translate("MainWindow", u"0", None))
        self.useredit_combo_role.setItemText(2, QCoreApplication.translate("MainWindow", u"1", None))

        self.useredit_combo_role.setCurrentText(QCoreApplication.translate("MainWindow", u"\uc5ed\ud560\uc744 \uc120\ud0dd\ud558\uc138\uc694.", None))
        self.useredit_combo_tps.setItemText(0, QCoreApplication.translate("MainWindow", u"tps\ub97c \uc120\ud0dd\ud558\uc138\uc694.", None))
        self.useredit_combo_tps.setItemText(1, QCoreApplication.translate("MainWindow", u"5", None))
        self.useredit_combo_tps.setItemText(2, QCoreApplication.translate("MainWindow", u"30", None))
        self.useredit_combo_tps.setItemText(3, QCoreApplication.translate("MainWindow", u"100", None))

        self.useredit_combo_tps.setCurrentText(QCoreApplication.translate("MainWindow", u"tps\ub97c \uc120\ud0dd\ud558\uc138\uc694.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u2705 \ud68c\uc6d0 \ubaa9\ub85d", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

