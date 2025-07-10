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
        self.stackedWidget_type = QStackedWidget(self.frame_active)
        self.stackedWidget_type.setObjectName(u"stackedWidget_type")
        self.page_shots = QWidget()
        self.page_shots.setObjectName(u"page_shots")
        self.verticalLayout_4 = QVBoxLayout(self.page_shots)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_name = QFrame(self.page_shots)
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

        self.lineEdit_sequence = QLineEdit(self.frame_name)
        self.lineEdit_sequence.setObjectName(u"lineEdit_sequence")
        self.lineEdit_sequence.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setFamily(u"Quicksand")
        font1.setPointSize(10)
        self.lineEdit_sequence.setFont(font1)
        self.lineEdit_sequence.setStyleSheet(u"color:#8B94A4;")
        self.lineEdit_sequence.setEchoMode(QLineEdit.Normal)
        self.lineEdit_sequence.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_sequence)

        self.label_2 = QLabel(self.frame_name)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:#8B94A4;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_shot = QLineEdit(self.frame_name)
        self.lineEdit_shot.setObjectName(u"lineEdit_shot")
        self.lineEdit_shot.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_shot.setFont(font1)
        self.lineEdit_shot.setStyleSheet(u"color:#8B94A4;")
        self.lineEdit_shot.setEchoMode(QLineEdit.Normal)
        self.lineEdit_shot.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_shot)


        self.verticalLayout_4.addWidget(self.frame_name)

        self.stackedWidget_type.addWidget(self.page_shots)
        self.page_assets = QWidget()
        self.page_assets.setObjectName(u"page_assets")
        self.verticalLayout_5 = QVBoxLayout(self.page_assets)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_name_assets = QFrame(self.page_assets)
        self.frame_name_assets.setObjectName(u"frame_name_assets")
        self.frame_name_assets.setFrameShape(QFrame.NoFrame)
        self.frame_name_assets.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_name_assets)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_assets = QLabel(self.frame_name_assets)
        self.label_assets.setObjectName(u"label_assets")
        self.label_assets.setFont(font)
        self.label_assets.setStyleSheet(u"color:#8B94A4;")
        self.label_assets.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_assets)

        self.lineEdit_assets = QLineEdit(self.frame_name_assets)
        self.lineEdit_assets.setObjectName(u"lineEdit_assets")
        self.lineEdit_assets.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_assets.setFont(font1)
        self.lineEdit_assets.setStyleSheet(u"color:#8B94A4;")
        self.lineEdit_assets.setEchoMode(QLineEdit.Normal)
        self.lineEdit_assets.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_assets)


        self.verticalLayout_5.addWidget(self.frame_name_assets)

        self.stackedWidget_type.addWidget(self.page_assets)

        self.verticalLayout_3.addWidget(self.stackedWidget_type)

        self.frame_btns = QFrame(self.frame_active)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_create = QPushButton(self.frame_btns)
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

        self.horizontalLayout_5.addWidget(self.btn_create)

        self.btn_close = QPushButton(self.frame_btns)
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

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.verticalLayout_3.addWidget(self.frame_btns)


        self.verticalLayout_2.addWidget(self.frame_active)


        self.verticalLayout.addWidget(self.frame_main)


        self.retranslateUi(Dialog)

        self.stackedWidget_type.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lab_name_2.setText(QCoreApplication.translate("Dialog", u"PIPELIAM DIALOG BOX", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"SEQUENCE :", None))
        self.lineEdit_sequence.setText(QCoreApplication.translate("Dialog", u"my_sequence", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"SHOT :", None))
        self.lineEdit_shot.setText(QCoreApplication.translate("Dialog", u"my_shot", None))
        self.label_assets.setText(QCoreApplication.translate("Dialog", u"FOLDER : ", None))
        self.lineEdit_assets.setText(QCoreApplication.translate("Dialog", u"my_folder", None))
        self.btn_create.setText(QCoreApplication.translate("Dialog", u"Create folder", None))
        self.btn_close.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

