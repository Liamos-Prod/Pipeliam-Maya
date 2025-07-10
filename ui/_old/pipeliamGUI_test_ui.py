# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pipeliamGUI_test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ressource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(815, 1565)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 40))
        self.frame_top.setStyleSheet(u"background-color: #313134;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_text = QFrame(self.frame_top)
        self.frame_text.setObjectName(u"frame_text")
        self.frame_text.setFrameShape(QFrame.NoFrame)
        self.frame_text.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_text)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.lab_name = QLabel(self.frame_text)
        self.lab_name.setObjectName(u"lab_name")
        self.lab_name.setStyleSheet(u"font: 63 20pt \"Quicksand SemiBold\";\n"
"color : #414752")
        self.lab_name.setFrameShadow(QFrame.Raised)
        self.lab_name.setTextFormat(Qt.AutoText)
        self.lab_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lab_name.setMargin(0)

        self.horizontalLayout_2.addWidget(self.lab_name)


        self.horizontalLayout.addWidget(self.frame_text)


        self.verticalLayout_2.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setStyleSheet(u"background-color: #414752;")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.frame_menu_bar = QFrame(self.frame_center)
        self.frame_menu_bar.setObjectName(u"frame_menu_bar")
        self.frame_menu_bar.setMinimumSize(QSize(0, 0))
        self.frame_menu_bar.setMaximumSize(QSize(50, 16777215))
        self.frame_menu_bar.setStyleSheet(u"background-color:#313134;\n"
"border-radius: 5px;")
        self.frame_menu_bar.setFrameShape(QFrame.NoFrame)
        self.frame_menu_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_menu_bar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.icon_menu = QPushButton(self.frame_menu_bar)
        self.icon_menu.setObjectName(u"icon_menu")
        self.icon_menu.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    icon: url(:/icons/icons/categories_h.png);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/categories.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_menu.setIcon(icon)
        self.icon_menu.setIconSize(QSize(30, 30))
        self.icon_menu.setFlat(True)

        self.verticalLayout_3.addWidget(self.icon_menu)

        self.vs_9 = QSpacerItem(20, 158, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.vs_9)

        self.icon_user = QPushButton(self.frame_menu_bar)
        self.icon_user.setObjectName(u"icon_user")
        self.icon_user.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    icon: url(:/icons/icons/user_h.png);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_user.setIcon(icon1)
        self.icon_user.setIconSize(QSize(33, 33))
        self.icon_user.setFlat(True)

        self.verticalLayout_3.addWidget(self.icon_user)

        self.vs_10 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.vs_10)

        self.icon_infos = QPushButton(self.frame_menu_bar)
        self.icon_infos.setObjectName(u"icon_infos")
        self.icon_infos.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    icon: url(:/icons/icons/infos_h.png);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/infos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_infos.setIcon(icon2)
        self.icon_infos.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.icon_infos)

        self.vs_11 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.vs_11)


        self.horizontalLayout_4.addWidget(self.frame_menu_bar)

        self.frame_menu = QFrame(self.frame_center)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(0, 0))
        self.frame_menu.setMaximumSize(QSize(100, 16777215))
        self.frame_menu.setStyleSheet(u"")
        self.frame_menu.setFrameShape(QFrame.NoFrame)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.vs_1 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.vs_1)

        self.frame_menu_background = QFrame(self.frame_menu)
        self.frame_menu_background.setObjectName(u"frame_menu_background")
        self.frame_menu_background.setStyleSheet(u"background-color : #626A79;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;")
        self.frame_menu_background.setFrameShape(QFrame.NoFrame)
        self.frame_menu_background.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_menu_background)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_menu_home = QFrame(self.frame_menu_background)
        self.frame_menu_home.setObjectName(u"frame_menu_home")
        self.frame_menu_home.setFrameShape(QFrame.StyledPanel)
        self.frame_menu_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_menu_home)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.icon_home = QPushButton(self.frame_menu_home)
        self.icon_home.setObjectName(u"icon_home")
        font = QFont()
        font.setFamily(u"Quicksand")
        font.setPointSize(16)
        self.icon_home.setFont(font)
        self.icon_home.setToolTipDuration(-1)
        self.icon_home.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"	color:#FFF\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    icon: url(:/icons/icons/home_h.png);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_home.setIcon(icon3)
        self.icon_home.setIconSize(QSize(60, 60))

        self.verticalLayout_13.addWidget(self.icon_home)


        self.verticalLayout_6.addWidget(self.frame_menu_home)

        self.vs_8 = QSpacerItem(20, 36, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.vs_8)

        self.frame_menu_projectM = QFrame(self.frame_menu_background)
        self.frame_menu_projectM.setObjectName(u"frame_menu_projectM")
        self.frame_menu_projectM.setStyleSheet(u"QFrame {\n"
"	background-color:transparent\n"
"}")
        self.frame_menu_projectM.setFrameShape(QFrame.NoFrame)
        self.frame_menu_projectM.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_menu_projectM)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.icon_projectM = QPushButton(self.frame_menu_projectM)
        self.icon_projectM.setObjectName(u"icon_projectM")
        self.icon_projectM.setEnabled(True)
        self.icon_projectM.setFont(font)
        self.icon_projectM.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    icon: url(:/icons/icons/folder_h.png);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_projectM.setIcon(icon4)
        self.icon_projectM.setIconSize(QSize(60, 60))

        self.verticalLayout_7.addWidget(self.icon_projectM)


        self.verticalLayout_6.addWidget(self.frame_menu_projectM)

        self.vs_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.vs_3)

        self.frame_menu_modelTools = QFrame(self.frame_menu_background)
        self.frame_menu_modelTools.setObjectName(u"frame_menu_modelTools")
        self.frame_menu_modelTools.setFrameShape(QFrame.StyledPanel)
        self.frame_menu_modelTools.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_menu_modelTools)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.icon_modelTools = QPushButton(self.frame_menu_modelTools)
        self.icon_modelTools.setObjectName(u"icon_modelTools")
        self.icon_modelTools.setFont(font)
        self.icon_modelTools.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    icon: url(:/icons/icons/modeling_h.png);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/modeling.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_modelTools.setIcon(icon5)
        self.icon_modelTools.setIconSize(QSize(60, 60))

        self.verticalLayout_8.addWidget(self.icon_modelTools)


        self.verticalLayout_6.addWidget(self.frame_menu_modelTools)

        self.vs_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.vs_4)

        self.frame_menu_textureTools = QFrame(self.frame_menu_background)
        self.frame_menu_textureTools.setObjectName(u"frame_menu_textureTools")
        self.frame_menu_textureTools.setFrameShape(QFrame.StyledPanel)
        self.frame_menu_textureTools.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_menu_textureTools)
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.icon_textureTools = QPushButton(self.frame_menu_textureTools)
        self.icon_textureTools.setObjectName(u"icon_textureTools")
        self.icon_textureTools.setFont(font)
        self.icon_textureTools.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    icon: url(:/icons/icons/paint_roller_h.png);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/paint_roller.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_textureTools.setIcon(icon6)
        self.icon_textureTools.setIconSize(QSize(60, 60))

        self.verticalLayout_9.addWidget(self.icon_textureTools)


        self.verticalLayout_6.addWidget(self.frame_menu_textureTools)

        self.vs_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.vs_5)

        self.frame_menu_animTools = QFrame(self.frame_menu_background)
        self.frame_menu_animTools.setObjectName(u"frame_menu_animTools")
        self.frame_menu_animTools.setFrameShape(QFrame.StyledPanel)
        self.frame_menu_animTools.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_menu_animTools)
        self.verticalLayout_10.setSpacing(3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.icon_animTools = QPushButton(self.frame_menu_animTools)
        self.icon_animTools.setObjectName(u"icon_animTools")
        self.icon_animTools.setFont(font)
        self.icon_animTools.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    icon: url(:/icons/icons/slow_motion_h.png);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/slow_motion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_animTools.setIcon(icon7)
        self.icon_animTools.setIconSize(QSize(60, 60))
        self.icon_animTools.setAutoDefault(False)
        self.icon_animTools.setFlat(False)

        self.verticalLayout_10.addWidget(self.icon_animTools)


        self.verticalLayout_6.addWidget(self.frame_menu_animTools)

        self.vs_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.vs_6)

        self.frame_menu_renderTools = QFrame(self.frame_menu_background)
        self.frame_menu_renderTools.setObjectName(u"frame_menu_renderTools")
        self.frame_menu_renderTools.setFrameShape(QFrame.StyledPanel)
        self.frame_menu_renderTools.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_menu_renderTools)
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.icon_renderTools = QPushButton(self.frame_menu_renderTools)
        self.icon_renderTools.setObjectName(u"icon_renderTools")
        self.icon_renderTools.setFont(font)
        self.icon_renderTools.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    icon: url(:/icons/icons/camera_h.png);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_renderTools.setIcon(icon8)
        self.icon_renderTools.setIconSize(QSize(60, 60))

        self.verticalLayout_11.addWidget(self.icon_renderTools)


        self.verticalLayout_6.addWidget(self.frame_menu_renderTools)

        self.vs_7 = QSpacerItem(20, 36, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.vs_7)

        self.frame_menu_importExportTools = QFrame(self.frame_menu_background)
        self.frame_menu_importExportTools.setObjectName(u"frame_menu_importExportTools")
        self.frame_menu_importExportTools.setFrameShape(QFrame.StyledPanel)
        self.frame_menu_importExportTools.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_menu_importExportTools)
        self.verticalLayout_12.setSpacing(3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.icon_importExportTools = QPushButton(self.frame_menu_importExportTools)
        self.icon_importExportTools.setObjectName(u"icon_importExportTools")
        self.icon_importExportTools.setFont(font)
        self.icon_importExportTools.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    icon: url(:/icons/icons/export_h.png);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_importExportTools.setIcon(icon9)
        self.icon_importExportTools.setIconSize(QSize(60, 60))

        self.verticalLayout_12.addWidget(self.icon_importExportTools)


        self.verticalLayout_6.addWidget(self.frame_menu_importExportTools)


        self.verticalLayout_4.addWidget(self.frame_menu_background)

        self.vs_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.vs_2)


        self.horizontalLayout_4.addWidget(self.frame_menu)

        self.frame_active = QFrame(self.frame_center)
        self.frame_active.setObjectName(u"frame_active")
        self.frame_active.setStyleSheet(u"")
        self.frame_active.setFrameShape(QFrame.NoFrame)
        self.frame_active.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_active)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_stackedW_active = QFrame(self.frame_active)
        self.frame_stackedW_active.setObjectName(u"frame_stackedW_active")
        self.frame_stackedW_active.setStyleSheet(u"QFrame{background-color:#626A79;border-radius:25px}")
        self.frame_stackedW_active.setFrameShape(QFrame.NoFrame)
        self.frame_stackedW_active.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_stackedW_active)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.stackedW_pages = QStackedWidget(self.frame_stackedW_active)
        self.stackedW_pages.setObjectName(u"stackedW_pages")
        self.stackedW_pages.setEnabled(True)
        self.stackedW_pages.setMaximumSize(QSize(16777215, 16777215))
        self.stackedW_pages.setStyleSheet(u"background-color:transparent;")
        self.stackedW_pages.setFrameShadow(QFrame.Raised)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"")
        self.verticalLayout_15 = QVBoxLayout(self.page_home)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_home = QFrame(self.page_home)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setFrameShape(QFrame.StyledPanel)
        self.frame_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_home)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_home_title = QFrame(self.frame_home)
        self.frame_home_title.setObjectName(u"frame_home_title")
        self.frame_home_title.setMaximumSize(QSize(16777215, 90))
        self.frame_home_title.setFrameShape(QFrame.StyledPanel)
        self.frame_home_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_home_title)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.hs_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.hs_7)

        self.icon_lab_home_2 = QPushButton(self.frame_home_title)
        self.icon_lab_home_2.setObjectName(u"icon_lab_home_2")
        self.icon_lab_home_2.setMaximumSize(QSize(81, 81))
        self.icon_lab_home_2.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    background-color:transparent;\n"
