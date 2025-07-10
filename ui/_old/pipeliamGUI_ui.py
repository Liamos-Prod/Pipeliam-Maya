# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pipeliamGUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ressource_rc

class Ui_pipeliamGUI(object):
    def setupUi(self, pipeliamGUI):
        if not pipeliamGUI.objectName():
            pipeliamGUI.setObjectName(u"pipeliamGUI")
        pipeliamGUI.resize(1451, 1606)
        pipeliamGUI.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(pipeliamGUI)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(pipeliamGUI)
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
        self.frame_home_title = QFrame(self.page_home)
        self.frame_home_title.setObjectName(u"frame_home_title")
        self.frame_home_title.setMaximumSize(QSize(16777215, 90))
        self.frame_home_title.setFrameShape(QFrame.StyledPanel)
        self.frame_home_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_home_title)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.hs_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.hs_1)

        self.icon_lab_home = QPushButton(self.frame_home_title)
        self.icon_lab_home.setObjectName(u"icon_lab_home")
        self.icon_lab_home.setMaximumSize(QSize(81, 81))
        self.icon_lab_home.setStyleSheet(u"/* Normal state */\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    background-color:transparent;\n"
"	border:none;\n"
"}")
        self.icon_lab_home.setIcon(icon4)
        self.icon_lab_home.setIconSize(QSize(80, 80))
        self.icon_lab_home.setFlat(True)

        self.horizontalLayout_6.addWidget(self.icon_lab_home)

        self.lab_home = QLabel(self.frame_home_title)
        self.lab_home.setObjectName(u"lab_home")
        self.lab_home.setMaximumSize(QSize(16777215, 150))
        font1 = QFont()
        font1.setFamily(u"Quicksand")
        font1.setPointSize(40)
        font1.setBold(False)
        self.lab_home.setFont(font1)
        self.lab_home.setStyleSheet(u"background-color:transparent;color:#414752;")
        self.lab_home.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lab_home)

        self.hs_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.hs_2)


        self.verticalLayout_15.addWidget(self.frame_home_title)

        self.frame_home_active = QFrame(self.page_home)
        self.frame_home_active.setObjectName(u"frame_home_active")
        self.frame_home_active.setLayoutDirection(Qt.LeftToRight)
        self.frame_home_active.setFrameShape(QFrame.NoFrame)
        self.frame_home_active.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_home_active)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_lastProject = QFrame(self.frame_home_active)
        self.frame_lastProject.setObjectName(u"frame_lastProject")
        self.frame_lastProject.setStyleSheet(u"")
        self.frame_lastProject.setFrameShape(QFrame.NoFrame)
        self.frame_lastProject.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_lastProject)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.vs_13 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_18.addItem(self.vs_13)

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

        self.vs_12 = QSpacerItem(20, 306, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.vs_12)


        self.horizontalLayout_7.addWidget(self.frame_lastProject)

        self.frame_newProject = QFrame(self.frame_home_active)
        self.frame_newProject.setObjectName(u"frame_newProject")
        self.frame_newProject.setFrameShape(QFrame.NoFrame)
        self.frame_newProject.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_newProject)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.vs_14 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_17.addItem(self.vs_14)

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

        self.vs_15 = QSpacerItem(20, 306, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.vs_15)


        self.horizontalLayout_7.addWidget(self.frame_newProject)

        self.frame_openProject = QFrame(self.frame_home_active)
        self.frame_openProject.setObjectName(u"frame_openProject")
        self.frame_openProject.setFrameShape(QFrame.NoFrame)
        self.frame_openProject.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_openProject)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.vs_16 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_16.addItem(self.vs_16)

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

        self.vs_17 = QSpacerItem(20, 306, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.vs_17)


        self.horizontalLayout_7.addWidget(self.frame_openProject)


        self.verticalLayout_15.addWidget(self.frame_home_active)

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
        self.hs_5 = QSpacerItem(346, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.hs_6 = QSpacerItem(346, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.hs_6)


        self.verticalLayout_20.addWidget(self.frame_projectM_type)

        self.stackedW_projectM = QStackedWidget(self.frame_projectM_active)
        self.stackedW_projectM.setObjectName(u"stackedW_projectM")
        self.stackedW_projectM.setFrameShadow(QFrame.Raised)
        self.page_assets = QWidget()
        self.page_assets.setObjectName(u"page_assets")
        self.verticalLayout_21 = QVBoxLayout(self.page_assets)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_assets_active = QFrame(self.page_assets)
        self.frame_assets_active.setObjectName(u"frame_assets_active")
        self.frame_assets_active.setFrameShape(QFrame.NoFrame)
        self.frame_assets_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_assets_active)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.frame_assets = QFrame(self.frame_assets_active)
        self.frame_assets.setObjectName(u"frame_assets")
        self.frame_assets.setMaximumSize(QSize(16777215, 16777215))
        self.frame_assets.setFrameShape(QFrame.NoFrame)
        self.frame_assets.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_assets)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_assets_assets_lab = QFrame(self.frame_assets)
        self.frame_assets_assets_lab.setObjectName(u"frame_assets_assets_lab")
        self.frame_assets_assets_lab.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setFamily(u"Quicksand")
        font3.setPointSize(12)
        self.frame_assets_assets_lab.setFont(font3)
        self.frame_assets_assets_lab.setFrameShape(QFrame.NoFrame)
        self.frame_assets_assets_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_assets_assets_lab)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
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

        self.verticalLayout_23.addWidget(self.lab_assets)


        self.verticalLayout_22.addWidget(self.frame_assets_assets_lab)

        self.frame_assets_scrol = QFrame(self.frame_assets)
        self.frame_assets_scrol.setObjectName(u"frame_assets_scrol")
        self.frame_assets_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_assets_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_assets_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_assets_scrol)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
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
        self.horizontalLayout_12 = QHBoxLayout(self.frame_assets_scrol_btn)
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_characters = QPushButton(self.frame_assets_scrol_btn)
        self.btn_characters.setObjectName(u"btn_characters")
        font4 = QFont()
        font4.setFamily(u"Quicksand")
        font4.setPointSize(14)
        self.btn_characters.setFont(font4)
        self.btn_characters.setCheckable(True)
        self.btn_characters.setChecked(True)

        self.horizontalLayout_12.addWidget(self.btn_characters)

        self.btn_props = QPushButton(self.frame_assets_scrol_btn)
        self.btn_props.setObjectName(u"btn_props")
        self.btn_props.setFont(font4)
        self.btn_props.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.btn_props)

        self.btn_sets = QPushButton(self.frame_assets_scrol_btn)
        self.btn_sets.setObjectName(u"btn_sets")
        self.btn_sets.setFont(font4)
        self.btn_sets.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.btn_sets)


        self.verticalLayout_25.addWidget(self.frame_assets_scrol_btn)

        self.stackedW_assets = QStackedWidget(self.frame_assets_scrol)
        self.stackedW_assets.setObjectName(u"stackedW_assets")
        self.page_characters = QWidget()
        self.page_characters.setObjectName(u"page_characters")
        self.verticalLayout_26 = QVBoxLayout(self.page_characters)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_characters_scrol_active = QFrame(self.page_characters)
        self.frame_characters_scrol_active.setObjectName(u"frame_characters_scrol_active")
        self.frame_characters_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_characters_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_characters_scrol_active)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
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
        self.scrollAWC_characters.setGeometry(QRect(0, 0, 1089, 1218))
        self.verticalLayout_27 = QVBoxLayout(self.scrollAWC_characters)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.listView_characters = QListView(self.scrollAWC_characters)
        self.listView_characters.setObjectName(u"listView_characters")
        self.listView_characters.setMinimumSize(QSize(0, 1200))
        self.listView_characters.setStyleSheet(u"")
        self.listView_characters.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_27.addWidget(self.listView_characters)

        self.scrollA_characters.setWidget(self.scrollAWC_characters)

        self.verticalLayout_98.addWidget(self.scrollA_characters)


        self.verticalLayout_26.addWidget(self.frame_characters_scrol_active)

        self.stackedW_assets.addWidget(self.page_characters)
        self.page_props = QWidget()
        self.page_props.setObjectName(u"page_props")
        self.verticalLayout_101 = QVBoxLayout(self.page_props)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.frame_props_scrol_active = QFrame(self.page_props)
        self.frame_props_scrol_active.setObjectName(u"frame_props_scrol_active")
        self.frame_props_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_props_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_props_scrol_active)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
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
        self.scrollAWC_props.setGeometry(QRect(0, 0, 66, 1218))
        self.verticalLayout_100 = QVBoxLayout(self.scrollAWC_props)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.listView_props = QListView(self.scrollAWC_props)
        self.listView_props.setObjectName(u"listView_props")
        self.listView_props.setMinimumSize(QSize(0, 1200))
        self.listView_props.setStyleSheet(u"")
        self.listView_props.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_100.addWidget(self.listView_props)

        self.scrollA_props.setWidget(self.scrollAWC_props)

        self.verticalLayout_99.addWidget(self.scrollA_props)


        self.verticalLayout_101.addWidget(self.frame_props_scrol_active)

        self.stackedW_assets.addWidget(self.page_props)
        self.page_sets = QWidget()
        self.page_sets.setObjectName(u"page_sets")
        self.verticalLayout_104 = QVBoxLayout(self.page_sets)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.frame_sets_scrol_active = QFrame(self.page_sets)
        self.frame_sets_scrol_active.setObjectName(u"frame_sets_scrol_active")
        self.frame_sets_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_sets_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_sets_scrol_active)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
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
        self.scrollAWC_sets.setGeometry(QRect(0, 0, 66, 1218))
        self.verticalLayout_103 = QVBoxLayout(self.scrollAWC_sets)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.listView_sets = QListView(self.scrollAWC_sets)
        self.listView_sets.setObjectName(u"listView_sets")
        self.listView_sets.setMinimumSize(QSize(0, 1200))
        self.listView_sets.setStyleSheet(u"")
        self.listView_sets.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_103.addWidget(self.listView_sets)

        self.scrollA_sets.setWidget(self.scrollAWC_sets)

        self.verticalLayout_102.addWidget(self.scrollA_sets)


        self.verticalLayout_104.addWidget(self.frame_sets_scrol_active)

        self.stackedW_assets.addWidget(self.page_sets)

        self.verticalLayout_25.addWidget(self.stackedW_assets)


        self.verticalLayout_22.addWidget(self.frame_assets_scrol)

        self.frame_assets_btn = QFrame(self.frame_assets)
        self.frame_assets_btn.setObjectName(u"frame_assets_btn")
        self.frame_assets_btn.setMaximumSize(QSize(16777215, 55))
        self.frame_assets_btn.setFrameShape(QFrame.NoFrame)
        self.frame_assets_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_assets_btn)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, -1, -1, -1)
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

        self.verticalLayout_24.addWidget(self.btn_add_assets)


        self.verticalLayout_22.addWidget(self.frame_assets_btn)


        self.verticalLayout_105.addWidget(self.frame_assets)

        self.frame_stage = QFrame(self.frame_assets_active)
        self.frame_stage.setObjectName(u"frame_stage")
        self.frame_stage.setMaximumSize(QSize(16777215, 16777215))
        self.frame_stage.setFrameShape(QFrame.NoFrame)
        self.frame_stage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_stage)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.frame_stage_lab = QFrame(self.frame_stage)
        self.frame_stage_lab.setObjectName(u"frame_stage_lab")
        self.frame_stage_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_stage_lab.setFrameShape(QFrame.NoFrame)
        self.frame_stage_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_stage_lab)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
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

        self.verticalLayout_47.addWidget(self.lab_stage)


        self.verticalLayout_48.addWidget(self.frame_stage_lab)

        self.frame_stage_scrol = QFrame(self.frame_stage)
        self.frame_stage_scrol.setObjectName(u"frame_stage_scrol")
        self.frame_stage_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_stage_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_stage_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_stage_scrol)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.frame_stage_scrol_active = QFrame(self.frame_stage_scrol)
        self.frame_stage_scrol_active.setObjectName(u"frame_stage_scrol_active")
        self.frame_stage_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_stage_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_stage_scrol_active)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
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
        self.scrollAWC_stage.setGeometry(QRect(0, 0, 1107, 1218))
        self.verticalLayout_46 = QVBoxLayout(self.scrollAWC_stage)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.listView_stage = QListView(self.scrollAWC_stage)
        self.listView_stage.setObjectName(u"listView_stage")
        self.listView_stage.setMinimumSize(QSize(0, 1200))
        self.listView_stage.setStyleSheet(u"")

        self.verticalLayout_46.addWidget(self.listView_stage)

        self.scrollA_stage.setWidget(self.scrollAWC_stage)

        self.verticalLayout_45.addWidget(self.scrollA_stage)


        self.verticalLayout_44.addWidget(self.frame_stage_scrol_active)


        self.verticalLayout_48.addWidget(self.frame_stage_scrol)

        self.frame_stage_btn = QFrame(self.frame_stage)
        self.frame_stage_btn.setObjectName(u"frame_stage_btn")
        self.frame_stage_btn.setMaximumSize(QSize(16777215, 55))
        self.frame_stage_btn.setFrameShape(QFrame.NoFrame)
        self.frame_stage_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_stage_btn)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, -1, -1, -1)
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

        self.verticalLayout_43.addWidget(self.btn_add_stage)


        self.verticalLayout_48.addWidget(self.frame_stage_btn)


        self.verticalLayout_105.addWidget(self.frame_stage)

        self.frame_assets_version = QFrame(self.frame_assets_active)
        self.frame_assets_version.setObjectName(u"frame_assets_version")
        self.frame_assets_version.setFrameShape(QFrame.NoFrame)
        self.frame_assets_version.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_assets_version)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.frame_assets_version_lab = QFrame(self.frame_assets_version)
        self.frame_assets_version_lab.setObjectName(u"frame_assets_version_lab")
        self.frame_assets_version_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_assets_version_lab.setFrameShape(QFrame.NoFrame)
        self.frame_assets_version_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_assets_version_lab)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
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

        self.verticalLayout_53.addWidget(self.lab_assets_version)


        self.verticalLayout_54.addWidget(self.frame_assets_version_lab)

        self.frame_assets_version_scrol = QFrame(self.frame_assets_version)
        self.frame_assets_version_scrol.setObjectName(u"frame_assets_version_scrol")
        self.frame_assets_version_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_assets_version_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_assets_version_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_assets_version_scrol)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.frame_assets_version_scrol_active = QFrame(self.frame_assets_version_scrol)
        self.frame_assets_version_scrol_active.setObjectName(u"frame_assets_version_scrol_active")
        self.frame_assets_version_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_assets_version_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_assets_version_scrol_active)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
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
        self.scrollAWC_assets_version.setGeometry(QRect(0, 0, 1107, 1218))
        self.verticalLayout_52 = QVBoxLayout(self.scrollAWC_assets_version)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.listView_assets_version = QListView(self.scrollAWC_assets_version)
        self.listView_assets_version.setObjectName(u"listView_assets_version")
        self.listView_assets_version.setMinimumSize(QSize(0, 1200))
        self.listView_assets_version.setStyleSheet(u"")

        self.verticalLayout_52.addWidget(self.listView_assets_version)

        self.scrollA_assets_version.setWidget(self.scrollAWC_assets_version)

        self.verticalLayout_51.addWidget(self.scrollA_assets_version)


        self.verticalLayout_50.addWidget(self.frame_assets_version_scrol_active)


        self.verticalLayout_54.addWidget(self.frame_assets_version_scrol)

        self.frame_assets_version_btn = QFrame(self.frame_assets_version)
        self.frame_assets_version_btn.setObjectName(u"frame_assets_version_btn")
        self.frame_assets_version_btn.setMinimumSize(QSize(0, 55))
        self.frame_assets_version_btn.setMaximumSize(QSize(16777215, 55))
        self.frame_assets_version_btn.setFrameShape(QFrame.NoFrame)
        self.frame_assets_version_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_assets_version_btn)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, -1, -1, -1)

        self.verticalLayout_54.addWidget(self.frame_assets_version_btn)


        self.verticalLayout_105.addWidget(self.frame_assets_version)

        self.frame_assets_publish_comment = QFrame(self.frame_assets_active)
        self.frame_assets_publish_comment.setObjectName(u"frame_assets_publish_comment")
        self.frame_assets_publish_comment.setFrameShape(QFrame.NoFrame)
        self.frame_assets_publish_comment.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_assets_publish_comment)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(-1, 0, -1, 0)
        self.frame_assets_publish = QFrame(self.frame_assets_publish_comment)
        self.frame_assets_publish.setObjectName(u"frame_assets_publish")
        self.frame_assets_publish.setMinimumSize(QSize(0, 200))
        self.frame_assets_publish.setFrameShape(QFrame.NoFrame)
        self.frame_assets_publish.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_assets_publish)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, -1, 0, -1)
        self.frame_assets_publish_lab = QFrame(self.frame_assets_publish)
        self.frame_assets_publish_lab.setObjectName(u"frame_assets_publish_lab")
        self.frame_assets_publish_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_assets_publish_lab.setFrameShape(QFrame.NoFrame)
        self.frame_assets_publish_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_assets_publish_lab)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
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

        self.verticalLayout_66.addWidget(self.lab_assets_publish)


        self.verticalLayout_67.addWidget(self.frame_assets_publish_lab)

        self.frame_assets_publish_scrol = QFrame(self.frame_assets_publish)
        self.frame_assets_publish_scrol.setObjectName(u"frame_assets_publish_scrol")
        self.frame_assets_publish_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_assets_publish_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_assets_publish_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_assets_publish_scrol)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, -1, 0, -1)
        self.frame_assets_publish_scrol_active = QFrame(self.frame_assets_publish_scrol)
        self.frame_assets_publish_scrol_active.setObjectName(u"frame_assets_publish_scrol_active")
        self.frame_assets_publish_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_assets_publish_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_assets_publish_scrol_active)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")

        self.verticalLayout_63.addWidget(self.frame_assets_publish_scrol_active)


        self.verticalLayout_67.addWidget(self.frame_assets_publish_scrol)


        self.verticalLayout_55.addWidget(self.frame_assets_publish)

        self.frame_assets_comment = QFrame(self.frame_assets_publish_comment)
        self.frame_assets_comment.setObjectName(u"frame_assets_comment")
        self.frame_assets_comment.setFrameShape(QFrame.StyledPanel)
        self.frame_assets_comment.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_assets_comment)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, -1, 0, -1)
        self.frame_assets_comment_lab = QFrame(self.frame_assets_comment)
        self.frame_assets_comment_lab.setObjectName(u"frame_assets_comment_lab")
        self.frame_assets_comment_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_assets_comment_lab.setFrameShape(QFrame.NoFrame)
        self.frame_assets_comment_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_assets_comment_lab)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
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

        self.verticalLayout_60.addWidget(self.lab_assets_comment)


        self.verticalLayout_61.addWidget(self.frame_assets_comment_lab)

        self.frame_assets_comment_scrol = QFrame(self.frame_assets_comment)
        self.frame_assets_comment_scrol.setObjectName(u"frame_assets_comment_scrol")
        self.frame_assets_comment_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_assets_comment_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_assets_comment_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_assets_comment_scrol)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.frame_assets_comment_scrol_active = QFrame(self.frame_assets_comment_scrol)
        self.frame_assets_comment_scrol_active.setObjectName(u"frame_assets_comment_scrol_active")
        self.frame_assets_comment_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_assets_comment_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_assets_comment_scrol_active)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
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
        self.scrollAWC_assets_comment.setGeometry(QRect(0, 0, 1107, 1218))
        self.verticalLayout_59 = QVBoxLayout(self.scrollAWC_assets_comment)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.plainTextEdit = QPlainTextEdit(self.scrollAWC_assets_comment)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(0, 1200))
        font5 = QFont()
        font5.setFamily(u"Quicksand")
        font5.setPointSize(10)
        self.plainTextEdit.setFont(font5)
        self.plainTextEdit.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_59.addWidget(self.plainTextEdit)

        self.scrollA_assets_comment.setWidget(self.scrollAWC_assets_comment)

        self.verticalLayout_58.addWidget(self.scrollA_assets_comment)


        self.verticalLayout_57.addWidget(self.frame_assets_comment_scrol_active)


        self.verticalLayout_61.addWidget(self.frame_assets_comment_scrol)

        self.frame_assets_comment_btn = QFrame(self.frame_assets_comment)
        self.frame_assets_comment_btn.setObjectName(u"frame_assets_comment_btn")
        self.frame_assets_comment_btn.setMaximumSize(QSize(16777215, 55))
        self.frame_assets_comment_btn.setFrameShape(QFrame.NoFrame)
        self.frame_assets_comment_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_assets_comment_btn)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, -1, -1, -1)
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

        self.verticalLayout_56.addWidget(self.btn_add_assets_comment)


        self.verticalLayout_61.addWidget(self.frame_assets_comment_btn)


        self.verticalLayout_55.addWidget(self.frame_assets_comment)


        self.verticalLayout_105.addWidget(self.frame_assets_publish_comment)


        self.verticalLayout_21.addWidget(self.frame_assets_active)

        self.frame_assets_active_btn = QFrame(self.page_assets)
        self.frame_assets_active_btn.setObjectName(u"frame_assets_active_btn")
        self.frame_assets_active_btn.setMaximumSize(QSize(16777215, 70))
        self.frame_assets_active_btn.setStyleSheet(u"QPushButton:hover{\n"
"	color:#FFF;\n"
"}")
        self.frame_assets_active_btn.setFrameShape(QFrame.NoFrame)
        self.frame_assets_active_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_assets_active_btn)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.btn_assets_reference_tool = QPushButton(self.frame_assets_active_btn)
        self.btn_assets_reference_tool.setObjectName(u"btn_assets_reference_tool")
        self.btn_assets_reference_tool.setMinimumSize(QSize(0, 35))
        font6 = QFont()
        font6.setFamily(u"Quicksand")
        font6.setPointSize(12)
        font6.setBold(True)
        self.btn_assets_reference_tool.setFont(font6)
        self.btn_assets_reference_tool.setStyleSheet(u"QPushButton{\n"
"	background-color:#8B94A4;\n"
"	color:#414752;\n"
"	border-radius:7px;\n"
"	margin-left:30px;\n"
"	margin-right:30px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#FFF;\n"
"}\n"
"QPushButton:pressed{\n"
"	color:#FFF;\n"
"	background-color:#000000;\n"
"}")

        self.horizontalLayout_16.addWidget(self.btn_assets_reference_tool)

        self.btn_assets_save = QPushButton(self.frame_assets_active_btn)
        self.btn_assets_save.setObjectName(u"btn_assets_save")
        self.btn_assets_save.setMinimumSize(QSize(0, 35))
        self.btn_assets_save.setFont(font6)
        self.btn_assets_save.setStyleSheet(u"QPushButton{\n"
"	background-color:#8B94A4;\n"
"	color:#414752;\n"
"	border-radius:7px;\n"
"	margin-left:30px;\n"
"	margin-right:30px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#FFF;\n"
"}\n"
"QPushButton:pressed{\n"
"	color:#FFF;\n"
"	background-color:#000000;\n"
"}")

        self.horizontalLayout_16.addWidget(self.btn_assets_save)

        self.btn_assets_save_incremental = QPushButton(self.frame_assets_active_btn)
        self.btn_assets_save_incremental.setObjectName(u"btn_assets_save_incremental")
        self.btn_assets_save_incremental.setMinimumSize(QSize(0, 35))
        self.btn_assets_save_incremental.setFont(font6)
        self.btn_assets_save_incremental.setStyleSheet(u"QPushButton{\n"
"	background-color:#8B94A4;\n"
"	color:#414752;\n"
"	border-radius:7px;\n"
"	margin-left:30px;\n"
"	margin-right:30px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#FFF;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color:#FFF;\n"
"	background-color:#000000;\n"
"}")

        self.horizontalLayout_16.addWidget(self.btn_assets_save_incremental)

        self.frame_assets_publish_btn = QFrame(self.frame_assets_active_btn)
        self.frame_assets_publish_btn.setObjectName(u"frame_assets_publish_btn")
        self.frame_assets_publish_btn.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:7px;\n"
