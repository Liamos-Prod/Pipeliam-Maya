"""
PIPELIAM SERVICES IS PROVIDED TO YOU BY _LIAMOS ! 

THANKS FOR YOUR INTEREST AND IF YOU HAVE ANY BUGS, FEEL FREE TO SEND A MAIL TO pro.liamdocherty@gmail.com

SEE YOU SOON !

coding utf-8

"""
#systeme import 
import sys
import os
import importlib

#pyside import
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import ui.pipeliam_folder_creater_UI_ui as pipeliam_folder_creater_UI
importlib.reload(pipeliam_folder_creater_UI)
import ui.pipeliam_folder_opener_UI_ui as pipeliam_folder_opener_UI_ui
importlib.reload(pipeliam_folder_opener_UI_ui)
import ui.pipeliam_folder_type_creater_ui as pipeliam_folder_type_creater_ui
importlib.reload(pipeliam_folder_type_creater_ui)
import modules.functions as functions
importlib.reload(functions)
import modules.ui_functions as ui_functions

#------------------------------------------------------------#
    #---------------# FOLDER CREATER CLASS #---------------#
#------------------------------------------------------------#
class FolderCreater(QDialog,pipeliam_folder_creater_UI.Ui_Dialog):
    name = "Folder Creater"
    version =functions.pipeliam_version

    #Basic method for the class
    def __init__(self,parent=None):
        super(FolderCreater, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(self.name + self.version)
        self.init_dialog()

    #Defining the connections to the buttons
    def init_dialog(self):
        self.btn_close.clicked.connect(self.close)

        #Setting the folder_path to a default value
        self.folder_path = "path/to/the/folder"
        self.btn_select_path.clicked.connect(self.open_file_dialog)
        #Get the name of the folder root
        self.lineEdit_file_name.textChanged.connect(self.name_folder)

        self.btn_create.clicked.connect(self.create_folder)


    def open_file_dialog(self):
        dialog = QFileDialog()
        self.folder_path = dialog.getExistingDirectory(None, "Select Folder")
        if self.folder_path :
            self.lab_path.setText(self.folder_path +"/")
        else :
            print("No path chosen, please select a real path !")

    def name_folder(self):
        self.name = self.lineEdit_file_name.text()
        self.creation_folder_path = self.folder_path+"/"+ self.name
        #print(self.creation_folder_path)
        return self.creation_folder_path,self.name

    def create_folder(self):
        try:
            functions.projectFolder(self.creation_folder_path)
            QMessageBox.information(self, "Success", "Folder created successfully.")
            self.accept()
        except RuntimeError as e:
            QMessageBox.critical(self, "Error", str(e))

#------------------------------------------------------------#
    #---------------# FOLDER OPENER CLASS #---------------#
#------------------------------------------------------------#

class FolderOpener(QDialog,pipeliam_folder_opener_UI_ui.Ui_Dialog):
    name = "Folder Opener"
    version = functions.pipeliam_version

    #Basic method for the class
    def __init__(self,parent=None):
        super(FolderOpener, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(self.name + self.version)
        self.paths = functions.get_paths_from_file()
        self.init_dialog()

    #Defining the connections to the buttons
    def init_dialog(self):
        self.btn_close.clicked.connect(self.close)
        self.btn_create.clicked.connect(self.accept)
        self.model = QStandardItemModel()
        self.show_folder()
        self.listView_folders.clicked.connect(lambda index : self.open_folder(index))

    def show_folder(self):

        for path in self.paths:
            folder_name = os.path.basename(os.path.normpath(path))
            item = QStandardItem(folder_name)
            self.model.appendRow(item)
        self.listView_folders.setModel(self.model)
        

    def open_folder(self,index):
        self.selected_item = self.model.data(index, Qt.DisplayRole)
        #print(self.selected_item)
        return self.selected_item

#------------------------------------------------------------#
    #---------------# FOLDER TYPE CREATER CLASS #---------------#
#------------------------------------------------------------#
class FolderTypeCreater(QDialog,pipeliam_folder_type_creater_ui.Ui_Dialog):
    name = "Folder Type Creater"
    version =functions.pipeliam_version

    #Basic method for the class
    def __init__(self,path,button_clicked,parent=None):
        super(FolderTypeCreater, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(self.name + self.version)
        self.init_dialog(path,button_clicked)

    #Defining the connections to the buttonsqz
    def init_dialog(self,path,button_clicked):
        self.button_clicked = button_clicked
        self.btn_close.clicked.connect(self.close)
        

        #Setting the folder_path to a default value
        self.folder_path = path
        if "ASSETS" in self.folder_path :
            #print("getting asset")
            self.stackedWidget_type.setCurrentIndex(1)
            self.lineEdit_assets.textChanged.connect(self.name_folder)
            self.name_folder()
            self.creation_folder_path = self.lineEdit_assets.textChanged.connect(self.name_folder)        

            self.btn_create.clicked.connect(self.create_folder)

        if "SHOTS" in self.folder_path :
            #print("getting shot")
            self.stackedWidget_type.setCurrentIndex(0) 
            self.lineEdit_sequence.textChanged.connect(self.name_folder)
            self.name_folder()
            self.creation_folder_path = self.lineEdit_shot.textChanged.connect(self.name_folder)        

            self.btn_create.clicked.connect(self.create_folder)            

    def name_folder(self):
        if "ASSETS" in self.folder_path :
            #print("getting asset name ")
            self.name = self.lineEdit_assets.text()
            self.creation_folder_path = self.folder_path+"/"+ self.name
            #print(self.creation_folder_path)
            return self.creation_folder_path
        if "SHOTS" in self.folder_path :
            #print("getting shot name ")
            self.name = self.lineEdit_sequence.text() + "_" + self.lineEdit_shot.text()
            self.creation_folder_path = self.folder_path+"/"+ self.name
            #print(self.creation_folder_path)
            return self.creation_folder_path

    def create_folder(self):
        try:
            #print("TEST OK -- ")
            functions.create_new_folder_type(self.creation_folder_path)
            QMessageBox.information(self, "Success", "Folder created successfully.")
            self.accept()
        except RuntimeError as e:
            QMessageBox.critical(self, "Error", str(e))