"	border:none;\n"
"}")
        self.icon_lab_home_2.setIcon(icon4)
        self.icon_lab_home_2.setIconSize(QSize(80, 80))
        self.icon_lab_home_2.setFlat(True)

        self.horizontalLayout_7.addWidget(self.icon_lab_home_2)

        self.lab_home_2 = QLabel(self.frame_home_title)
        self.lab_home_2.setObjectName(u"lab_home_2")
        self.lab_home_2.setMaximumSize(QSize(16777215, 150))
        font1 = QFont()
        font1.setFamily(u"Quicksand")
        font1.setPointSize(40)
        font1.setBold(False)
        font1.setWeight(50)
        self.lab_home_2.setFont(font1)
        self.lab_home_2.setStyleSheet(u"background-color:transparent;color:#414752;")
        self.lab_home_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lab_home_2)

        self.hs_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.hs_8)


        self.verticalLayout_14.addWidget(self.frame_home_title)

        self.frame_home_active = QFrame(self.frame_home)
        self.frame_home_active.setObjectName(u"frame_home_active")
        self.frame_home_active.setLayoutDirection(Qt.LeftToRight)
        self.frame_home_active.setFrameShape(QFrame.NoFrame)
        self.frame_home_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_home_active)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.scrollA_home = QScrollArea(self.frame_home_active)
        self.scrollA_home.setObjectName(u"scrollA_home")
        self.scrollA_home.setStyleSheet(u" QScrollBar:vertical {\n"
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
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.scrollA_home.setFrameShape(QFrame.NoFrame)
        self.scrollA_home.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollA_home.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollA_home.setWidgetResizable(True)
        self.scrollAWC_home = QWidget()
        self.scrollAWC_home.setObjectName(u"scrollAWC_home")
        self.scrollAWC_home.setGeometry(QRect(0, 0, 525, 1303))
        self.scrollAWC_home.setMinimumSize(QSize(0, 0))
        self.scrollAWC_home.setStyleSheet(u"")
        self.verticalLayout_23 = QVBoxLayout(self.scrollAWC_home)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_scroll_home = QFrame(self.scrollAWC_home)
        self.frame_scroll_home.setObjectName(u"frame_scroll_home")
        self.frame_scroll_home.setMinimumSize(QSize(0, 1200))
        self.frame_scroll_home.setMaximumSize(QSize(16777215, 16777215))
        self.frame_scroll_home.setFrameShape(QFrame.NoFrame)
        self.frame_scroll_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_scroll_home)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(9, 0, -1, -1)
        self.frame_newProject = QFrame(self.frame_scroll_home)
        self.frame_newProject.setObjectName(u"frame_newProject")
        self.frame_newProject.setFrameShape(QFrame.NoFrame)
        self.frame_newProject.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_newProject)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.icon_newProject = QPushButton(self.frame_newProject)
        self.icon_newProject.setObjectName(u"icon_newProject")
        self.icon_newProject.setFont(font)
        self.icon_newProject.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    icon: url(:/icons/icons/folder_h.png);\n"
"	color:transparent;\n"
"	border:none\n"
"}")
        self.icon_newProject.setIcon(icon4)
        self.icon_newProject.setIconSize(QSize(100, 100))

        self.verticalLayout_17.addWidget(self.icon_newProject)

        self.btn_newProject = QPushButton(self.frame_newProject)
        self.btn_newProject.setObjectName(u"btn_newProject")
        self.btn_newProject.setFont(font)
        self.btn_newProject.setStyleSheet(u"QPushButton{\n"
"	background-color:#8B94A4;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	border-width: 5px;\n"
"	border-radius: 17px;\n"
"	margin-left : 60px;\n"
"	margin-right : 60px;\n"
"	color:#414752;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#313134;\n"
"	background-color:#FFF;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:#313134;\n"
"	color:#FFF;	\n"
"}")
        self.btn_newProject.setIconSize(QSize(60, 60))

        self.verticalLayout_17.addWidget(self.btn_newProject)


        self.verticalLayout_24.addWidget(self.frame_newProject)

        self.frame_openProject = QFrame(self.frame_scroll_home)
        self.frame_openProject.setObjectName(u"frame_openProject")
        self.frame_openProject.setFrameShape(QFrame.NoFrame)
        self.frame_openProject.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_openProject)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.icon_openProject = QPushButton(self.frame_openProject)
        self.icon_openProject.setObjectName(u"icon_openProject")
        self.icon_openProject.setFont(font)
        self.icon_openProject.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    icon: url(:/icons/icons/folder_h.png);\n"
"	color:transparent;\n"
"	border:none\n"
"}")
        self.icon_openProject.setIcon(icon4)
        self.icon_openProject.setIconSize(QSize(100, 100))

        self.verticalLayout_16.addWidget(self.icon_openProject)

        self.bnt_openProject = QPushButton(self.frame_openProject)
        self.bnt_openProject.setObjectName(u"bnt_openProject")
        self.bnt_openProject.setFont(font)
        self.bnt_openProject.setStyleSheet(u"QPushButton{\n"
"	background-color:#8B94A4;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	border-width: 5px;\n"
"	border-radius: 17px;\n"
"	margin-left : 60px;\n"
"	margin-right : 60px;\n"
"	color:#414752;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#313134;\n"
"	background-color:#FFF;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:#313134;\n"
"	color:#FFF;	\n"
"}")

        self.verticalLayout_16.addWidget(self.bnt_openProject)


        self.verticalLayout_24.addWidget(self.frame_openProject)

        self.frame_lastProject = QFrame(self.frame_scroll_home)
        self.frame_lastProject.setObjectName(u"frame_lastProject")
        self.frame_lastProject.setStyleSheet(u"")
        self.frame_lastProject.setFrameShape(QFrame.NoFrame)
        self.frame_lastProject.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_lastProject)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.icon_lastProject = QPushButton(self.frame_lastProject)
        self.icon_lastProject.setObjectName(u"icon_lastProject")
        self.icon_lastProject.setFont(font)
        self.icon_lastProject.setStyleSheet(u"/* Normal state */\n"
"QPushButton#icon_lastProject {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton#icon_lastProject:hover {\n"
"    icon: url(:/icons/icons/folder_h.png);\n"
"	color:transparent;\n"
"	border:none\n"
"}")
        self.icon_lastProject.setIcon(icon4)
        self.icon_lastProject.setIconSize(QSize(100, 100))

        self.verticalLayout_18.addWidget(self.icon_lastProject)

        self.btn_lastProject = QPushButton(self.frame_lastProject)
        self.btn_lastProject.setObjectName(u"btn_lastProject")
        self.btn_lastProject.setMaximumSize(QSize(16777215, 16777215))
        self.btn_lastProject.setFont(font)
        self.btn_lastProject.setStyleSheet(u"QPushButton#btn_lastProject{\n"
"	background-color:#8B94A4;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	border-width: 5px;\n"
"	border-radius: 17px;\n"
"	margin-left : 60px;\n"
"	margin-right : 60px;\n"
"	color:#414752;\n"
"}\n"
"QPushButton#btn_lastProject:hover{\n"
"	color:#313134;\n"
"	background-color:#FFF;\n"
"}\n"
"QPushButton#btn_lastProject:pressed{\n"
"	background-color:#313134;\n"
"	color:#FFF;	\n"
"}")

        self.verticalLayout_18.addWidget(self.btn_lastProject)


        self.verticalLayout_24.addWidget(self.frame_lastProject)


        self.verticalLayout_23.addWidget(self.frame_scroll_home)

        self.scrollA_home.setWidget(self.scrollAWC_home)

        self.verticalLayout_22.addWidget(self.scrollA_home)


        self.verticalLayout_14.addWidget(self.frame_home_active)


        self.verticalLayout_15.addWidget(self.frame_home)

        self.stackedW_pages.addWidget(self.page_home)
        self.page_projectM = QWidget()
        self.page_projectM.setObjectName(u"page_projectM")
        self.page_projectM.setStyleSheet(u"")
        self.verticalLayout_19 = QVBoxLayout(self.page_projectM)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_projetM = QFrame(self.page_projectM)
        self.frame_projetM.setObjectName(u"frame_projetM")
        self.frame_projetM.setMaximumSize(QSize(16777215, 80))
        self.frame_projetM.setFrameShape(QFrame.NoFrame)
        self.frame_projetM.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_projetM)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.hs_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.hs_3)

        self.icon_lab_projectM = QPushButton(self.frame_projetM)
        self.icon_lab_projectM.setObjectName(u"icon_lab_projectM")
        self.icon_lab_projectM.setMaximumSize(QSize(81, 81))
        self.icon_lab_projectM.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    background-color:transparent;\n"