"	margin-left:30px;\n"
"	margin-right:30px;\n"
"}\n"
"\n"
"QFrame#frame_assets_publish_btn QPushButton#btn_assets_publish:pressed{\n"
"\n"
"	background-color:#000000;\n"
"}")
        self.frame_assets_publish_btn.setFrameShape(QFrame.NoFrame)
        self.frame_assets_publish_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_assets_publish_btn)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.btn_assets_publish = QPushButton(self.frame_assets_publish_btn)
        self.btn_assets_publish.setObjectName(u"btn_assets_publish")
        self.btn_assets_publish.setFont(font6)
        self.btn_assets_publish.setStyleSheet(u"QPushButton{\n"
"	color:#414752;\n"
"}\n"
"QPushButton:hover{\n"
"	color:#FFF;\n"
"}\n"
"QPushButton:pressed{\n"
"	color:#FFF;\n"
"	background-color:#000000;\n"
"	border-radius:10px;\n"
"}")
        self.btn_assets_publish.setFlat(True)

        self.horizontalLayout_17.addWidget(self.btn_assets_publish)

        self.ico_assets_publish = QPushButton(self.frame_assets_publish_btn)
        self.ico_assets_publish.setObjectName(u"ico_assets_publish")
        self.ico_assets_publish.setMaximumSize(QSize(30, 16777215))
        self.ico_assets_publish.setFont(font3)
        self.ico_assets_publish.setStyleSheet(u"QPushButton {\n"
"	background-color:transparent;\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	icon:url(:/icons/icons/engrenage_h.png)\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/engrenage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ico_assets_publish.setIcon(icon12)
        self.ico_assets_publish.setIconSize(QSize(30, 30))

        self.horizontalLayout_17.addWidget(self.ico_assets_publish)


        self.horizontalLayout_16.addWidget(self.frame_assets_publish_btn)


        self.verticalLayout_21.addWidget(self.frame_assets_active_btn)

        self.stackedW_projectM.addWidget(self.page_assets)
        self.page_shots = QWidget()
        self.page_shots.setObjectName(u"page_shots")
        self.verticalLayout_95 = QVBoxLayout(self.page_shots)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.frame_shots_active = QFrame(self.page_shots)
        self.frame_shots_active.setObjectName(u"frame_shots_active")
        self.frame_shots_active.setFrameShape(QFrame.NoFrame)
        self.frame_shots_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_shots_active)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.frame_shots = QFrame(self.frame_shots_active)
        self.frame_shots.setObjectName(u"frame_shots")
        self.frame_shots.setMaximumSize(QSize(16777215, 16777215))
        self.frame_shots.setFrameShape(QFrame.NoFrame)
        self.frame_shots.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_shots)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.frame_shots_sequences_lab = QFrame(self.frame_shots)
        self.frame_shots_sequences_lab.setObjectName(u"frame_shots_sequences_lab")
        self.frame_shots_sequences_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_shots_sequences_lab.setFont(font3)
        self.frame_shots_sequences_lab.setFrameShape(QFrame.NoFrame)
        self.frame_shots_sequences_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_shots_sequences_lab)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
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

        self.verticalLayout_65.addWidget(self.lab_sequences)


        self.verticalLayout_62.addWidget(self.frame_shots_sequences_lab)

        self.frame_sequences_scrol = QFrame(self.frame_shots)
        self.frame_sequences_scrol.setObjectName(u"frame_sequences_scrol")
        self.frame_sequences_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_sequences_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_sequences_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_sequences_scrol)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.frame_sequences_scrol_active = QFrame(self.frame_sequences_scrol)
        self.frame_sequences_scrol_active.setObjectName(u"frame_sequences_scrol_active")
        self.frame_sequences_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_sequences_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_sequences_scrol_active)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
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
        self.scrollAWC_sequences.setGeometry(QRect(0, 0, 1107, 1218))
        self.verticalLayout_70 = QVBoxLayout(self.scrollAWC_sequences)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.listView_sequences = QListView(self.scrollAWC_sequences)
        self.listView_sequences.setObjectName(u"listView_sequences")
        self.listView_sequences.setMinimumSize(QSize(0, 1200))
        self.listView_sequences.setStyleSheet(u"")

        self.verticalLayout_70.addWidget(self.listView_sequences)

        self.scrollA_sequences.setWidget(self.scrollAWC_sequences)

        self.verticalLayout_69.addWidget(self.scrollA_sequences)


        self.verticalLayout_68.addWidget(self.frame_sequences_scrol_active)


        self.verticalLayout_62.addWidget(self.frame_sequences_scrol)

        self.frame_sequences_btn = QFrame(self.frame_shots)
        self.frame_sequences_btn.setObjectName(u"frame_sequences_btn")
        self.frame_sequences_btn.setMaximumSize(QSize(16777215, 55))
        self.frame_sequences_btn.setFrameShape(QFrame.NoFrame)
        self.frame_sequences_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_sequences_btn)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, -1, -1, -1)
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

        self.verticalLayout_71.addWidget(self.btn_add_sequences)


        self.verticalLayout_62.addWidget(self.frame_sequences_btn)


        self.verticalLayout_106.addWidget(self.frame_shots)

        self.frame_shots_shots = QFrame(self.frame_shots_active)
        self.frame_shots_shots.setObjectName(u"frame_shots_shots")
        self.frame_shots_shots.setMaximumSize(QSize(16777215, 16777215))
        self.frame_shots_shots.setFrameShape(QFrame.NoFrame)
        self.frame_shots_shots.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_shots_shots)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.frame_shots_lab = QFrame(self.frame_shots_shots)
        self.frame_shots_lab.setObjectName(u"frame_shots_lab")
        self.frame_shots_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_shots_lab.setFrameShape(QFrame.NoFrame)
        self.frame_shots_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_shots_lab)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
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

        self.verticalLayout_73.addWidget(self.lab_shots)


        self.verticalLayout_72.addWidget(self.frame_shots_lab)

        self.frame_shots_scrol = QFrame(self.frame_shots_shots)
        self.frame_shots_scrol.setObjectName(u"frame_shots_scrol")
        self.frame_shots_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_shots_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_shots_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_shots_scrol)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.frame_shots_scrol_active = QFrame(self.frame_shots_scrol)
        self.frame_shots_scrol_active.setObjectName(u"frame_shots_scrol_active")
        self.frame_shots_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_shots_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_shots_scrol_active)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.scrollA_shots = QScrollArea(self.frame_shots_scrol_active)
        self.scrollA_shots.setObjectName(u"scrollA_shots")
        self.scrollA_shots.setStyleSheet(u" QScrollBar:vertical {\n"
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
        self.scrollA_shots.setFrameShape(QFrame.NoFrame)
        self.scrollA_shots.setFrameShadow(QFrame.Raised)
        self.scrollA_shots.setWidgetResizable(True)
        self.scrollAWC_shots = QWidget()
        self.scrollAWC_shots.setObjectName(u"scrollAWC_shots")
        self.scrollAWC_shots.setGeometry(QRect(0, 0, 1107, 1218))
        self.verticalLayout_76 = QVBoxLayout(self.scrollAWC_shots)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.listView_shots = QListView(self.scrollAWC_shots)
        self.listView_shots.setObjectName(u"listView_shots")
        self.listView_shots.setMinimumSize(QSize(0, 1200))
        self.listView_shots.setStyleSheet(u"")

        self.verticalLayout_76.addWidget(self.listView_shots)

        self.scrollA_shots.setWidget(self.scrollAWC_shots)

        self.verticalLayout_75.addWidget(self.scrollA_shots)


        self.verticalLayout_74.addWidget(self.frame_shots_scrol_active)


        self.verticalLayout_72.addWidget(self.frame_shots_scrol)

        self.frame_shots_btn = QFrame(self.frame_shots_shots)
        self.frame_shots_btn.setObjectName(u"frame_shots_btn")
        self.frame_shots_btn.setMaximumSize(QSize(16777215, 55))
        self.frame_shots_btn.setFrameShape(QFrame.NoFrame)
        self.frame_shots_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_shots_btn)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, -1, -1, -1)
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

        self.verticalLayout_77.addWidget(self.btn_add_shots)


        self.verticalLayout_72.addWidget(self.frame_shots_btn)


        self.verticalLayout_106.addWidget(self.frame_shots_shots)

        self.frame_shots_version = QFrame(self.frame_shots_active)
        self.frame_shots_version.setObjectName(u"frame_shots_version")
        self.frame_shots_version.setMaximumSize(QSize(16777215, 16777215))
        self.frame_shots_version.setFrameShape(QFrame.NoFrame)
        self.frame_shots_version.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_shots_version)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.frame_shots_version_lab = QFrame(self.frame_shots_version)
        self.frame_shots_version_lab.setObjectName(u"frame_shots_version_lab")
        self.frame_shots_version_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_shots_version_lab.setFrameShape(QFrame.NoFrame)
        self.frame_shots_version_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_shots_version_lab)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
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

        self.verticalLayout_79.addWidget(self.lab_shots_version)


        self.verticalLayout_78.addWidget(self.frame_shots_version_lab)

        self.frame_shots_version_scrol = QFrame(self.frame_shots_version)
        self.frame_shots_version_scrol.setObjectName(u"frame_shots_version_scrol")
        self.frame_shots_version_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_shots_version_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_shots_version_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_shots_version_scrol)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.frame_shots_version_scrol_active = QFrame(self.frame_shots_version_scrol)
        self.frame_shots_version_scrol_active.setObjectName(u"frame_shots_version_scrol_active")
        self.frame_shots_version_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_shots_version_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_shots_version_scrol_active)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
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
        self.scrollAWC_shots_version.setGeometry(QRect(0, 0, 1107, 1218))
        self.verticalLayout_82 = QVBoxLayout(self.scrollAWC_shots_version)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.listView_shots_version = QListView(self.scrollAWC_shots_version)
        self.listView_shots_version.setObjectName(u"listView_shots_version")
        self.listView_shots_version.setMinimumSize(QSize(0, 1200))
        self.listView_shots_version.setStyleSheet(u"")

        self.verticalLayout_82.addWidget(self.listView_shots_version)

        self.scrollA_shots_version.setWidget(self.scrollAWC_shots_version)

        self.verticalLayout_81.addWidget(self.scrollA_shots_version)


        self.verticalLayout_80.addWidget(self.frame_shots_version_scrol_active)


        self.verticalLayout_78.addWidget(self.frame_shots_version_scrol)

        self.frame_shots_version_btn = QFrame(self.frame_shots_version)
        self.frame_shots_version_btn.setObjectName(u"frame_shots_version_btn")
        self.frame_shots_version_btn.setMinimumSize(QSize(0, 55))
        self.frame_shots_version_btn.setMaximumSize(QSize(16777215, 55))
        self.frame_shots_version_btn.setFrameShape(QFrame.NoFrame)
        self.frame_shots_version_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_shots_version_btn)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, -1, -1, -1)

        self.verticalLayout_78.addWidget(self.frame_shots_version_btn)


        self.verticalLayout_106.addWidget(self.frame_shots_version)

        self.frame_shots_publish_comment = QFrame(self.frame_shots_active)
        self.frame_shots_publish_comment.setObjectName(u"frame_shots_publish_comment")
        self.frame_shots_publish_comment.setFrameShape(QFrame.NoFrame)
        self.frame_shots_publish_comment.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_shots_publish_comment)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(-1, 0, -1, 0)
        self.frame_shots_publish = QFrame(self.frame_shots_publish_comment)
        self.frame_shots_publish.setObjectName(u"frame_shots_publish")
        self.frame_shots_publish.setMinimumSize(QSize(0, 200))
        self.frame_shots_publish.setFrameShape(QFrame.NoFrame)
        self.frame_shots_publish.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_shots_publish)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.frame_shots_publish_lab = QFrame(self.frame_shots_publish)
        self.frame_shots_publish_lab.setObjectName(u"frame_shots_publish_lab")
        self.frame_shots_publish_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_shots_publish_lab.setFrameShape(QFrame.NoFrame)
        self.frame_shots_publish_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_shots_publish_lab)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
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

        self.verticalLayout_86.addWidget(self.lab_shots_publish)


        self.verticalLayout_85.addWidget(self.frame_shots_publish_lab)

        self.frame_shots_publish_scrol = QFrame(self.frame_shots_publish)
        self.frame_shots_publish_scrol.setObjectName(u"frame_shots_publish_scrol")
        self.frame_shots_publish_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_shots_publish_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_shots_publish_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_shots_publish_scrol)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.frame_shots_publish_scrol_active = QFrame(self.frame_shots_publish_scrol)
        self.frame_shots_publish_scrol_active.setObjectName(u"frame_shots_publish_scrol_active")
        self.frame_shots_publish_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_shots_publish_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_shots_publish_scrol_active)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")

        self.verticalLayout_87.addWidget(self.frame_shots_publish_scrol_active)


        self.verticalLayout_85.addWidget(self.frame_shots_publish_scrol)


        self.verticalLayout_84.addWidget(self.frame_shots_publish)

        self.frame_shots_comment = QFrame(self.frame_shots_publish_comment)
        self.frame_shots_comment.setObjectName(u"frame_shots_comment")
        self.frame_shots_comment.setFrameShape(QFrame.StyledPanel)
        self.frame_shots_comment.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.frame_shots_comment)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.frame_shots_comment_lab = QFrame(self.frame_shots_comment)
        self.frame_shots_comment_lab.setObjectName(u"frame_shots_comment_lab")
        self.frame_shots_comment_lab.setMaximumSize(QSize(16777215, 50))
        self.frame_shots_comment_lab.setFrameShape(QFrame.NoFrame)
        self.frame_shots_comment_lab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_shots_comment_lab)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
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

        self.verticalLayout_90.addWidget(self.lab_shots_comment)


        self.verticalLayout_89.addWidget(self.frame_shots_comment_lab)

        self.frame_shots_comment_scrol = QFrame(self.frame_shots_comment)
        self.frame_shots_comment_scrol.setObjectName(u"frame_shots_comment_scrol")
        self.frame_shots_comment_scrol.setStyleSheet(u"QFrame{\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}")
        self.frame_shots_comment_scrol.setFrameShape(QFrame.NoFrame)
        self.frame_shots_comment_scrol.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_shots_comment_scrol)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.frame_shots_comment_scrol_active = QFrame(self.frame_shots_comment_scrol)
        self.frame_shots_comment_scrol_active.setObjectName(u"frame_shots_comment_scrol_active")
        self.frame_shots_comment_scrol_active.setFrameShape(QFrame.NoFrame)
        self.frame_shots_comment_scrol_active.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_shots_comment_scrol_active)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
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
        self.scrollAWC_shots_comment.setGeometry(QRect(0, 0, 1089, 1218))
        self.verticalLayout_93 = QVBoxLayout(self.scrollAWC_shots_comment)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.listView_shots_comment = QListView(self.scrollAWC_shots_comment)
        self.listView_shots_comment.setObjectName(u"listView_shots_comment")
        self.listView_shots_comment.setMinimumSize(QSize(0, 1200))
        self.listView_shots_comment.setStyleSheet(u"")

        self.verticalLayout_93.addWidget(self.listView_shots_comment)

        self.scrollA_shots_comment.setWidget(self.scrollAWC_shots_comment)

        self.verticalLayout_92.addWidget(self.scrollA_shots_comment)


        self.verticalLayout_91.addWidget(self.frame_shots_comment_scrol_active)


        self.verticalLayout_89.addWidget(self.frame_shots_comment_scrol)

        self.frame_shots_comment_btn = QFrame(self.frame_shots_comment)
        self.frame_shots_comment_btn.setObjectName(u"frame_shots_comment_btn")
        self.frame_shots_comment_btn.setMaximumSize(QSize(16777215, 55))
        self.frame_shots_comment_btn.setFrameShape(QFrame.NoFrame)
        self.frame_shots_comment_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_shots_comment_btn)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, -1, -1, -1)
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

        self.verticalLayout_94.addWidget(self.btn_add_shots_comment)


        self.verticalLayout_89.addWidget(self.frame_shots_comment_btn)


        self.verticalLayout_84.addWidget(self.frame_shots_comment)


        self.verticalLayout_106.addWidget(self.frame_shots_publish_comment)


        self.verticalLayout_95.addWidget(self.frame_shots_active)

        self.stackedW_projectM.addWidget(self.page_shots)

        self.verticalLayout_20.addWidget(self.stackedW_projectM)


        self.verticalLayout_19.addWidget(self.frame_projectM_active)

        self.stackedW_pages.addWidget(self.page_projectM)
        self.page_tools = QWidget()
        self.page_tools.setObjectName(u"page_tools")
        self.page_tools.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.page_tools)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_tools = QFrame(self.page_tools)
        self.frame_tools.setObjectName(u"frame_tools")
        self.frame_tools.setFrameShape(QFrame.StyledPanel)
        self.frame_tools.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_tools)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.tabW_tools = QTabWidget(self.frame_tools)
        self.tabW_tools.setObjectName(u"tabW_tools")
        font7 = QFont()
        font7.setFamily(u"Quicksand")
        font7.setPointSize(11)
        font7.setBold(True)
        self.tabW_tools.setFont(font7)
        self.tabW_tools.setStyleSheet(u"QTabWidget::pane {\n"
"    border: none;\n"
"	background-color:#8B94A4;\n"
"	border-radius:15px;\n"
"}\n"
"\n"
"/* Style the individual tabs */\n"
"QTabBar::tab {\n"
"    margin-left: 20px; /* Add a left margin */\n"
"    margin-right: 20px; /* Add a right margin */\n"
"	margin-bottom:8px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: transparent;\n"
"    padding: 8px 16px; /* Adjust the padding as needed */\n"
"    border: none;\n"
"    color: #414752;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    color: #ffffff; /* Set the text color of the selected tab */\n"
"    border-radius:15px;\n"
"}")
        self.tabW_tools.setElideMode(Qt.ElideNone)
        self.tab_modelTools = QWidget()
        self.tab_modelTools.setObjectName(u"tab_modelTools")
        self.verticalLayout_29 = QVBoxLayout(self.tab_modelTools)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.scrollA_modelTools = QScrollArea(self.tab_modelTools)
        self.scrollA_modelTools.setObjectName(u"scrollA_modelTools")
        self.scrollA_modelTools.setStyleSheet(u" QScrollBar:vertical {\n"
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
        self.scrollA_modelTools.setFrameShape(QFrame.NoFrame)
        self.scrollA_modelTools.setFrameShadow(QFrame.Raised)
        self.scrollA_modelTools.setWidgetResizable(True)
        self.scrollAWC_modelTools = QWidget()
        self.scrollAWC_modelTools.setObjectName(u"scrollAWC_modelTools")
        self.scrollAWC_modelTools.setGeometry(QRect(0, 0, 68, 1218))
        self.scrollAWC_modelTools.setStyleSheet(u"")
        self.verticalLayout_31 = QVBoxLayout(self.scrollAWC_modelTools)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.listView_modelTools = QListView(self.scrollAWC_modelTools)
        self.listView_modelTools.setObjectName(u"listView_modelTools")
        self.listView_modelTools.setMinimumSize(QSize(0, 1200))
        self.listView_modelTools.setStyleSheet(u"QListView{\n"
"	background-color:#A1A7B4;\n"
"	border-radius:25px;\n"
"}")

        self.verticalLayout_31.addWidget(self.listView_modelTools)

        self.scrollA_modelTools.setWidget(self.scrollAWC_modelTools)

        self.verticalLayout_29.addWidget(self.scrollA_modelTools)

        self.frame_modelTools = QFrame(self.tab_modelTools)
        self.frame_modelTools.setObjectName(u"frame_modelTools")
        self.frame_modelTools.setFrameShape(QFrame.StyledPanel)
        self.frame_modelTools.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_modelTools)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.icon_modelTools_add = QPushButton(self.frame_modelTools)
        self.icon_modelTools_add.setObjectName(u"icon_modelTools_add")
        self.icon_modelTools_add.setStyleSheet(u"QPushButton{\n"
"	background-color:#626A79;\n"
"	border-radius:20px;\n"
"	margin: 0 560px 0 560px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	icon:url(:/icons/icons/add_h.png);\n"
"	background-color:#A1A7B4;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	icon:url(:/icons/icons/add_h.png);\n"
"	background-color:#000000;\n"
"}")
        self.icon_modelTools_add.setIcon(icon10)
        self.icon_modelTools_add.setIconSize(QSize(45, 45))

        self.verticalLayout_30.addWidget(self.icon_modelTools_add)


        self.verticalLayout_29.addWidget(self.frame_modelTools)

        self.tabW_tools.addTab(self.tab_modelTools, "")
        self.tab_textureTools = QWidget()
        self.tab_textureTools.setObjectName(u"tab_textureTools")
        self.verticalLayout_41 = QVBoxLayout(self.tab_textureTools)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.scrollA_textureTools = QScrollArea(self.tab_textureTools)
        self.scrollA_textureTools.setObjectName(u"scrollA_textureTools")
        self.scrollA_textureTools.setStyleSheet(u" QScrollBar:vertical {\n"
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
        self.scrollA_textureTools.setFrameShape(QFrame.NoFrame)
        self.scrollA_textureTools.setFrameShadow(QFrame.Raised)
        self.scrollA_textureTools.setWidgetResizable(True)
        self.scrollAWC_textureTools = QWidget()
        self.scrollAWC_textureTools.setObjectName(u"scrollAWC_textureTools")
        self.scrollAWC_textureTools.setGeometry(QRect(0, 0, 68, 1218))
        self.scrollAWC_textureTools.setStyleSheet(u"")
        self.verticalLayout_33 = QVBoxLayout(self.scrollAWC_textureTools)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.listView_modelTools_2 = QListView(self.scrollAWC_textureTools)
        self.listView_modelTools_2.setObjectName(u"listView_modelTools_2")
        self.listView_modelTools_2.setMinimumSize(QSize(0, 1200))
        self.listView_modelTools_2.setStyleSheet(u"QListView{\n"
"	background-color:#A1A7B4;\n"
"	border-radius:25px;\n"
"}")

        self.verticalLayout_33.addWidget(self.listView_modelTools_2)

        self.scrollA_textureTools.setWidget(self.scrollAWC_textureTools)

        self.verticalLayout_41.addWidget(self.scrollA_textureTools)

        self.frame_textureTools = QFrame(self.tab_textureTools)
        self.frame_textureTools.setObjectName(u"frame_textureTools")
        self.frame_textureTools.setFrameShape(QFrame.StyledPanel)
        self.frame_textureTools.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_textureTools)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.icon_textureTools_add = QPushButton(self.frame_textureTools)
        self.icon_textureTools_add.setObjectName(u"icon_textureTools_add")
        self.icon_textureTools_add.setStyleSheet(u"QPushButton{\n"
"	background-color:#626A79;\n"
"	border-radius:20px;\n"
"	margin: 0 560px 0 560px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	icon:url(:/icons/icons/add_h.png);\n"
"	background-color:#A1A7B4;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	icon:url(:/icons/icons/add_h.png);\n"
"	background-color:#000000;\n"
"}")
        self.icon_textureTools_add.setIcon(icon10)
        self.icon_textureTools_add.setIconSize(QSize(45, 45))

        self.verticalLayout_32.addWidget(self.icon_textureTools_add)


        self.verticalLayout_41.addWidget(self.frame_textureTools)

        self.tabW_tools.addTab(self.tab_textureTools, "")
        self.tab_animTools = QWidget()
        self.tab_animTools.setObjectName(u"tab_animTools")
        self.verticalLayout_40 = QVBoxLayout(self.tab_animTools)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.scrollA_animTools = QScrollArea(self.tab_animTools)
        self.scrollA_animTools.setObjectName(u"scrollA_animTools")
        self.scrollA_animTools.setStyleSheet(u" QScrollBar:vertical {\n"
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
        self.scrollA_animTools.setFrameShape(QFrame.NoFrame)
        self.scrollA_animTools.setFrameShadow(QFrame.Raised)
        self.scrollA_animTools.setWidgetResizable(True)
        self.scrollAWC_animTools = QWidget()
        self.scrollAWC_animTools.setObjectName(u"scrollAWC_animTools")
        self.scrollAWC_animTools.setGeometry(QRect(0, 0, 68, 1218))
        self.scrollAWC_animTools.setStyleSheet(u"")
        self.verticalLayout_35 = QVBoxLayout(self.scrollAWC_animTools)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.listView_animTools = QListView(self.scrollAWC_animTools)
        self.listView_animTools.setObjectName(u"listView_animTools")
        self.listView_animTools.setMinimumSize(QSize(0, 1200))
        self.listView_animTools.setStyleSheet(u"QListView{\n"
"	background-color:#A1A7B4;\n"
"	border-radius:25px;\n"
"}")

        self.verticalLayout_35.addWidget(self.listView_animTools)

        self.scrollA_animTools.setWidget(self.scrollAWC_animTools)

        self.verticalLayout_40.addWidget(self.scrollA_animTools)

        self.frame_animTools = QFrame(self.tab_animTools)
        self.frame_animTools.setObjectName(u"frame_animTools")
        self.frame_animTools.setFrameShape(QFrame.StyledPanel)
        self.frame_animTools.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_animTools)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.icon_animTools_add = QPushButton(self.frame_animTools)
        self.icon_animTools_add.setObjectName(u"icon_animTools_add")
        self.icon_animTools_add.setStyleSheet(u"QPushButton{\n"
"	background-color:#626A79;\n"
"	border-radius:20px;\n"
"	margin: 0 560px 0 560px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	icon:url(:/icons/icons/add_h.png);\n"
"	background-color:#A1A7B4;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	icon:url(:/icons/icons/add_h.png);\n"
"	background-color:#000000;\n"
"}")
        self.icon_animTools_add.setIcon(icon10)
        self.icon_animTools_add.setIconSize(QSize(45, 45))

        self.verticalLayout_34.addWidget(self.icon_animTools_add)


        self.verticalLayout_40.addWidget(self.frame_animTools)

        self.tabW_tools.addTab(self.tab_animTools, "")
        self.tab_renderTools = QWidget()
        self.tab_renderTools.setObjectName(u"tab_renderTools")
        self.verticalLayout_97 = QVBoxLayout(self.tab_renderTools)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.scrollA_renderTools = QScrollArea(self.tab_renderTools)
        self.scrollA_renderTools.setObjectName(u"scrollA_renderTools")
        self.scrollA_renderTools.setStyleSheet(u" QScrollBar:vertical {\n"
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
        self.scrollA_renderTools.setFrameShape(QFrame.NoFrame)
        self.scrollA_renderTools.setFrameShadow(QFrame.Raised)
        self.scrollA_renderTools.setWidgetResizable(True)
        self.scrollAWC_renderTools = QWidget()
        self.scrollAWC_renderTools.setObjectName(u"scrollAWC_renderTools")
        self.scrollAWC_renderTools.setGeometry(QRect(0, 0, 68, 1218))
        self.scrollAWC_renderTools.setStyleSheet(u"")
        self.verticalLayout_37 = QVBoxLayout(self.scrollAWC_renderTools)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.listView_renderTools = QListView(self.scrollAWC_renderTools)
        self.listView_renderTools.setObjectName(u"listView_renderTools")
        self.listView_renderTools.setMinimumSize(QSize(0, 1200))
        self.listView_renderTools.setStyleSheet(u"QListView{\n"
"	background-color:#A1A7B4;\n"
"	border-radius:25px;\n"
"}")

        self.verticalLayout_37.addWidget(self.listView_renderTools)

        self.scrollA_renderTools.setWidget(self.scrollAWC_renderTools)

        self.verticalLayout_97.addWidget(self.scrollA_renderTools)

        self.frame_renderTools = QFrame(self.tab_renderTools)
        self.frame_renderTools.setObjectName(u"frame_renderTools")
        self.frame_renderTools.setFrameShape(QFrame.StyledPanel)
        self.frame_renderTools.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_renderTools)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.icon_renderTools_add = QPushButton(self.frame_renderTools)
        self.icon_renderTools_add.setObjectName(u"icon_renderTools_add")
        self.icon_renderTools_add.setStyleSheet(u"QPushButton{\n"
"	background-color:#626A79;\n"
"	border-radius:20px;\n"
"	margin: 0 560px 0 560px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	icon:url(:/icons/icons/add_h.png);\n"
"	background-color:#A1A7B4;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	icon:url(:/icons/icons/add_h.png);\n"
"	background-color:#000000;\n"
"}")
        self.icon_renderTools_add.setIcon(icon10)
        self.icon_renderTools_add.setIconSize(QSize(45, 45))

        self.verticalLayout_36.addWidget(self.icon_renderTools_add)


        self.verticalLayout_97.addWidget(self.frame_renderTools)

        self.tabW_tools.addTab(self.tab_renderTools, "")
        self.tab_importExportTools = QWidget()
        self.tab_importExportTools.setObjectName(u"tab_importExportTools")
        self.verticalLayout_42 = QVBoxLayout(self.tab_importExportTools)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.scrollA_importExportTools = QScrollArea(self.tab_importExportTools)
        self.scrollA_importExportTools.setObjectName(u"scrollA_importExportTools")
        self.scrollA_importExportTools.setStyleSheet(u" QScrollBar:vertical {\n"
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
        self.scrollA_importExportTools.setFrameShape(QFrame.NoFrame)
        self.scrollA_importExportTools.setFrameShadow(QFrame.Raised)
        self.scrollA_importExportTools.setWidgetResizable(True)
        self.scrollAWC_importExportTools = QWidget()
        self.scrollAWC_importExportTools.setObjectName(u"scrollAWC_importExportTools")
        self.scrollAWC_importExportTools.setGeometry(QRect(0, 0, 68, 1218))
        self.scrollAWC_importExportTools.setStyleSheet(u"")
        self.verticalLayout_39 = QVBoxLayout(self.scrollAWC_importExportTools)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.listView_importExportTools = QListView(self.scrollAWC_importExportTools)
        self.listView_importExportTools.setObjectName(u"listView_importExportTools")
        self.listView_importExportTools.setMinimumSize(QSize(0, 1200))
        self.listView_importExportTools.setStyleSheet(u"QListView{\n"
"	background-color:#A1A7B4;\n"
"	border-radius:25px;\n"
"}")

        self.verticalLayout_39.addWidget(self.listView_importExportTools)

        self.scrollA_importExportTools.setWidget(self.scrollAWC_importExportTools)

        self.verticalLayout_42.addWidget(self.scrollA_importExportTools)

        self.frame_importExportTools = QFrame(self.tab_importExportTools)
        self.frame_importExportTools.setObjectName(u"frame_importExportTools")
        self.frame_importExportTools.setFrameShape(QFrame.StyledPanel)
        self.frame_importExportTools.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_importExportTools)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.icon_importExportTools_add = QPushButton(self.frame_importExportTools)
        self.icon_importExportTools_add.setObjectName(u"icon_importExportTools_add")
        self.icon_importExportTools_add.setStyleSheet(u"QPushButton{\n"
"	background-color:#626A79;\n"
"	border-radius:20px;\n"
"	margin: 0 560px 0 560px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	icon:url(:/icons/icons/add_h.png);\n"
"	background-color:#A1A7B4;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	icon:url(:/icons/icons/add_h.png);\n"
"	background-color:#000000;\n"
"}")
        self.icon_importExportTools_add.setIcon(icon10)
        self.icon_importExportTools_add.setIconSize(QSize(45, 45))

        self.verticalLayout_38.addWidget(self.icon_importExportTools_add)


        self.verticalLayout_42.addWidget(self.frame_importExportTools)

        self.tabW_tools.addTab(self.tab_importExportTools, "")

        self.verticalLayout_14.addWidget(self.tabW_tools)


        self.verticalLayout_5.addWidget(self.frame_tools)

        self.stackedW_pages.addWidget(self.page_tools)
        self.page_infos = QWidget()
        self.page_infos.setObjectName(u"page_infos")
        self.page_infos.setStyleSheet(u"")
        self.verticalLayout_28 = QVBoxLayout(self.page_infos)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_5 = QLabel(self.page_infos)
        self.label_5.setObjectName(u"label_5")
        font8 = QFont()
        font8.setFamily(u"Quicksand")
        font8.setPointSize(48)
        self.label_5.setFont(font8)
        self.label_5.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_28.addWidget(self.label_5)

        self.stackedW_pages.addWidget(self.page_infos)
        self.page_user = QWidget()
        self.page_user.setObjectName(u"page_user")
        self.verticalLayout_96 = QVBoxLayout(self.page_user)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.label_4 = QLabel(self.page_user)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font8)
        self.label_4.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_96.addWidget(self.label_4)

        self.stackedW_pages.addWidget(self.page_user)

        self.horizontalLayout_5.addWidget(self.stackedW_pages)


        self.horizontalLayout_3.addWidget(self.frame_stackedW_active)


        self.horizontalLayout_4.addWidget(self.frame_active)


        self.verticalLayout_2.addWidget(self.frame_center)


        self.verticalLayout.addWidget(self.frame_main)


        self.retranslateUi(pipeliamGUI)

        self.icon_animTools.setDefault(False)
        self.stackedW_pages.setCurrentIndex(1)
        self.stackedW_projectM.setCurrentIndex(0)
        self.tabW_tools.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(pipeliamGUI)
    # setupUi

    def retranslateUi(self, pipeliamGUI):
        pipeliamGUI.setWindowTitle(QCoreApplication.translate("pipeliamGUI", u"Form", None))
        self.lab_name.setText(QCoreApplication.translate("pipeliamGUI", u"PIPELIAM", None))
