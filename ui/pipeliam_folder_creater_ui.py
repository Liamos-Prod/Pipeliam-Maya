# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pipeliam_folder_type_creater.ui'
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
        Dialog.resize(400, 200)
        Dialog.setMinimumSize(QSize(400, 200))
        Dialog.setMaximumSize(QSize(800, 200))
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
        self.frame_main.setStyleSheet(u"background-color: #414752;")
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
        self.frame_name = QFrame(self.frame_active)
        self.frame_name.setObjectName(u"frame_name")
        self.frame_name.setFrameShape(QFrame.NoFrame)
        self.frame_name.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_name)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_name)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Quicksand")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:#8B94A4;")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_file_name = QLineEdit(self.frame_name)
        self.lineEdit_file_name.setObjectName(u"lineEdit_file_name")
        self.lineEdit_file_name.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setFamily(u"Quicksand")
        font1.setPointSize(10)
        self.lineEdit_file_name.setFont(font1)
        self.lineEdit_file_name.setStyleSheet(u"color:#8B94A4;")
        self.lineEdit_file_name.setEchoMode(QLineEdit.Normal)
        self.lineEdit_file_name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_file_name)

        self.label_2 = QLabel(self.frame_name)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:#8B94A4;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_file_name_2 = QLineEdit(self.frame_name)
        self.lineEdit_file_name_2.setObjectName(u"lineEdit_file_name_2")
        self.lineEdit_file_name_2.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_file_name_2.setFont(font1)
        self.lineEdit_file_name_2.setStyleSheet(u"color:#8B94A4;")
        self.lineEdit_file_name_2.setEchoMode(QLineEdit.Normal)
        self.lineEdit_file_name_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_file_name_2)


        self.verticalLayout_3.addWidget(self.frame_name)

        self.frame_btn = QFrame(self.frame_active)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setFrameShape(QFrame.NoFrame)
        self.frame_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_btn)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_create = QPushButton(self.frame_btn)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setFont(font1)
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
        self.btn_close.setFont(font1)
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
        self.label.setText(QCoreApplication.translate("Dialog", u"SEQUENCE :", None))
        self.lineEdit_file_name.setText(QCoreApplication.translate("Dialog", u"my_sequence", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"SHOT :", None))
        self.lineEdit_file_name_2.setText(QCoreApplication.translate("Dialog", u"my_shot", None))
        self.btn_create.setText(QCoreApplication.translate("Dialog", u"Create folder", None))
        self.btn_close.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