"	border:none;\n"
"}")
        self.icon_lab_projectM.setIcon(icon4)
        self.icon_lab_projectM.setIconSize(QSize(80, 80))
        self.icon_lab_projectM.setFlat(True)

        self.horizontalLayout_8.addWidget(self.icon_lab_projectM)

        self.lab_projectM = QLabel(self.frame_projetM)
        self.lab_projectM.setObjectName(u"lab_projectM")
        self.lab_projectM.setMaximumSize(QSize(16777215, 150))
        self.lab_projectM.setFont(font1)
        self.lab_projectM.setStyleSheet(u"background-color:transparent;color:#414752;")
        self.lab_projectM.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lab_projectM)

        self.lab_projectM_project = QLabel(self.frame_projetM)
        self.lab_projectM_project.setObjectName(u"lab_projectM_project")
        self.lab_projectM_project.setMaximumSize(QSize(16777215, 150))
        self.lab_projectM_project.setFont(font1)
        self.lab_projectM_project.setStyleSheet(u"background-color:transparent;color:#414752;")
        self.lab_projectM_project.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lab_projectM_project)

        self.hs_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.hs_4)


        self.verticalLayout_19.addWidget(self.frame_projetM)

        self.frame_projectM_active = QFrame(self.page_projectM)
        self.frame_projectM_active.setObjectName(u"frame_projectM_active")
        self.frame_projectM_active.setFrameShape(QFrame.StyledPanel)
        self.frame_projectM_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_projectM_active)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_projectM_type = QFrame(self.frame_projectM_active)
        self.frame_projectM_type.setObjectName(u"frame_projectM_type")
        self.frame_projectM_type.setMaximumSize(QSize(16777215, 55))
        self.frame_projectM_type.setFrameShape(QFrame.StyledPanel)
        self.frame_projectM_type.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_projectM_type)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.hs_5 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.hs_5)

        self.frame_projectM_type_btn = QFrame(self.frame_projectM_type)
        self.frame_projectM_type_btn.setObjectName(u"frame_projectM_type_btn")
        self.frame_projectM_type_btn.setStyleSheet(u"QFrame{\n"
"	background-color:#313134;\n"
"	border-radius:18px;\n"
"}")
        self.frame_projectM_type_btn.setFrameShape(QFrame.NoFrame)
        self.frame_projectM_type_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_projectM_type_btn)
        self.horizontalLayout_10.setSpacing(40)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(23, -1, 23, -1)
        self.btn_assets = QPushButton(self.frame_projectM_type_btn)
        self.btn_assets.setObjectName(u"btn_assets")
        font2 = QFont()
        font2.setFamily(u"Quicksand")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_assets.setFont(font2)
        self.btn_assets.setStyleSheet(u"QPushButton{\n"
"	color:#8B94A4;\n"
"	background-color:transparent;\n"
"	border:none\n"
"}\n"
"QPushButton:checked{\n"
"	color:#FFF;\n"
"}")
        self.btn_assets.setCheckable(True)
        self.btn_assets.setChecked(True)

        self.horizontalLayout_10.addWidget(self.btn_assets)

        self.btn_shots = QPushButton(self.frame_projectM_type_btn)
        self.btn_shots.setObjectName(u"btn_shots")
        self.btn_shots.setFont(font2)
        self.btn_shots.setStyleSheet(u"QPushButton{\n"
"	color:#8B94A4;\n"
"	background-color:transparent;\n"
"	border:none\n"
"}\n"
"QPushButton:checked{\n"
"	color:#FFF;\n"
"}")
        self.btn_shots.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.btn_shots)


        self.horizontalLayout_9.addWidget(self.frame_projectM_type_btn)

        self.hs_6 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.hs_6)


        self.verticalLayout_20.addWidget(self.frame_projectM_type)

        self.stackedW_projectM = QStackedWidget(self.frame_projectM_active)
        self.stackedW_projectM.setObjectName(u"stackedW_projectM")
        self.stackedW_projectM.setFrameShadow(QFrame.Raised)
        self.page_assets = QWidget()
        self.page_assets.setObjectName(u"page_assets")
        self.verticalLayout_36 = QVBoxLayout(self.page_assets)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.scrollA_assets = QScrollArea(self.page_assets)
        self.scrollA_assets.setObjectName(u"scrollA_assets")
        self.scrollA_assets.setStyleSheet(u" QScrollBar:vertical {\n"
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
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.scrollA_assets.setFrameShape(QFrame.NoFrame)
        self.scrollA_assets.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollA_assets.setWidgetResizable(True)
        self.scrollAW_assets = QWidget()
        self.scrollAW_assets.setObjectName(u"scrollAW_assets")
        self.scrollAW_assets.setGeometry(QRect(0, 0, 525, 1292))
        self.verticalLayout_26 = QVBoxLayout(self.scrollAW_assets)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_assets_active = QFrame(self.scrollAW_assets)
        self.frame_assets_active.setObjectName(u"frame_assets_active")
        self.frame_assets_active.setFrameShape(QFrame.NoFrame)
        self.frame_assets_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_assets_active)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_assets = QFrame(self.frame_assets_active)
        self.frame_assets.setObjectName(u"frame_assets")
        self.frame_assets.setMaximumSize(QSize(16777215, 16777215))
        self.frame_assets.setFrameShape(QFrame.NoFrame)
        self.frame_assets.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_assets)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_assets_assets_lab = QFrame(self.frame_assets)
        self.frame_assets_assets_lab.setObjectName(u"frame_assets_assets_lab")
        self.frame_assets_assets_lab.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setFamily(u"Quicksand")
        font3.setPointSize(12)
        self.frame_assets_assets_lab.setFont(font3)
        self.frame_assets_assets_lab.setFrameShape(QFrame.NoFrame)
        self.frame_assets_assets_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_assets_assets_lab)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.lab_assets = QPushButton(self.frame_assets_assets_lab)
        self.lab_assets.setObjectName(u"lab_assets")
        self.lab_assets.setFont(font2)
        self.lab_assets.setStyleSheet(u"QPushButton{\n"
"	background-color:#313134;\n"
"	color:#8B94A4;\n"
"	border-radius:10px;\n"
"	margin-left:30px;\n"
"	margin-right:30px;\n"
"}")

        self.verticalLayout_31.addWidget(self.lab_assets)


        self.verticalLayout_30.addWidget(self.frame_assets_assets_lab)

        self.frame_assets_scrol = QFrame(self.frame_assets)
        self.frame_assets_scrol.setObjectName(u"frame_assets_scrol")
        self.frame_assets_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_assets_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_assets_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_assets_scrol)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_assets_scrol_btn = QFrame(self.frame_assets_scrol)
        self.frame_assets_scrol_btn.setObjectName(u"frame_assets_scrol_btn")
        self.frame_assets_scrol_btn.setMaximumSize(QSize(16777215, 40))
        self.frame_assets_scrol_btn.setStyleSheet(u"QFrame{\n"
"	background-color:#313134;\n"
"	border-radius:15px;\n"
"	margin-left:30px;\n"
"	margin-right:30px;\n"
"}\n"
"QPushButton{\n"
"	color:#8B94A4;\n"
"	background-color:transparent;\n"
"	border:none;\n"
"}\n"
"QPushButton:checked{\n"
"	color:#FFF;\n"
"	background-color:transparent;\n"
"	border:none;\n"
"}")
        self.frame_assets_scrol_btn.setFrameShape(QFrame.NoFrame)
        self.frame_assets_scrol_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_assets_scrol_btn)
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_characters = QPushButton(self.frame_assets_scrol_btn)
        self.btn_characters.setObjectName(u"btn_characters")
        font4 = QFont()
        font4.setFamily(u"Quicksand")
        font4.setPointSize(14)
        self.btn_characters.setFont(font4)
        self.btn_characters.setCheckable(True)
        self.btn_characters.setChecked(True)

        self.horizontalLayout_13.addWidget(self.btn_characters)

        self.btn_props = QPushButton(self.frame_assets_scrol_btn)
        self.btn_props.setObjectName(u"btn_props")
        self.btn_props.setFont(font4)
        self.btn_props.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.btn_props)

        self.btn_sets = QPushButton(self.frame_assets_scrol_btn)
        self.btn_sets.setObjectName(u"btn_sets")
        self.btn_sets.setFont(font4)
        self.btn_sets.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.btn_sets)


        self.verticalLayout_32.addWidget(self.frame_assets_scrol_btn)

        self.stackedW_assets = QStackedWidget(self.frame_assets_scrol)
        self.stackedW_assets.setObjectName(u"stackedW_assets")
        self.page_characters = QWidget()
        self.page_characters.setObjectName(u"page_characters")
        self.verticalLayout_33 = QVBoxLayout(self.page_characters)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_characters_scrol_active = QFrame(self.page_characters)
        self.frame_characters_scrol_active.setObjectName(u"frame_characters_scrol_active")
        self.frame_characters_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_characters_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_characters_scrol_active)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.scrollA_characters = QScrollArea(self.frame_characters_scrol_active)
        self.scrollA_characters.setObjectName(u"scrollA_characters")
        self.scrollA_characters.setStyleSheet(u" QScrollBar:vertical {\n"
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
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.scrollA_characters.setFrameShadow(QFrame.Raised)
        self.scrollA_characters.setWidgetResizable(True)
        self.scrollAWC_characters = QWidget()
        self.scrollAWC_characters.setObjectName(u"scrollAWC_characters")
        self.scrollAWC_characters.setGeometry(QRect(0, -480, 403, 1218))
        self.verticalLayout_34 = QVBoxLayout(self.scrollAWC_characters)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.listView_characters = QListView(self.scrollAWC_characters)
        self.listView_characters.setObjectName(u"listView_characters")
        self.listView_characters.setMinimumSize(QSize(0, 1200))
        self.listView_characters.setStyleSheet(u"")
        self.listView_characters.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_34.addWidget(self.listView_characters)

        self.scrollA_characters.setWidget(self.scrollAWC_characters)

        self.verticalLayout_105.addWidget(self.scrollA_characters)


        self.verticalLayout_33.addWidget(self.frame_characters_scrol_active)

        self.stackedW_assets.addWidget(self.page_characters)
        self.page_props = QWidget()
        self.page_props.setObjectName(u"page_props")
        self.verticalLayout_106 = QVBoxLayout(self.page_props)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.frame_props_scrol_active = QFrame(self.page_props)
        self.frame_props_scrol_active.setObjectName(u"frame_props_scrol_active")
        self.frame_props_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_props_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.frame_props_scrol_active)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.scrollA_props = QScrollArea(self.frame_props_scrol_active)
        self.scrollA_props.setObjectName(u"scrollA_props")
        self.scrollA_props.setStyleSheet(u" QScrollBar:vertical {\n"
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
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.scrollA_props.setFrameShadow(QFrame.Raised)
        self.scrollA_props.setWidgetResizable(True)
        self.scrollAWC_props = QWidget()
        self.scrollAWC_props.setObjectName(u"scrollAWC_props")
        self.scrollAWC_props.setGeometry(QRect(0, 0, 86, 1218))
        self.verticalLayout_108 = QVBoxLayout(self.scrollAWC_props)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.listView_props = QListView(self.scrollAWC_props)
        self.listView_props.setObjectName(u"listView_props")
        self.listView_props.setMinimumSize(QSize(0, 1200))
        self.listView_props.setStyleSheet(u"")
        self.listView_props.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_108.addWidget(self.listView_props)

        self.scrollA_props.setWidget(self.scrollAWC_props)

        self.verticalLayout_107.addWidget(self.scrollA_props)


        self.verticalLayout_106.addWidget(self.frame_props_scrol_active)

        self.stackedW_assets.addWidget(self.page_props)
        self.page_sets = QWidget()
        self.page_sets.setObjectName(u"page_sets")
        self.verticalLayout_109 = QVBoxLayout(self.page_sets)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.frame_sets_scrol_active = QFrame(self.page_sets)
        self.frame_sets_scrol_active.setObjectName(u"frame_sets_scrol_active")
        self.frame_sets_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_sets_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_110 = QVBoxLayout(self.frame_sets_scrol_active)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.scrollA_sets = QScrollArea(self.frame_sets_scrol_active)
        self.scrollA_sets.setObjectName(u"scrollA_sets")
        self.scrollA_sets.setStyleSheet(u" QScrollBar:vertical {\n"
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
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.scrollA_sets.setFrameShadow(QFrame.Raised)
        self.scrollA_sets.setWidgetResizable(True)
        self.scrollAWC_sets = QWidget()
        self.scrollAWC_sets.setObjectName(u"scrollAWC_sets")
        self.scrollAWC_sets.setGeometry(QRect(0, 0, 86, 1218))
        self.verticalLayout_111 = QVBoxLayout(self.scrollAWC_sets)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.listView_sets = QListView(self.scrollAWC_sets)
        self.listView_sets.setObjectName(u"listView_sets")
        self.listView_sets.setMinimumSize(QSize(0, 1200))
        self.listView_sets.setStyleSheet(u"")
        self.listView_sets.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_111.addWidget(self.listView_sets)

        self.scrollA_sets.setWidget(self.scrollAWC_sets)

        self.verticalLayout_110.addWidget(self.scrollA_sets)


        self.verticalLayout_109.addWidget(self.frame_sets_scrol_active)

        self.stackedW_assets.addWidget(self.page_sets)

        self.verticalLayout_32.addWidget(self.stackedW_assets)


        self.verticalLayout_30.addWidget(self.frame_assets_scrol)

        self.frame_assets_btn = QFrame(self.frame_assets)
        self.frame_assets_btn.setObjectName(u"frame_assets_btn")
        self.frame_assets_btn.setMaximumSize(QSize(16777215, 55))
        self.frame_assets_btn.setFrameShape(QFrame.NoFrame)
        self.frame_assets_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_assets_btn)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, -1, -1, -1)
        self.btn_add_assets = QPushButton(self.frame_assets_btn)
        self.btn_add_assets.setObjectName(u"btn_add_assets")
        self.btn_add_assets.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    icon: url(:/icons/icons/add_h.png);\n"