#if QT_CONFIG(tooltip)
        self.icon_menu.setToolTip(QCoreApplication.translate("pipeliamGUI", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.icon_menu.setText("")
#if QT_CONFIG(tooltip)
        self.icon_user.setToolTip(QCoreApplication.translate("pipeliamGUI", u"User Settings", None))
#endif // QT_CONFIG(tooltip)
        self.icon_user.setText("")
#if QT_CONFIG(tooltip)
        self.icon_infos.setToolTip(QCoreApplication.translate("pipeliamGUI", u"Need Help ?", None))
#endif // QT_CONFIG(tooltip)
        self.icon_infos.setText("")
#if QT_CONFIG(tooltip)
        self.icon_home.setToolTip(QCoreApplication.translate("pipeliamGUI", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.icon_home.setText("")
#if QT_CONFIG(tooltip)
        self.icon_projectM.setToolTip(QCoreApplication.translate("pipeliamGUI", u"Project Manager", None))
#endif // QT_CONFIG(tooltip)
        self.icon_projectM.setText("")
#if QT_CONFIG(tooltip)
        self.icon_modelTools.setToolTip(QCoreApplication.translate("pipeliamGUI", u"Modeling Tools", None))
#endif // QT_CONFIG(tooltip)
        self.icon_modelTools.setText("")
#if QT_CONFIG(tooltip)
        self.icon_textureTools.setToolTip(QCoreApplication.translate("pipeliamGUI", u"Texturing Tools", None))
#endif // QT_CONFIG(tooltip)
        self.icon_textureTools.setText("")
#if QT_CONFIG(tooltip)
        self.icon_animTools.setToolTip(QCoreApplication.translate("pipeliamGUI", u"Animation Tools", None))
#endif // QT_CONFIG(tooltip)
        self.icon_animTools.setText("")
#if QT_CONFIG(tooltip)
        self.icon_renderTools.setToolTip(QCoreApplication.translate("pipeliamGUI", u"Rendering Tools", None))
#endif // QT_CONFIG(tooltip)
        self.icon_renderTools.setText("")
#if QT_CONFIG(tooltip)
        self.icon_importExportTools.setToolTip(QCoreApplication.translate("pipeliamGUI", u"Import / Export Tools", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.icon_importExportTools.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.icon_importExportTools.setText("")
        self.icon_lab_home.setText("")
        self.lab_home.setText(QCoreApplication.translate("pipeliamGUI", u"HOME PAGE", None))
#if QT_CONFIG(tooltip)
        self.icon_lastProject.setToolTip(QCoreApplication.translate("pipeliamGUI", u"Open the last Project", None))
#endif // QT_CONFIG(tooltip)
        self.icon_lastProject.setText("")
        self.btn_lastProject.setText(QCoreApplication.translate("pipeliamGUI", u"Last Project", None))
#if QT_CONFIG(tooltip)
        self.icon_newProject.setToolTip(QCoreApplication.translate("pipeliamGUI", u"Start a new Project", None))
#endif // QT_CONFIG(tooltip)
        self.icon_newProject.setText("")
        self.btn_newProject.setText(QCoreApplication.translate("pipeliamGUI", u"New Project", None))
#if QT_CONFIG(tooltip)
        self.icon_openProject.setToolTip(QCoreApplication.translate("pipeliamGUI", u"Open a Project", None))
#endif // QT_CONFIG(tooltip)
        self.icon_openProject.setText("")
        self.bnt_openProject.setText(QCoreApplication.translate("pipeliamGUI", u"Open Project", None))
        self.icon_lab_projectM.setText("")
        self.lab_projectM.setText(QCoreApplication.translate("pipeliamGUI", u"PROJECT :", None))
        self.lab_projectM_project.setText(QCoreApplication.translate("pipeliamGUI", u"SUPER LONG TEXTAAAAAAA", None))
        self.btn_assets.setText(QCoreApplication.translate("pipeliamGUI", u"ASSETS", None))
        self.btn_shots.setText(QCoreApplication.translate("pipeliamGUI", u"SHOTS", None))
        self.lab_assets.setText(QCoreApplication.translate("pipeliamGUI", u"Assets", None))
        self.btn_characters.setText(QCoreApplication.translate("pipeliamGUI", u"Characters", None))
        self.btn_props.setText(QCoreApplication.translate("pipeliamGUI", u"Props", None))
        self.btn_sets.setText(QCoreApplication.translate("pipeliamGUI", u"Sets", None))
        self.btn_add_assets.setText("")
        self.lab_stage.setText(QCoreApplication.translate("pipeliamGUI", u"Stage", None))
        self.btn_add_stage.setText("")
        self.lab_assets_version.setText(QCoreApplication.translate("pipeliamGUI", u"Versions", None))
        self.lab_assets_publish.setText(QCoreApplication.translate("pipeliamGUI", u"Publish", None))
        self.lab_assets_comment.setText(QCoreApplication.translate("pipeliamGUI", u"Comment", None))
        self.plainTextEdit.setPlainText("")
        self.btn_add_assets_comment.setText("")
        self.btn_assets_reference_tool.setText(QCoreApplication.translate("pipeliamGUI", u"REFERENCE TOOL", None))
        self.btn_assets_save.setText(QCoreApplication.translate("pipeliamGUI", u"SAVE", None))
        self.btn_assets_save_incremental.setText(QCoreApplication.translate("pipeliamGUI", u"SAVE INCREMENTAL", None))
        self.btn_assets_publish.setText(QCoreApplication.translate("pipeliamGUI", u"PUBLISH", None))
        self.ico_assets_publish.setText("")
        self.lab_sequences.setText(QCoreApplication.translate("pipeliamGUI", u"Sequences", None))
        self.btn_add_sequences.setText("")
        self.lab_shots.setText(QCoreApplication.translate("pipeliamGUI", u"Shots", None))
        self.btn_add_shots.setText("")
        self.lab_shots_version.setText(QCoreApplication.translate("pipeliamGUI", u"Versions", None))
        self.lab_shots_publish.setText(QCoreApplication.translate("pipeliamGUI", u"Publish", None))
        self.lab_shots_comment.setText(QCoreApplication.translate("pipeliamGUI", u"Comment", None))
        self.btn_add_shots_comment.setText("")
        self.icon_modelTools_add.setText("")
        self.tabW_tools.setTabText(self.tabW_tools.indexOf(self.tab_modelTools), QCoreApplication.translate("pipeliamGUI", u"MODELING TOOLS", None))
        self.icon_textureTools_add.setText("")
        self.tabW_tools.setTabText(self.tabW_tools.indexOf(self.tab_textureTools), QCoreApplication.translate("pipeliamGUI", u"TEXTURE TOOLS", None))
        self.icon_animTools_add.setText("")
        self.tabW_tools.setTabText(self.tabW_tools.indexOf(self.tab_animTools), QCoreApplication.translate("pipeliamGUI", u"ANIMATION TOOLS", None))
        self.icon_renderTools_add.setText("")
        self.tabW_tools.setTabText(self.tabW_tools.indexOf(self.tab_renderTools), QCoreApplication.translate("pipeliamGUI", u"RENDERING TOOLS", None))
        self.icon_importExportTools_add.setText("")
        self.tabW_tools.setTabText(self.tabW_tools.indexOf(self.tab_importExportTools), QCoreApplication.translate("pipeliamGUI", u"IMPORT/EXPORT TOOLS", None))
        self.label_5.setText(QCoreApplication.translate("pipeliamGUI", u"HELP TEST", None))
        self.label_4.setText(QCoreApplication.translate("pipeliamGUI", u"USER TEST", None))
    # retranslateUi

