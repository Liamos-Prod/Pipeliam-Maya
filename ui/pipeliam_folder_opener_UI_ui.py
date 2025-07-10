# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pipeliam_folder_opener_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 430)
        Dialog.setMinimumSize(QSize(0, 0))
        Dialog.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(Dialog)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 40))
        self.frame_top.setStyleSheet(u"background-color: #313134;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_text_2 = QFrame(self.frame_top)
        self.frame_text_2.setObjectName(u"frame_text_2")
        self.frame_text_2.setFrameShape(QFrame.NoFrame)
        self.frame_text_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_text_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.lab_name_2 = QLabel(self.frame_text_2)
        self.lab_name_2.setObjectName(u"lab_name_2")
        self.lab_name_2.setStyleSheet(u"font: 63 20pt \"Quicksand SemiBold\";\n"
"color : #414752")
        self.lab_name_2.setFrameShadow(QFrame.Raised)
        self.lab_name_2.setTextFormat(Qt.AutoText)
        self.lab_name_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lab_name_2.setMargin(0)

        self.horizontalLayout_6.addWidget(self.lab_name_2)


        self.horizontalLayout.addWidget(self.frame_text_2)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_main = QFrame(Dialog)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u".QFrame {\n"
"    background-color:#414752;\n"
"}")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_active = QFrame(self.frame_main)
        self.frame_active.setObjectName(u"frame_active")
        self.frame_active.setFrameShape(QFrame.NoFrame)
        self.frame_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_active)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_folders = QFrame(self.frame_active)
        self.frame_folders.setObjectName(u"frame_folders")
        self.frame_folders.setStyleSheet(u"")
        self.frame_folders.setFrameShape(QFrame.NoFrame)
        self.frame_folders.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_folders)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollA_folders = QScrollArea(self.frame_folders)
        self.scrollA_folders.setObjectName(u"scrollA_folders")
        self.scrollA_folders.setAutoFillBackground(False)
        self.scrollA_folders.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: #313134;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: #8B94A4;\n"
"	min-height: 30px;\n"
"	margin: 0 3px 0 3px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color:  #FFF;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color:  #FFF;\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color:#313134;\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: #313134;\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
""
                        "	subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}")
        self.scrollA_folders.setFrameShape(QFrame.NoFrame)
        self.scrollA_folders.setFrameShadow(QFrame.Sunken)
        self.scrollA_folders.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollA_folders.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollA_folders.setWidgetResizable(True)
        self.scrollAWC_folders = QWidget()
        self.scrollAWC_folders.setObjectName(u"scrollAWC_folders")
        self.scrollAWC_folders.setGeometry(QRect(0, 0, 368, 518))
        self.scrollAWC_folders.setStyleSheet(u"background-color:#414752;\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.scrollAWC_folders)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.listView_folders = QListView(self.scrollAWC_folders)
        self.listView_folders.setObjectName(u"listView_folders")
        self.listView_folders.setMinimumSize(QSize(0, 500))
        font = QFont()
        font.setFamily(u"Quicksand")
        font.setPointSize(10)
        self.listView_folders.setFont(font)
        self.listView_folders.setStyleSheet(u"background-color: #313134;")
        self.listView_folders.setFrameShape(QFrame.NoFrame)
        self.listView_folders.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listView_folders.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listView_folders.setViewMode(QListView.ListMode)
        self.listView_folders.setModelColumn(0)

        self.verticalLayout_4.addWidget(self.listView_folders)

        self.scrollA_folders.setWidget(self.scrollAWC_folders)

        self.horizontalLayout_2.addWidget(self.scrollA_folders)


        self.verticalLayout_3.addWidget(self.frame_folders)

        self.frame_btn = QFrame(self.frame_active)
        self.frame_btn.setObjectName(u"frame_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_btn.sizePolicy().hasHeightForWidth())
        self.frame_btn.setSizePolicy(sizePolicy)
        self.frame_btn.setFrameShape(QFrame.NoFrame)
        self.frame_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_btn)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_create = QPushButton(self.frame_btn)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setFont(font)
        self.btn_create.setStyleSheet(u"QPushButton{\n"
"	background-color:#8B94A4;\n"
"	color:#414752;\n"
"	border-radius:7px;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#FFF;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color:#FFF;\n"
"	background-color:#000000;\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_create)

        self.btn_close = QPushButton(self.frame_btn)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setFont(font)
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	background-color:#8B94A4;\n"
"	color:#414752;\n"
"	border-radius:7px;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#FFF;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color:#FFF;\n"
"	background-color:#000000;\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_close)


        self.verticalLayout_3.addWidget(self.frame_btn)


        self.verticalLayout_2.addWidget(self.frame_active)


        self.verticalLayout.addWidget(self.frame_main)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lab_name_2.setText(QCoreApplication.translate("Dialog", u"PIPELIAM DIALOG BOX", None))
        self.btn_create.setText(QCoreApplication.translate("Dialog", u"Open Folder", None))
        self.btn_close.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