"	border:none;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_assets.setIcon(icon10)
        self.btn_add_assets.setIconSize(QSize(40, 40))

        self.verticalLayout_35.addWidget(self.btn_add_assets)


        self.verticalLayout_30.addWidget(self.frame_assets_btn)


        self.verticalLayout_21.addWidget(self.frame_assets)

        self.frame_stage = QFrame(self.frame_assets_active)
        self.frame_stage.setObjectName(u"frame_stage")
        self.frame_stage.setMaximumSize(QSize(16777215, 16777215))
        self.frame_stage.setFrameShape(QFrame.NoFrame)
        self.frame_stage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_stage)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.frame_stage_lab = QFrame(self.frame_stage)
        self.frame_stage_lab.setObjectName(u"frame_stage_lab")
        self.frame_stage_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_stage_lab.setFrameShape(QFrame.NoFrame)
        self.frame_stage_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_stage_lab)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.lab_stage = QPushButton(self.frame_stage_lab)
        self.lab_stage.setObjectName(u"lab_stage")
        self.lab_stage.setFont(font2)
        self.lab_stage.setStyleSheet(u"QPushButton{\n"
"	background-color:#313134;\n"
"	color:#8B94A4;\n"
"	border-radius:10px;\n"
"	margin-left:30px;\n"
"	margin-right:30px;\n"
"}")

        self.verticalLayout_65.addWidget(self.lab_stage)


        self.verticalLayout_62.addWidget(self.frame_stage_lab)

        self.frame_stage_scrol = QFrame(self.frame_stage)
        self.frame_stage_scrol.setObjectName(u"frame_stage_scrol")
        self.frame_stage_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_stage_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_stage_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_stage_scrol)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.frame_stage_scrol_active = QFrame(self.frame_stage_scrol)
        self.frame_stage_scrol_active.setObjectName(u"frame_stage_scrol_active")
        self.frame_stage_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_stage_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_stage_scrol_active)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.scrollA_stage = QScrollArea(self.frame_stage_scrol_active)
        self.scrollA_stage.setObjectName(u"scrollA_stage")
        self.scrollA_stage.setStyleSheet(u" QScrollBar:vertical {\n"
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
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.scrollA_stage.setFrameShadow(QFrame.Raised)
        self.scrollA_stage.setWidgetResizable(True)
        self.scrollAWC_stage = QWidget()
        self.scrollAWC_stage.setObjectName(u"scrollAWC_stage")
        self.scrollAWC_stage.setGeometry(QRect(0, 0, 421, 1218))
        self.verticalLayout_70 = QVBoxLayout(self.scrollAWC_stage)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.listView_stage = QListView(self.scrollAWC_stage)
        self.listView_stage.setObjectName(u"listView_stage")
        self.listView_stage.setMinimumSize(QSize(0, 1200))
        self.listView_stage.setStyleSheet(u"")

        self.verticalLayout_70.addWidget(self.listView_stage)

        self.scrollA_stage.setWidget(self.scrollAWC_stage)

        self.verticalLayout_69.addWidget(self.scrollA_stage)


        self.verticalLayout_68.addWidget(self.frame_stage_scrol_active)


        self.verticalLayout_62.addWidget(self.frame_stage_scrol)

        self.frame_stage_btn = QFrame(self.frame_stage)
        self.frame_stage_btn.setObjectName(u"frame_stage_btn")
        self.frame_stage_btn.setMaximumSize(QSize(16777215, 55))
        self.frame_stage_btn.setFrameShape(QFrame.NoFrame)
        self.frame_stage_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_stage_btn)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, -1, -1, -1)
        self.btn_add_stage = QPushButton(self.frame_stage_btn)
        self.btn_add_stage.setObjectName(u"btn_add_stage")
        self.btn_add_stage.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    icon: url(:/icons/icons/add_h.png);\n"
