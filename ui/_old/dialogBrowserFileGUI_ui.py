# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogBrowserFileGUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ressource_rc

class Ui_dialogBrowserFileGUI(object):
    def setupUi(self, dialogBrowserFileGUI):
        if not dialogBrowserFileGUI.objectName():
            dialogBrowserFileGUI.setObjectName(u"dialogBrowserFileGUI")
        dialogBrowserFileGUI.resize(400, 300)
        dialogBrowserFileGUI.setStyleSheet(u"QPushButton{\n"
"	font: 500 12pt \"Quicksand\";\n"
"	color:#414752;\n"
"}\n"
"\n"
"QLabel{\n"
"	font: 500 12pt \"Quicksand\";\n"
"	color:#414752;\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"	font: 500 12pt \"Quicksand\";\n"
"	color:#414752;\n"
"}")
        self.verticalLayout = QVBoxLayout(dialogBrowserFileGUI)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_dialog = QFrame(dialogBrowserFileGUI)
        self.frame_dialog.setObjectName(u"frame_dialog")
        self.frame_dialog.setStyleSheet(u"background-color: #414752;")
        self.frame_dialog.setFrameShape(QFrame.NoFrame)
        self.frame_dialog.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_dialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fram_lab = QFrame(self.frame_dialog)
        self.fram_lab.setObjectName(u"fram_lab")
        self.fram_lab.setMaximumSize(QSize(16777215, 30))
        self.fram_lab.setStyleSheet(u"background-color: #313134;")
        self.fram_lab.setFrameShape(QFrame.NoFrame)
        self.fram_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.fram_lab)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 0, 0, 0)
        self.lab_pipeliam = QLabel(self.fram_lab)
        self.lab_pipeliam.setObjectName(u"lab_pipeliam")
        self.lab_pipeliam.setStyleSheet(u"font: 63 20pt \"Quicksand SemiBold\";\n"
"color : #414752")
        self.lab_pipeliam.setFrameShadow(QFrame.Raised)
        self.lab_pipeliam.setTextFormat(Qt.AutoText)
        self.lab_pipeliam.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lab_pipeliam.setMargin(0)

        self.verticalLayout_4.addWidget(self.lab_pipeliam)


        self.verticalLayout_2.addWidget(self.fram_lab)

        self.frame_active = QFrame(self.frame_dialog)
        self.frame_active.setObjectName(u"frame_active")
        self.frame_active.setFrameShape(QFrame.NoFrame)
        self.frame_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_active)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_newProject_name = QFrame(self.frame_active)
        self.frame_newProject_name.setObjectName(u"frame_newProject_name")
        font = QFont()
        font.setFamily(u"Quicksand")
        font.setPointSize(12)
        self.frame_newProject_name.setFont(font)
        self.frame_newProject_name.setStyleSheet(u"QFrame{background-color:#626A79;border-radius:25px}")
        self.frame_newProject_name.setFrameShape(QFrame.NoFrame)
        self.frame_newProject_name.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_newProject_name)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_newProject_name)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color:transparent;")
        self.page_create_folder = QWidget()
        self.page_create_folder.setObjectName(u"page_create_folder")
        self.page_create_folder.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.page_create_folder)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_browse = QFrame(self.page_create_folder)
        self.frame_browse.setObjectName(u"frame_browse")
        self.frame_browse.setFrameShape(QFrame.StyledPanel)
        self.frame_browse.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_browse)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lab_path_to_folder = QLabel(self.frame_browse)
        self.lab_path_to_folder.setObjectName(u"lab_path_to_folder")
        self.lab_path_to_folder.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lab_path_to_folder)

        self.btn_browse_folder = QPushButton(self.frame_browse)
        self.btn_browse_folder.setObjectName(u"btn_browse_folder")
        self.btn_browse_folder.setStyleSheet(u"QPushButton{\n"
"	font: 500 12pt \"Quicksand\";\n"
"	color:#414752;\n"
"	background-color : #8B94A4;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#FFF\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:#000000;\n"
"	color:#FFF;\n"
"	icon:url(:/icons/icons/folder_h.png);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_browse_folder.setIcon(icon)
        self.btn_browse_folder.setIconSize(QSize(20, 20))

        self.verticalLayout_7.addWidget(self.btn_browse_folder)


        self.verticalLayout_6.addWidget(self.frame_browse)

        self.frame_name = QFrame(self.page_create_folder)
        self.frame_name.setObjectName(u"frame_name")
        self.frame_name.setFont(font)
        self.frame_name.setFrameShape(QFrame.StyledPanel)
        self.frame_name.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_name)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pte_name = QPlainTextEdit(self.frame_name)
        self.pte_name.setObjectName(u"pte_name")
        self.pte_name.setMaximumSize(QSize(250, 30))
        self.pte_name.setStyleSheet(u"background-color:#313134;\n"
"border-radius:10px;\n"
"color:#8B94A4;\n"
"")
        self.pte_name.setFrameShape(QFrame.NoFrame)
        self.pte_name.setReadOnly(False)
        self.pte_name.setCenterOnScroll(False)

        self.horizontalLayout.addWidget(self.pte_name)

        self.btn_create = QPushButton(self.frame_name)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setStyleSheet(u"QPushButton{\n"
"	font: 500 12pt \"Quicksand\";\n"
"	color:#414752;\n"
"	background-color : #8B94A4;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#FFF\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:#000000;\n"
"	color:#FFF;\n"
"	icon:url(:/icons/icons/correct_h.png);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/correct.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_create.setIcon(icon1)
        self.btn_create.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_create)


        self.verticalLayout_6.addWidget(self.frame_name)

        self.stackedWidget.addWidget(self.page_create_folder)
        self.page_open_folder = QWidget()
        self.page_open_folder.setObjectName(u"page_open_folder")
        self.stackedWidget.addWidget(self.page_open_folder)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.frame_newProject_name)


        self.verticalLayout_2.addWidget(self.frame_active)


        self.verticalLayout.addWidget(self.frame_dialog)


        self.retranslateUi(dialogBrowserFileGUI)

        QMetaObject.connectSlotsByName(dialogBrowserFileGUI)
    # setupUi

    def retranslateUi(self, dialogBrowserFileGUI):
        dialogBrowserFileGUI.setWindowTitle(QCoreApplication.translate("dialogBrowserFileGUI", u"Dialog", None))
        self.lab_pipeliam.setText(QCoreApplication.translate("dialogBrowserFileGUI", u"PIPELIAM", None))
        self.lab_path_to_folder.setText(QCoreApplication.translate("dialogBrowserFileGUI", u"path/to/your/folder", None))
        self.btn_browse_folder.setText(QCoreApplication.translate("dialogBrowserFileGUI", u"Browse", None))
        self.pte_name.setPlainText(QCoreApplication.translate("dialogBrowserFileGUI", u"Your_root_folder_name", None))
        self.btn_create.setText("")
    # retranslateUi