"	border:none;\n"
"}")
        self.btn_add_stage.setIcon(icon10)
        self.btn_add_stage.setIconSize(QSize(40, 40))

        self.verticalLayout_71.addWidget(self.btn_add_stage)


        self.verticalLayout_62.addWidget(self.frame_stage_btn)


        self.verticalLayout_21.addWidget(self.frame_stage)

        self.frame_assets_version = QFrame(self.frame_assets_active)
        self.frame_assets_version.setObjectName(u"frame_assets_version")
        self.frame_assets_version.setFrameShape(QFrame.NoFrame)
        self.frame_assets_version.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_assets_version)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.frame_assets_version_lab = QFrame(self.frame_assets_version)
        self.frame_assets_version_lab.setObjectName(u"frame_assets_version_lab")
        self.frame_assets_version_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_assets_version_lab.setFrameShape(QFrame.NoFrame)
        self.frame_assets_version_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_assets_version_lab)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.lab_assets_version = QPushButton(self.frame_assets_version_lab)
        self.lab_assets_version.setObjectName(u"lab_assets_version")
        self.lab_assets_version.setFont(font2)
        self.lab_assets_version.setStyleSheet(u"QPushButton{\n"
"	background-color:#313134;\n"
"	color:#8B94A4;\n"
"	border-radius:10px;\n"
"	margin-left:30px;\n"
"	margin-right:30px;\n"
"}")

        self.verticalLayout_73.addWidget(self.lab_assets_version)


        self.verticalLayout_72.addWidget(self.frame_assets_version_lab)

        self.frame_assets_version_scrol = QFrame(self.frame_assets_version)
        self.frame_assets_version_scrol.setObjectName(u"frame_assets_version_scrol")
        self.frame_assets_version_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_assets_version_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_assets_version_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_assets_version_scrol)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.frame_assets_version_scrol_active = QFrame(self.frame_assets_version_scrol)
        self.frame_assets_version_scrol_active.setObjectName(u"frame_assets_version_scrol_active")
        self.frame_assets_version_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_assets_version_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_assets_version_scrol_active)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.scrollA_assets_version = QScrollArea(self.frame_assets_version_scrol_active)
        self.scrollA_assets_version.setObjectName(u"scrollA_assets_version")
        self.scrollA_assets_version.setStyleSheet(u" QScrollBar:vertical {\n"
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
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.scrollA_assets_version.setFrameShadow(QFrame.Raised)
        self.scrollA_assets_version.setWidgetResizable(True)
        self.scrollAWC_assets_version = QWidget()
        self.scrollAWC_assets_version.setObjectName(u"scrollAWC_assets_version")
        self.scrollAWC_assets_version.setGeometry(QRect(0, 0, 421, 1218))
        self.verticalLayout_76 = QVBoxLayout(self.scrollAWC_assets_version)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.listView_assets_version = QListView(self.scrollAWC_assets_version)
        self.listView_assets_version.setObjectName(u"listView_assets_version")
        self.listView_assets_version.setMinimumSize(QSize(0, 1200))
        self.listView_assets_version.setStyleSheet(u"")

        self.verticalLayout_76.addWidget(self.listView_assets_version)

        self.scrollA_assets_version.setWidget(self.scrollAWC_assets_version)

        self.verticalLayout_75.addWidget(self.scrollA_assets_version)


        self.verticalLayout_74.addWidget(self.frame_assets_version_scrol_active)


        self.verticalLayout_72.addWidget(self.frame_assets_version_scrol)

        self.frame_assets_version_btn = QFrame(self.frame_assets_version)
        self.frame_assets_version_btn.setObjectName(u"frame_assets_version_btn")
        self.frame_assets_version_btn.setMinimumSize(QSize(0, 55))
        self.frame_assets_version_btn.setMaximumSize(QSize(16777215, 55))
        self.frame_assets_version_btn.setFrameShape(QFrame.NoFrame)
        self.frame_assets_version_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_assets_version_btn)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, -1, -1, -1)

        self.verticalLayout_72.addWidget(self.frame_assets_version_btn)


        self.verticalLayout_21.addWidget(self.frame_assets_version)

        self.frame_assets_publish_comment = QFrame(self.frame_assets_active)
        self.frame_assets_publish_comment.setObjectName(u"frame_assets_publish_comment")
        self.frame_assets_publish_comment.setFrameShape(QFrame.NoFrame)
        self.frame_assets_publish_comment.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_assets_publish_comment)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(-1, 0, -1, 0)
        self.frame_assets_publish = QFrame(self.frame_assets_publish_comment)
        self.frame_assets_publish.setObjectName(u"frame_assets_publish")
        self.frame_assets_publish.setMinimumSize(QSize(0, 200))
        self.frame_assets_publish.setFrameShape(QFrame.NoFrame)
        self.frame_assets_publish.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_assets_publish)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, -1, 0, -1)
        self.frame_assets_publish_lab = QFrame(self.frame_assets_publish)
        self.frame_assets_publish_lab.setObjectName(u"frame_assets_publish_lab")
        self.frame_assets_publish_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_assets_publish_lab.setFrameShape(QFrame.NoFrame)
        self.frame_assets_publish_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_assets_publish_lab)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.lab_assets_publish = QPushButton(self.frame_assets_publish_lab)
        self.lab_assets_publish.setObjectName(u"lab_assets_publish")
        self.lab_assets_publish.setFont(font2)
        self.lab_assets_publish.setStyleSheet(u"QPushButton{\n"
"	background-color:#313134;\n"
"	color:#8B94A4;\n"
"	border-radius:10px;\n"
"	margin-left:30px;\n"
"	margin-right:30px;\n"
"}")

        self.verticalLayout_80.addWidget(self.lab_assets_publish)


        self.verticalLayout_79.addWidget(self.frame_assets_publish_lab)

        self.frame_assets_publish_scrol = QFrame(self.frame_assets_publish)
        self.frame_assets_publish_scrol.setObjectName(u"frame_assets_publish_scrol")
        self.frame_assets_publish_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_assets_publish_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_assets_publish_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_assets_publish_scrol)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, -1, 0, -1)
        self.frame_assets_publish_scrol_active = QFrame(self.frame_assets_publish_scrol)
        self.frame_assets_publish_scrol_active.setObjectName(u"frame_assets_publish_scrol_active")
        self.frame_assets_publish_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_assets_publish_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_assets_publish_scrol_active)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")

        self.verticalLayout_81.addWidget(self.frame_assets_publish_scrol_active)


        self.verticalLayout_79.addWidget(self.frame_assets_publish_scrol)


        self.verticalLayout_78.addWidget(self.frame_assets_publish)

        self.frame_assets_comment = QFrame(self.frame_assets_publish_comment)
        self.frame_assets_comment.setObjectName(u"frame_assets_comment")
        self.frame_assets_comment.setFrameShape(QFrame.StyledPanel)
        self.frame_assets_comment.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_assets_comment)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, -1, 0, -1)
        self.frame_assets_comment_lab = QFrame(self.frame_assets_comment)
        self.frame_assets_comment_lab.setObjectName(u"frame_assets_comment_lab")
        self.frame_assets_comment_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_assets_comment_lab.setFrameShape(QFrame.NoFrame)
        self.frame_assets_comment_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_assets_comment_lab)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.lab_assets_comment = QPushButton(self.frame_assets_comment_lab)
        self.lab_assets_comment.setObjectName(u"lab_assets_comment")
        self.lab_assets_comment.setFont(font2)
        self.lab_assets_comment.setStyleSheet(u"QPushButton{\n"
"	background-color:#313134;\n"
"	color:#8B94A4;\n"
"	border-radius:10px;\n"
"	margin-left:30px;\n"
"	margin-right:30px;\n"
"}")

        self.verticalLayout_84.addWidget(self.lab_assets_comment)


        self.verticalLayout_83.addWidget(self.frame_assets_comment_lab)

        self.frame_assets_comment_scrol = QFrame(self.frame_assets_comment)
        self.frame_assets_comment_scrol.setObjectName(u"frame_assets_comment_scrol")
        self.frame_assets_comment_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_assets_comment_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_assets_comment_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_assets_comment_scrol)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.frame_assets_comment_scrol_active = QFrame(self.frame_assets_comment_scrol)
        self.frame_assets_comment_scrol_active.setObjectName(u"frame_assets_comment_scrol_active")
        self.frame_assets_comment_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_assets_comment_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_assets_comment_scrol_active)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.scrollA_assets_comment = QScrollArea(self.frame_assets_comment_scrol_active)
        self.scrollA_assets_comment.setObjectName(u"scrollA_assets_comment")
        self.scrollA_assets_comment.setStyleSheet(u" QScrollBar:vertical {\n"
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
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.scrollA_assets_comment.setFrameShadow(QFrame.Raised)
        self.scrollA_assets_comment.setWidgetResizable(True)
        self.scrollAWC_assets_comment = QWidget()
        self.scrollAWC_assets_comment.setObjectName(u"scrollAWC_assets_comment")
        self.scrollAWC_assets_comment.setGeometry(QRect(0, 0, 421, 1218))
        self.verticalLayout_87 = QVBoxLayout(self.scrollAWC_assets_comment)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.plainTextEdit = QPlainTextEdit(self.scrollAWC_assets_comment)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(0, 1200))
        font5 = QFont()
        font5.setFamily(u"Quicksand")
        font5.setPointSize(10)
        self.plainTextEdit.setFont(font5)
        self.plainTextEdit.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_87.addWidget(self.plainTextEdit)

        self.scrollA_assets_comment.setWidget(self.scrollAWC_assets_comment)

        self.verticalLayout_86.addWidget(self.scrollA_assets_comment)


        self.verticalLayout_85.addWidget(self.frame_assets_comment_scrol_active)


        self.verticalLayout_83.addWidget(self.frame_assets_comment_scrol)

        self.frame_assets_comment_btn = QFrame(self.frame_assets_comment)
        self.frame_assets_comment_btn.setObjectName(u"frame_assets_comment_btn")
        self.frame_assets_comment_btn.setMaximumSize(QSize(16777215, 55))
        self.frame_assets_comment_btn.setFrameShape(QFrame.NoFrame)
        self.frame_assets_comment_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_assets_comment_btn)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, -1, -1, -1)
        self.btn_add_assets_comment = QPushButton(self.frame_assets_comment_btn)
        self.btn_add_assets_comment.setObjectName(u"btn_add_assets_comment")
        self.btn_add_assets_comment.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    icon: url(:/icons/icons/correct_h.png);\n"
"	border:none;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/correct.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_assets_comment.setIcon(icon11)
        self.btn_add_assets_comment.setIconSize(QSize(40, 40))

        self.verticalLayout_88.addWidget(self.btn_add_assets_comment)


        self.verticalLayout_83.addWidget(self.frame_assets_comment_btn)


        self.verticalLayout_78.addWidget(self.frame_assets_comment)


        self.verticalLayout_21.addWidget(self.frame_assets_publish_comment)


        self.verticalLayout_26.addWidget(self.frame_assets_active)

        self.scrollA_assets.setWidget(self.scrollAW_assets)

        self.verticalLayout_36.addWidget(self.scrollA_assets)

        self.stackedW_projectM.addWidget(self.page_assets)
        self.page_shots = QWidget()
        self.page_shots.setObjectName(u"page_shots")
        self.verticalLayout_29 = QVBoxLayout(self.page_shots)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.scrollA_shots = QScrollArea(self.page_shots)
        self.scrollA_shots.setObjectName(u"scrollA_shots")
        self.scrollA_shots.setWidgetResizable(True)
        self.scrollAWC_shots = QWidget()
        self.scrollAWC_shots.setObjectName(u"scrollAWC_shots")
        self.scrollAWC_shots.setGeometry(QRect(0, 0, 522, 1228))
        self.verticalLayout_25 = QVBoxLayout(self.scrollAWC_shots)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_shots_active = QFrame(self.scrollAWC_shots)
        self.frame_shots_active.setObjectName(u"frame_shots_active")
        self.frame_shots_active.setFrameShape(QFrame.NoFrame)
        self.frame_shots_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_shots_active)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_shots = QFrame(self.frame_shots_active)
        self.frame_shots.setObjectName(u"frame_shots")
        self.frame_shots.setMaximumSize(QSize(16777215, 16777215))
        self.frame_shots.setFrameShape(QFrame.NoFrame)
        self.frame_shots.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_shots)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.frame_shots_sequences_lab = QFrame(self.frame_shots)
        self.frame_shots_sequences_lab.setObjectName(u"frame_shots_sequences_lab")
        self.frame_shots_sequences_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_shots_sequences_lab.setFont(font3)
        self.frame_shots_sequences_lab.setFrameShape(QFrame.NoFrame)
        self.frame_shots_sequences_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_shots_sequences_lab)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.lab_sequences = QPushButton(self.frame_shots_sequences_lab)
        self.lab_sequences.setObjectName(u"lab_sequences")
        self.lab_sequences.setFont(font2)
        self.lab_sequences.setStyleSheet(u"QPushButton{\n"
"	background-color:#313134;\n"
"	color:#8B94A4;\n"
"	border-radius:10px;\n"
"	margin-left:30px;\n"
"	margin-right:30px;\n"
"}")

        self.verticalLayout_66.addWidget(self.lab_sequences)


        self.verticalLayout_63.addWidget(self.frame_shots_sequences_lab)

        self.frame_sequences_scrol = QFrame(self.frame_shots)
        self.frame_sequences_scrol.setObjectName(u"frame_sequences_scrol")
        self.frame_sequences_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_sequences_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_sequences_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.frame_sequences_scrol)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.frame_sequences_scrol_active = QFrame(self.frame_sequences_scrol)
        self.frame_sequences_scrol_active.setObjectName(u"frame_sequences_scrol_active")
        self.frame_sequences_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_sequences_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_sequences_scrol_active)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.scrollA_sequences = QScrollArea(self.frame_sequences_scrol_active)
        self.scrollA_sequences.setObjectName(u"scrollA_sequences")
        self.scrollA_sequences.setStyleSheet(u" QScrollBar:vertical {\n"
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
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.scrollA_sequences.setFrameShadow(QFrame.Raised)
        self.scrollA_sequences.setWidgetResizable(True)
        self.scrollAWC_sequences = QWidget()
        self.scrollAWC_sequences.setObjectName(u"scrollAWC_sequences")
        self.scrollAWC_sequences.setGeometry(QRect(0, 0, 418, 1218))
        self.verticalLayout_91 = QVBoxLayout(self.scrollAWC_sequences)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.listView_sequences = QListView(self.scrollAWC_sequences)
        self.listView_sequences.setObjectName(u"listView_sequences")
        self.listView_sequences.setMinimumSize(QSize(0, 1200))
        self.listView_sequences.setStyleSheet(u"")

        self.verticalLayout_91.addWidget(self.listView_sequences)

        self.scrollA_sequences.setWidget(self.scrollAWC_sequences)

        self.verticalLayout_90.addWidget(self.scrollA_sequences)


        self.verticalLayout_89.addWidget(self.frame_sequences_scrol_active)


        self.verticalLayout_63.addWidget(self.frame_sequences_scrol)

        self.frame_sequences_btn = QFrame(self.frame_shots)
        self.frame_sequences_btn.setObjectName(u"frame_sequences_btn")
        self.frame_sequences_btn.setMaximumSize(QSize(16777215, 55))
        self.frame_sequences_btn.setFrameShape(QFrame.NoFrame)
        self.frame_sequences_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_sequences_btn)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, -1, -1, -1)
        self.btn_add_sequences = QPushButton(self.frame_sequences_btn)
        self.btn_add_sequences.setObjectName(u"btn_add_sequences")
        self.btn_add_sequences.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    icon: url(:/icons/icons/add_h.png);\n"
"	border:none;\n"
"}")
        self.btn_add_sequences.setIcon(icon10)
        self.btn_add_sequences.setIconSize(QSize(40, 40))

        self.verticalLayout_92.addWidget(self.btn_add_sequences)


        self.verticalLayout_63.addWidget(self.frame_sequences_btn)


        self.verticalLayout_27.addWidget(self.frame_shots)

        self.frame_shots_shots = QFrame(self.frame_shots_active)
        self.frame_shots_shots.setObjectName(u"frame_shots_shots")
        self.frame_shots_shots.setMaximumSize(QSize(16777215, 16777215))
        self.frame_shots_shots.setFrameShape(QFrame.NoFrame)
        self.frame_shots_shots.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_shots_shots)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.frame_shots_lab = QFrame(self.frame_shots_shots)
        self.frame_shots_lab.setObjectName(u"frame_shots_lab")
        self.frame_shots_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_shots_lab.setFrameShape(QFrame.NoFrame)
        self.frame_shots_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_shots_lab)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.lab_shots = QPushButton(self.frame_shots_lab)
        self.lab_shots.setObjectName(u"lab_shots")
        self.lab_shots.setFont(font2)
        self.lab_shots.setStyleSheet(u"QPushButton{\n"
"	background-color:#313134;\n"
"	color:#8B94A4;\n"
"	border-radius:10px;\n"
"	margin-left:30px;\n"
"	margin-right:30px;\n"
"}")

        self.verticalLayout_94.addWidget(self.lab_shots)


        self.verticalLayout_93.addWidget(self.frame_shots_lab)

        self.frame_shots_scrol = QFrame(self.frame_shots_shots)
        self.frame_shots_scrol.setObjectName(u"frame_shots_scrol")
        self.frame_shots_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_shots_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_shots_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_shots_scrol)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.frame_shots_scrol_active = QFrame(self.frame_shots_scrol)
        self.frame_shots_scrol_active.setObjectName(u"frame_shots_scrol_active")
        self.frame_shots_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_shots_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_shots_scrol_active)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.scrollA_shots_list = QScrollArea(self.frame_shots_scrol_active)
        self.scrollA_shots_list.setObjectName(u"scrollA_shots_list")
        self.scrollA_shots_list.setStyleSheet(u" QScrollBar:vertical {\n"
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
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.scrollA_shots_list.setFrameShape(QFrame.NoFrame)
        self.scrollA_shots_list.setFrameShadow(QFrame.Raised)
        self.scrollA_shots_list.setWidgetResizable(True)
        self.scrollAWC_shots_list = QWidget()
        self.scrollAWC_shots_list.setObjectName(u"scrollAWC_shots_list")
        self.scrollAWC_shots_list.setGeometry(QRect(0, 0, 418, 1218))
        self.verticalLayout_99 = QVBoxLayout(self.scrollAWC_shots_list)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.listView_shots = QListView(self.scrollAWC_shots_list)
        self.listView_shots.setObjectName(u"listView_shots")
        self.listView_shots.setMinimumSize(QSize(0, 1200))
        self.listView_shots.setStyleSheet(u"")

        self.verticalLayout_99.addWidget(self.listView_shots)

        self.scrollA_shots_list.setWidget(self.scrollAWC_shots_list)

        self.verticalLayout_98.addWidget(self.scrollA_shots_list)


        self.verticalLayout_97.addWidget(self.frame_shots_scrol_active)


        self.verticalLayout_93.addWidget(self.frame_shots_scrol)

        self.frame_shots_btn = QFrame(self.frame_shots_shots)
        self.frame_shots_btn.setObjectName(u"frame_shots_btn")
        self.frame_shots_btn.setMaximumSize(QSize(16777215, 55))
        self.frame_shots_btn.setFrameShape(QFrame.NoFrame)
        self.frame_shots_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.frame_shots_btn)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(0, -1, -1, -1)
        self.btn_add_shots = QPushButton(self.frame_shots_btn)
        self.btn_add_shots.setObjectName(u"btn_add_shots")
        self.btn_add_shots.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    icon: url(:/icons/icons/add_h.png);\n"
"	border:none;\n"
"}")
        self.btn_add_shots.setIcon(icon10)
        self.btn_add_shots.setIconSize(QSize(40, 40))

        self.verticalLayout_100.addWidget(self.btn_add_shots)


        self.verticalLayout_93.addWidget(self.frame_shots_btn)


        self.verticalLayout_27.addWidget(self.frame_shots_shots)

        self.frame_shots_version = QFrame(self.frame_shots_active)
        self.frame_shots_version.setObjectName(u"frame_shots_version")
        self.frame_shots_version.setMaximumSize(QSize(16777215, 16777215))
        self.frame_shots_version.setFrameShape(QFrame.NoFrame)
        self.frame_shots_version.setFrameShadow(QFrame.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.frame_shots_version)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.frame_shots_version_lab = QFrame(self.frame_shots_version)
        self.frame_shots_version_lab.setObjectName(u"frame_shots_version_lab")
        self.frame_shots_version_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_shots_version_lab.setFrameShape(QFrame.NoFrame)
        self.frame_shots_version_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_shots_version_lab)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.lab_shots_version = QPushButton(self.frame_shots_version_lab)
        self.lab_shots_version.setObjectName(u"lab_shots_version")
        self.lab_shots_version.setFont(font2)
        self.lab_shots_version.setStyleSheet(u"QPushButton{\n"
"	background-color:#313134;\n"
"	color:#8B94A4;\n"
"	border-radius:10px;\n"
"	margin-left:30px;\n"
"	margin-right:30px;\n"
"}")

        self.verticalLayout_102.addWidget(self.lab_shots_version)


        self.verticalLayout_101.addWidget(self.frame_shots_version_lab)

        self.frame_shots_version_scrol = QFrame(self.frame_shots_version)
        self.frame_shots_version_scrol.setObjectName(u"frame_shots_version_scrol")
        self.frame_shots_version_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_shots_version_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_shots_version_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_shots_version_scrol)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.frame_shots_version_scrol_active = QFrame(self.frame_shots_version_scrol)
        self.frame_shots_version_scrol_active.setObjectName(u"frame_shots_version_scrol_active")
        self.frame_shots_version_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_shots_version_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_shots_version_scrol_active)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.scrollA_shots_version = QScrollArea(self.frame_shots_version_scrol_active)
        self.scrollA_shots_version.setObjectName(u"scrollA_shots_version")
        self.scrollA_shots_version.setStyleSheet(u" QScrollBar:vertical {\n"
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
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.scrollA_shots_version.setFrameShadow(QFrame.Raised)
        self.scrollA_shots_version.setWidgetResizable(True)
        self.scrollAWC_shots_version = QWidget()
        self.scrollAWC_shots_version.setObjectName(u"scrollAWC_shots_version")
        self.scrollAWC_shots_version.setGeometry(QRect(0, 0, 418, 1218))
        self.verticalLayout_113 = QVBoxLayout(self.scrollAWC_shots_version)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.listView_shots_version = QListView(self.scrollAWC_shots_version)
        self.listView_shots_version.setObjectName(u"listView_shots_version")
        self.listView_shots_version.setMinimumSize(QSize(0, 1200))
        self.listView_shots_version.setStyleSheet(u"")

        self.verticalLayout_113.addWidget(self.listView_shots_version)

        self.scrollA_shots_version.setWidget(self.scrollAWC_shots_version)

        self.verticalLayout_104.addWidget(self.scrollA_shots_version)


        self.verticalLayout_103.addWidget(self.frame_shots_version_scrol_active)


        self.verticalLayout_101.addWidget(self.frame_shots_version_scrol)

        self.frame_shots_version_btn = QFrame(self.frame_shots_version)
        self.frame_shots_version_btn.setObjectName(u"frame_shots_version_btn")
        self.frame_shots_version_btn.setMinimumSize(QSize(0, 55))
        self.frame_shots_version_btn.setMaximumSize(QSize(16777215, 55))
        self.frame_shots_version_btn.setFrameShape(QFrame.NoFrame)
        self.frame_shots_version_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.frame_shots_version_btn)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, -1, -1, -1)

        self.verticalLayout_101.addWidget(self.frame_shots_version_btn)


        self.verticalLayout_27.addWidget(self.frame_shots_version)

        self.frame_shots_publish_comment = QFrame(self.frame_shots_active)
        self.frame_shots_publish_comment.setObjectName(u"frame_shots_publish_comment")
        self.frame_shots_publish_comment.setFrameShape(QFrame.NoFrame)
        self.frame_shots_publish_comment.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.frame_shots_publish_comment)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(-1, 0, -1, 0)
        self.frame_shots_publish = QFrame(self.frame_shots_publish_comment)
        self.frame_shots_publish.setObjectName(u"frame_shots_publish")
        self.frame_shots_publish.setMinimumSize(QSize(0, 200))
        self.frame_shots_publish.setFrameShape(QFrame.NoFrame)
        self.frame_shots_publish.setFrameShadow(QFrame.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.frame_shots_publish)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.frame_shots_publish_lab = QFrame(self.frame_shots_publish)
        self.frame_shots_publish_lab.setObjectName(u"frame_shots_publish_lab")
        self.frame_shots_publish_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_shots_publish_lab.setFrameShape(QFrame.NoFrame)
        self.frame_shots_publish_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_117 = QVBoxLayout(self.frame_shots_publish_lab)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.lab_shots_publish = QPushButton(self.frame_shots_publish_lab)
        self.lab_shots_publish.setObjectName(u"lab_shots_publish")
        self.lab_shots_publish.setFont(font2)
        self.lab_shots_publish.setStyleSheet(u"QPushButton{\n"
"	background-color:#313134;\n"
"	color:#8B94A4;\n"
"	border-radius:10px;\n"
"	margin-left:30px;\n"
"	margin-right:30px;\n"
"}")

        self.verticalLayout_117.addWidget(self.lab_shots_publish)


        self.verticalLayout_116.addWidget(self.frame_shots_publish_lab)

        self.frame_shots_publish_scrol = QFrame(self.frame_shots_publish)
        self.frame_shots_publish_scrol.setObjectName(u"frame_shots_publish_scrol")
        self.frame_shots_publish_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_shots_publish_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_shots_publish_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_118 = QVBoxLayout(self.frame_shots_publish_scrol)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.frame_shots_publish_scrol_active = QFrame(self.frame_shots_publish_scrol)
        self.frame_shots_publish_scrol_active.setObjectName(u"frame_shots_publish_scrol_active")
        self.frame_shots_publish_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_shots_publish_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_119 = QVBoxLayout(self.frame_shots_publish_scrol_active)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")

        self.verticalLayout_118.addWidget(self.frame_shots_publish_scrol_active)


        self.verticalLayout_116.addWidget(self.frame_shots_publish_scrol)


        self.verticalLayout_115.addWidget(self.frame_shots_publish)

        self.frame_shots_comment = QFrame(self.frame_shots_publish_comment)
        self.frame_shots_comment.setObjectName(u"frame_shots_comment")
        self.frame_shots_comment.setFrameShape(QFrame.StyledPanel)
        self.frame_shots_comment.setFrameShadow(QFrame.Raised)
        self.verticalLayout_120 = QVBoxLayout(self.frame_shots_comment)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.frame_shots_comment_lab = QFrame(self.frame_shots_comment)
        self.frame_shots_comment_lab.setObjectName(u"frame_shots_comment_lab")
        self.frame_shots_comment_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_shots_comment_lab.setFrameShape(QFrame.NoFrame)
        self.frame_shots_comment_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_121 = QVBoxLayout(self.frame_shots_comment_lab)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.lab_shots_comment = QPushButton(self.frame_shots_comment_lab)
        self.lab_shots_comment.setObjectName(u"lab_shots_comment")
        self.lab_shots_comment.setFont(font2)
        self.lab_shots_comment.setStyleSheet(u"QPushButton{\n"
"	background-color:#313134;\n"
"	color:#8B94A4;\n"
"	border-radius:10px;\n"
"	margin-left:30px;\n"
"	margin-right:30px;\n"
"}")

        self.verticalLayout_121.addWidget(self.lab_shots_comment)


        self.verticalLayout_120.addWidget(self.frame_shots_comment_lab)

        self.frame_shots_comment_scrol = QFrame(self.frame_shots_comment)
        self.frame_shots_comment_scrol.setObjectName(u"frame_shots_comment_scrol")
        self.frame_shots_comment_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_shots_comment_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_shots_comment_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_122 = QVBoxLayout(self.frame_shots_comment_scrol)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.frame_shots_comment_scrol_active = QFrame(self.frame_shots_comment_scrol)
        self.frame_shots_comment_scrol_active.setObjectName(u"frame_shots_comment_scrol_active")
        self.frame_shots_comment_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_shots_comment_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_123 = QVBoxLayout(self.frame_shots_comment_scrol_active)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.scrollA_shots_comment = QScrollArea(self.frame_shots_comment_scrol_active)
        self.scrollA_shots_comment.setObjectName(u"scrollA_shots_comment")
        self.scrollA_shots_comment.setStyleSheet(u" QScrollBar:vertical {\n"
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
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.scrollA_shots_comment.setFrameShadow(QFrame.Raised)
        self.scrollA_shots_comment.setWidgetResizable(True)
        self.scrollAWC_shots_comment = QWidget()
        self.scrollAWC_shots_comment.setObjectName(u"scrollAWC_shots_comment")
        self.scrollAWC_shots_comment.setGeometry(QRect(0, 0, 400, 1218))
        self.verticalLayout_124 = QVBoxLayout(self.scrollAWC_shots_comment)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.listView_shots_comment = QListView(self.scrollAWC_shots_comment)
        self.listView_shots_comment.setObjectName(u"listView_shots_comment")
        self.listView_shots_comment.setMinimumSize(QSize(0, 1200))
        self.listView_shots_comment.setStyleSheet(u"")

        self.verticalLayout_124.addWidget(self.listView_shots_comment)

        self.scrollA_shots_comment.setWidget(self.scrollAWC_shots_comment)

        self.verticalLayout_123.addWidget(self.scrollA_shots_comment)


        self.verticalLayout_122.addWidget(self.frame_shots_comment_scrol_active)


        self.verticalLayout_120.addWidget(self.frame_shots_comment_scrol)

        self.frame_shots_comment_btn = QFrame(self.frame_shots_comment)
        self.frame_shots_comment_btn.setObjectName(u"frame_shots_comment_btn")
        self.frame_shots_comment_btn.setMaximumSize(QSize(16777215, 55))
        self.frame_shots_comment_btn.setFrameShape(QFrame.NoFrame)
        self.frame_shots_comment_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_125 = QVBoxLayout(self.frame_shots_comment_btn)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(0, -1, -1, -1)
        self.btn_add_shots_comment = QPushButton(self.frame_shots_comment_btn)
        self.btn_add_shots_comment.setObjectName(u"btn_add_shots_comment")
        self.btn_add_shots_comment.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover { \n"
"	icon: url(:/icons/icons/correct_h.png);\n"
"	border:none;\n"
"}")
        self.btn_add_shots_comment.setIcon(icon11)
        self.btn_add_shots_comment.setIconSize(QSize(40, 40))

        self.verticalLayout_125.addWidget(self.btn_add_shots_comment)


        self.verticalLayout_120.addWidget(self.frame_shots_comment_btn)


        self.verticalLayout_115.addWidget(self.frame_shots_comment)


        self.verticalLayout_27.addWidget(self.frame_shots_publish_comment)


        self.verticalLayout_25.addWidget(self.frame_shots_active)

        self.scrollA_shots.setWidget(self.scrollAWC_shots)

        self.verticalLayout_29.addWidget(self.scrollA_shots)

        self.frame_shots_active_btn = QFrame(self.page_shots)
        self.frame_shots_active_btn.setObjectName(u"frame_shots_active_btn")
        self.frame_shots_active_btn.setMaximumSize(QSize(16777215, 70))
        self.frame_shots_active_btn.setStyleSheet(u"")
        self.frame_shots_active_btn.setFrameShape(QFrame.NoFrame)
        self.frame_shots_active_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_shots_active_btn)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, -1, 0)
        self.btn_shots_reference_tool = QPushButton(self.frame_shots_active_btn)
        self.btn_shots_reference_tool.setObjectName(u"btn_shots_reference_tool")
        self.btn_shots_reference_tool.setMinimumSize(QSize(0, 35))
        font6 = QFont()
        font6.setFamily(u"Quicksand")
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.btn_shots_reference_tool.setFont(font6)
        self.btn_shots_reference_tool.setStyleSheet(u"QPushButton{\n"
"	background-color:#8B94A4;\n"
"	color:#414752;\n"
"	border-radius:7px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	color:#FFF;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color:#FFF;\n"
"	background-color:#000000;\n"
"}")

        self.horizontalLayout_20.addWidget(self.btn_shots_reference_tool)

        self.btn_shots_save = QPushButton(self.frame_shots_active_btn)
        self.btn_shots_save.setObjectName(u"btn_shots_save")
        self.btn_shots_save.setMinimumSize(QSize(0, 35))
        self.btn_shots_save.setFont(font6)
        self.btn_shots_save.setStyleSheet(u"QPushButton{\n"
"	background-color:#8B94A4;\n"
"	color:#414752;\n"
"	border-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#FFF;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color:#FFF;\n"
"	background-color:#000000;\n"
"}")

        self.horizontalLayout_20.addWidget(self.btn_shots_save)

        self.btn_shots_save_incremental = QPushButton(self.frame_shots_active_btn)
        self.btn_shots_save_incremental.setObjectName(u"btn_shots_save_incremental")
        self.btn_shots_save_incremental.setMinimumSize(QSize(0, 35))
        self.btn_shots_save_incremental.setFont(font6)
        self.btn_shots_save_incremental.setStyleSheet(u"QPushButton{\n"
"	background-color:#8B94A4;\n"
"	color:#414752;\n"
"	border-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#FFF;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color:#FFF;\n"
"	background-color:#000000;\n"
"}")

        self.horizontalLayout_20.addWidget(self.btn_shots_save_incremental)

        self.frame_shots_publish_btn = QFrame(self.frame_shots_active_btn)
        self.frame_shots_publish_btn.setObjectName(u"frame_shots_publish_btn")
        self.frame_shots_publish_btn.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:7px;\n"
"	margin-left:30px;\n"
"	margin-right:30px;\n"
"}")
        self.frame_shots_publish_btn.setFrameShape(QFrame.NoFrame)
        self.frame_shots_publish_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_shots_publish_btn)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, -1, 0)
        self.btn_shots_publish = QPushButton(self.frame_shots_publish_btn)
        self.btn_shots_publish.setObjectName(u"btn_shots_publish")
        self.btn_shots_publish.setFont(font6)
        self.btn_shots_publish.setStyleSheet(u"QPushButton{\n"
"	color:#414752;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#FFF;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color:#FFF;\n"
"	background-color:#000000;\n"
"	border-radius:10px\n"
"}")
        self.btn_shots_publish.setFlat(True)

        self.horizontalLayout_21.addWidget(self.btn_shots_publish)

        self.ico_shots_publish = QPushButton(self.frame_shots_publish_btn)
        self.ico_shots_publish.setObjectName(u"ico_shots_publish")
        self.ico_shots_publish.setMaximumSize(QSize(30, 16777215))
        self.ico_shots_publish.setFont(font3)
        self.ico_shots_publish.setStyleSheet(u"QPushButton {\n"
"	background-color:transparent;\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	icon:url(:/icons/icons/engrenage_h.png)\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/engrenage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ico_shots_publish.setIcon(icon12)
        self.ico_shots_publish.setIconSize(QSize(30, 30))

        self.horizontalLayout_21.addWidget(self.ico_shots_publish)


        self.horizontalLayout_20.addWidget(self.frame_shots_publish_btn)


        self.verticalLayout_29.addWidget(self.frame_shots_active_btn)

        self.stackedW_projectM.addWidget(self.page_shots)

        self.verticalLayout_20.addWidget(self.stackedW_projectM)


        self.verticalLayout_19.addWidget(self.frame_projectM_active)

        self.stackedW_pages.addWidget(self.page_projectM)
        self.page_tools = QWidget()
        self.page_tools.setObjectName(u"page_tools")
        self.page_tools.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.page_tools)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedW_pages.addWidget(self.page_tools)
        self.page_infos = QWidget()
        self.page_infos.setObjectName(u"page_infos")
        self.page_infos.setStyleSheet(u"")
        self.verticalLayout_28 = QVBoxLayout(self.page_infos)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_5 = QLabel(self.page_infos)
        self.label_5.setObjectName(u"label_5")
        font7 = QFont()
        font7.setFamily(u"Quicksand")
        font7.setPointSize(48)
        self.label_5.setFont(font7)
        self.label_5.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_28.addWidget(self.label_5)

        self.stackedW_pages.addWidget(self.page_infos)
        self.page_user = QWidget()
        self.page_user.setObjectName(u"page_user")
        self.verticalLayout_96 = QVBoxLayout(self.page_user)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.label_4 = QLabel(self.page_user)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font7)
        self.label_4.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_96.addWidget(self.label_4)

        self.stackedW_pages.addWidget(self.page_user)

        self.horizontalLayout_5.addWidget(self.stackedW_pages)


        self.horizontalLayout_3.addWidget(self.frame_stackedW_active)


        self.horizontalLayout_4.addWidget(self.frame_active)


        self.verticalLayout_2.addWidget(self.frame_center)


        self.verticalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.icon_animTools.setDefault(False)
        self.stackedW_pages.setCurrentIndex(1)
        self.stackedW_projectM.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lab_name.setText(QCoreApplication.translate("MainWindow", u"PIPELIAM", None))
#if QT_CONFIG(tooltip)
        self.icon_menu.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.icon_menu.setText("")
#if QT_CONFIG(tooltip)
        self.icon_user.setToolTip(QCoreApplication.translate("MainWindow", u"User Settings", None))
#endif // QT_CONFIG(tooltip)
        self.icon_user.setText("")
#if QT_CONFIG(tooltip)
        self.icon_infos.setToolTip(QCoreApplication.translate("MainWindow", u"Need Help ?", None))
#endif // QT_CONFIG(tooltip)
        self.icon_infos.setText("")
#if QT_CONFIG(tooltip)
        self.icon_home.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.icon_home.setText("")
#if QT_CONFIG(tooltip)
        self.icon_projectM.setToolTip(QCoreApplication.translate("MainWindow", u"Project Manager", None))
#endif // QT_CONFIG(tooltip)
        self.icon_projectM.setText("")
#if QT_CONFIG(tooltip)
        self.icon_modelTools.setToolTip(QCoreApplication.translate("MainWindow", u"Modeling Tools", None))
#endif // QT_CONFIG(tooltip)
        self.icon_modelTools.setText("")
#if QT_CONFIG(tooltip)
        self.icon_textureTools.setToolTip(QCoreApplication.translate("MainWindow", u"Texturing Tools", None))
#endif // QT_CONFIG(tooltip)
        self.icon_textureTools.setText("")
#if QT_CONFIG(tooltip)
        self.icon_animTools.setToolTip(QCoreApplication.translate("MainWindow", u"Animation Tools", None))
#endif // QT_CONFIG(tooltip)
        self.icon_animTools.setText("")
#if QT_CONFIG(tooltip)
        self.icon_renderTools.setToolTip(QCoreApplication.translate("MainWindow", u"Rendering Tools", None))
#endif // QT_CONFIG(tooltip)
        self.icon_renderTools.setText("")
#if QT_CONFIG(tooltip)
        self.icon_importExportTools.setToolTip(QCoreApplication.translate("MainWindow", u"Import / Export Tools", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.icon_importExportTools.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.icon_importExportTools.setText("")
        self.icon_lab_home_2.setText("")
        self.lab_home_2.setText(QCoreApplication.translate("MainWindow", u"HOME PAGE", None))
#if QT_CONFIG(tooltip)
        self.icon_newProject.setToolTip(QCoreApplication.translate("MainWindow", u"Start a new Project", None))
#endif // QT_CONFIG(tooltip)
        self.icon_newProject.setText("")
        self.btn_newProject.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
#if QT_CONFIG(tooltip)
        self.icon_openProject.setToolTip(QCoreApplication.translate("MainWindow", u"Open a Project", None))
#endif // QT_CONFIG(tooltip)
        self.icon_openProject.setText("")
        self.bnt_openProject.setText(QCoreApplication.translate("MainWindow", u"Open Project", None))
#if QT_CONFIG(tooltip)
        self.icon_lastProject.setToolTip(QCoreApplication.translate("MainWindow", u"Open the last Project", None))
#endif // QT_CONFIG(tooltip)
        self.icon_lastProject.setText("")
        self.btn_lastProject.setText(QCoreApplication.translate("MainWindow", u"Last Project", None))
        self.icon_lab_projectM.setText("")
        self.lab_projectM.setText(QCoreApplication.translate("MainWindow", u"PROJECT :", None))
        self.lab_projectM_project.setText(QCoreApplication.translate("MainWindow", u"123", None))
        self.btn_assets.setText(QCoreApplication.translate("MainWindow", u"ASSETS", None))
        self.btn_shots.setText(QCoreApplication.translate("MainWindow", u"SHOTS", None))
        self.lab_assets.setText(QCoreApplication.translate("MainWindow", u"Assets", None))
        self.btn_characters.setText(QCoreApplication.translate("MainWindow", u"Characters", None))
        self.btn_props.setText(QCoreApplication.translate("MainWindow", u"Props", None))
        self.btn_sets.setText(QCoreApplication.translate("MainWindow", u"Sets", None))
        self.btn_add_assets.setText("")
        self.lab_stage.setText(QCoreApplication.translate("MainWindow", u"Stage", None))
        self.btn_add_stage.setText("")
        self.lab_assets_version.setText(QCoreApplication.translate("MainWindow", u"Versions", None))
        self.lab_assets_publish.setText(QCoreApplication.translate("MainWindow", u"Publish", None))
        self.lab_assets_comment.setText(QCoreApplication.translate("MainWindow", u"Comment", None))
        self.plainTextEdit.setPlainText("")
        self.btn_add_assets_comment.setText("")
        self.lab_sequences.setText(QCoreApplication.translate("MainWindow", u"Sequences", None))
        self.btn_add_sequences.setText("")
        self.lab_shots.setText(QCoreApplication.translate("MainWindow", u"Shots", None))
        self.btn_add_shots.setText("")
        self.lab_shots_version.setText(QCoreApplication.translate("MainWindow", u"Versions", None))
        self.lab_shots_publish.setText(QCoreApplication.translate("MainWindow", u"Publish", None))
        self.lab_shots_comment.setText(QCoreApplication.translate("MainWindow", u"Comment", None))
        self.btn_add_shots_comment.setText("")
        self.btn_shots_reference_tool.setText(QCoreApplication.translate("MainWindow", u"REFERENCE TOOL", None))
        self.btn_shots_save.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.btn_shots_save_incremental.setText(QCoreApplication.translate("MainWindow", u"SAVE INCREMENTAL", None))
        self.btn_shots_publish.setText(QCoreApplication.translate("MainWindow", u"PUBLISH", None))
        self.ico_shots_publish.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"HELP TEST", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"USER TEST", None))
    # retranslateUi

