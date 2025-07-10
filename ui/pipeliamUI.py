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
from functools import partial
#maya ui import
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
#pyside import
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

#modules import
from main import pipeliam_path
import ui.pipeliamGUI_test_ui as pipeliamUI
importlib.reload(pipeliamUI)
import modules.ui_functions as ui_functions
importlib.reload(ui_functions)
import modules.ui_dictionnaries as ui_dictionnaries
importlib.reload(ui_dictionnaries)
import ui.pipeliamWidgets as other_widgets
importlib.reload(other_widgets)
import modules.functions as functions
importlib.reload(functions)
import modules.path_appender as path_appender
importlib.reload(path_appender)
import modules.maya_functions as maya_functions
importlib.reload(maya_functions)



#------------------------------------------------------------#
    #---------------# MAYA WINDOW #---------------#
#------------------------------------------------------------#
def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QWidget)

#------------------------------------------------------------#
    #---------------# UI CLASS #---------------#
#------------------------------------------------------------#
# Name + Version of the UI 
pipeliam_name = "Pipeliam"
pipeliam_version = functions.pipeliam_version
class PipeliamUI(MayaQWidgetDockableMixin,QMainWindow,pipeliamUI.Ui_MainWindow):

    #Basic method for the class , getting maya_main_window as parent and launching all the functions
    def __init__(self, parent=maya_main_window()):
        super(PipeliamUI, self).__init__(parent)
        self.setMinimumSize(200, 100)
        
        #Def main variables for the paths 
        self.folder_path = pipeliam_path
        self.asset_path = "/03_3D/01_ASSETS"
        self.shot_path = "/03_3D/02_SHOTS"
        self.comment_path = "/03_3D/03_COMMENTS"
        self.charaters_path = "/01_CHARACTERS"
        self.props_path = "/02_PROPS"
        self.sets_path = "/03_SETS"
        self.path_mode_list = [self.asset_path,self.shot_path]
        self.path_type_list = [self.charaters_path,self.props_path,self.sets_path]
        self.maya_path = "/maya/scenes/edit/"

        #Setting UI + status bar
        self.init_ui()
        self.statusBar
        self.toggle_menu_function(self.qstatusbar)
        

    #Setting up initial UI
    def init_ui(self):
        self.setupUi(self)
        self.setWindowTitle(pipeliam_name + pipeliam_version)
        #Defining a QStatusBar to raise Errors and Technical matters
        self.qstatusbar = QStatusBar(self)
        self.setStatusBar(self.qstatusbar)
        self.qstatusbar.setStyleSheet(ui_dictionnaries.frames_dict["stylesheets"]["dark"])
        #Assigning the basic toolTip Style to every button
        ui_functions.toolTip_assigner(self.frame_main)
        #Setting the first page
        ui_functions.switch_page_menu(self.stackedW_pages,self.page_home)
        
        #Connecting the icons menu --- --- 
        self.icon_home.clicked.connect(lambda :ui_functions.switch_page_menu(self.stackedW_pages,self.page_home))
        self.icon_projectM.clicked.connect(lambda :ui_functions.switch_page_menu(self.stackedW_pages,self.page_projectM))
        self.icon_infos.clicked.connect(lambda :ui_functions.switch_page_menu(self.stackedW_pages,self.page_infos))
        self.icon_infos.clicked.connect(lambda :ui_functions.switch_page_menu(self.stackedW_pages,self.page_user))
        #------#

        #Connecting in homePage --- --- 
        self.main_folder = path_appender.pipeliam_path
        self.btn_newProject.clicked.connect(self.show_dialog_folder_creater)
        self.btn_openProject.clicked.connect(self.show_dialog_folder_opener)
        self.btn_lastProject.clicked.connect(self.last_project_opener)
        #------#

        #Connecting in projectM --- --- 
        self.group_button_projectM = QButtonGroup()
        self.group_button_projectM.setExclusive(True)
        self.btn_assets.setChecked(True)
        self.btn_list_projectM = [self.btn_assets,self.btn_shots]
        ui_functions.grouping_tabs(self.btn_list_projectM,self.group_button_projectM)

        #Assigning switch pages
        self.btn_assets.clicked.connect(lambda :ui_functions.switch_tab(self.stackedW_projectM,0,self.listView_full_list))
        self.btn_assets.clicked.connect(lambda :ui_functions.show_message_status_bar(self.qstatusbar,"Page Assets"))
        self.btn_shots.clicked.connect(lambda :ui_functions.switch_tab(self.stackedW_projectM,1,self.listView_full_list))
        self.btn_shots.clicked.connect(lambda :ui_functions.show_message_status_bar(self.qstatusbar,"Page Shots"))
        #------#

        #Connecting in Assets --- --- 
        self.group_button_assets = QButtonGroup()
        self.group_button_assets.setExclusive(True)
        self.btn_list_assets = [self.btn_characters,self.btn_props,self.btn_sets]
        ui_functions.grouping_tabs(self.btn_list_assets,self.group_button_assets)

        #Creating models
        self.model_asset_type = QFileSystemModel()
        self.model_asset_stage = QFileSystemModel()
        self.model_asset_version = QFileSystemModel()
        self.model_asset_publish = QFileSystemModel()

        #Assigning models to listviews
        self.listView_assets_version.setModel(self.model_asset_version)
        self.listView_assets_publish.setModel(self.model_asset_publish)

        #Getting the listviews to have only one selection possible
        self.listView_assets.setSelectionMode(QListView.SingleSelection)
        self.listView_stage.setSelectionMode(QListView.SingleSelection)
        self.listView_assets_version.setSelectionMode(QListView.SingleSelection)
        self.listView_assets_publish.setSelectionMode(QListView.SingleSelection)

        #Connecting buttons
        self.btn_characters.setChecked(True)
        self.btn_characters.clicked.connect(self.switch_listview)
        self.btn_props.clicked.connect(self.switch_listview)
        self.btn_sets.clicked.connect(self.switch_listview)
        #------#

        #Connecting in Shots --- --- 

        #Creating models 
        self.model_shot_sequence = QFileSystemModel()
        self.model_shot_shot = QFileSystemModel()
        self.model_shot_version = QFileSystemModel()
        self.model_shot_publish = QFileSystemModel()
        #------#

        #Lists of listViews & Models --- --- 
        self.model_type_list = [self.model_asset_type,self.model_shot_sequence]
        self.listView_mode_list = [self.listView_assets,self.listView_sequences]

        #List of listViews under mode :
        self.listView_full_list = [self.listView_assets,self.listView_sequences,self.listView_shots,self.listView_assets_version,self.listView_assets_publish,self.listView_shots_publish,self.listView_shots_version,self.listView_stage,self.listView_shots]
        self.listView_under_mode_list = [self.listView_assets_version,self.listView_assets_publish,self.listView_shots_publish,self.listView_shots_version,self.listView_stage,self.listView_shots]

        #Lists of the ListViews for version and publish in asset and shot
        self.model_version_and_publish_list = [self.model_asset_version,self.model_shot_version,self.model_asset_publish,self.model_shot_publish]
        self.listView_version_and_publish_list = [self.listView_assets_version,self.listView_assets_publish,self.listView_shots_version,self.listView_shots_publish]

        #Assigning switch listViews
        self.path_to_stage ="null_stage"
        self.get_stage_folder()
        self.btn_assets.clicked.connect(self.get_type_folder)
        self.btn_shots.clicked.connect(self.get_type_folder)
        self.listView_assets.clicked.connect(self.get_stage_folder)
        self.listView_sequences.clicked.connect(self.get_shot_folder)
        self.listView_stage.clicked.connect(self.get_path_for_version_asset)
        self.listView_shots.clicked.connect(self.get_path_for_version_shot)

        #Connecting buttons --- --- 

        self.btn_openScene.clicked.connect(self.open_maya_scenes)
        self.btn_save.clicked.connect(self.save_maya_files)
        self.btn_save_incremental.clicked.connect(self.incremental_save_files)
        self.btn_publish.clicked.connect(self.publish_files)

        self.btn_list_adding_type = [self.btn_add_assets.objectName(),self.btn_add_shots.objectName()]
        self.btn_add_assets.clicked.connect(lambda :self.folder_type_opener(self.btn_list_adding_type[0]))
        self.btn_add_shots.clicked.connect(lambda :self.folder_type_opener(self.btn_list_adding_type[1]))

        self.btn_add_assets_comment.clicked.connect(self.comment_creater)
        self.btn_add_shots_comment.clicked.connect(self.comment_creater)



    #Setting up functions 

    def toggle_menu_function(self,statusbar):
        minWidth_frame_inner_menu = 0
        maxWidth_frame_inner_menu = 100
        self.icon_menu.clicked.connect(ui_functions.toggle_frame_visibility(self.frame_menu,minWidth_frame_inner_menu,maxWidth_frame_inner_menu,statusbar))

    def show_dialog_folder_creater(self):
        dialog = other_widgets.FolderCreater()
        result = dialog.exec_()
        if result == QDialog.Accepted:
            name_folder = dialog.name
            self.folder_path = dialog.creation_folder_path
            self.main_folder = self.folder_path
            if name_folder:
                self.getting_projet_name(name_folder)
                ui_functions.switch_page_menu(self.stackedW_pages,self.page_projectM)
                ui_functions.show_message_status_bar(self.qstatusbar,"The Project has been created and set to "+self.folder_path)
                functions.file_path_appender(self.folder_path)
                functions.FolderSetter(self.folder_path,self.model_asset_type,self.listView_assets,self.btn_list_assets,self.listView_full_list)
                self.btn_assets.click()
                self.clear_comments()
                self.maya_comment_scene = maya_functions.get_maya_scene_name().split("/")[-1].strip(".ma")
                potential_comment = functions.update_comment(self.folder_path+self.comment_path+"/"+self.maya_comment_scene+"_comment.txt")
                print(potential_comment)
                if potential_comment :
                    if "ASSETS" in self.maya_comment_path :
                        self.comment_scene_opened = self.plainTextEdit_asset_comment.setPlainText(potential_comment)
                    else : self.comment_scene_opened = self.plainTextEdit_shots_comment.setPlainText(potential_comment)
                else:
                    print("No Comment")
            return self.folder_path

    def show_dialog_folder_opener(self):
        dialog = other_widgets.FolderOpener()
        result = dialog.exec_()
        if result == QDialog.Accepted:
            for path in dialog.paths :
                if dialog.selected_item in path :
                    name_folder = dialog.selected_item
                    self.folder_path = path
            self.main_folder = self.folder_path
            #print(self.folder_path)
            if name_folder:
                self.getting_projet_name(name_folder)
                ui_functions.switch_page_menu(self.stackedW_pages,self.page_projectM)
                functions.file_path_appender(self.folder_path)
                ui_functions.show_message_status_bar(self.qstatusbar,"The Project has been set to "+self.folder_path)
                ui_functions.update_mode(self.btn_list_projectM,self.path_mode_list,self.model_type_list,self.listView_mode_list,self.folder_path,self.btn_list_assets,self.path_type_list,self.path_to_stage,self.listView_under_mode_list)
                self.btn_assets.click()
                self.clear_comments()
                self.maya_comment_scene = maya_functions.get_maya_scene_name().split("/")[-1].strip(".ma")
                potential_comment = functions.update_comment(self.folder_path+self.comment_path+"/"+self.maya_comment_scene+"_comment.txt")
                print(potential_comment)
                if potential_comment :
                    if "ASSETS" in self.maya_comment_path :
                        self.comment_scene_opened = self.plainTextEdit_asset_comment.setPlainText(potential_comment)
                    else : self.comment_scene_opened = self.plainTextEdit_shots_comment.setPlainText(potential_comment)
                else:
                    print("No Comment")
            return self.folder_path
        
    def last_project_opener(self):
        self.last_project = functions.get_last_project()
        self.folder_path = self.last_project
        name_folder = os.path.basename(os.path.normpath(self.last_project))
        self.getting_projet_name(name_folder)
        ui_functions.switch_page_menu(self.stackedW_pages,self.page_projectM)
        ui_functions.show_message_status_bar(self.qstatusbar,"The Project has been set to "+self.folder_path)
        ui_functions.update_mode(self.btn_list_projectM,self.path_mode_list,self.model_type_list,self.listView_mode_list,self.folder_path,self.btn_list_assets,self.path_type_list,self.path_to_stage,self.listView_under_mode_list)
        self.btn_assets.click()
        self.clear_comments()
        self.maya_comment_scene = maya_functions.get_maya_scene_name().split("/")[-1].strip(".ma")
        self.maya_comment_path = maya_functions.get_maya_scene_name()
        potential_comment = functions.update_comment(self.folder_path+self.comment_path+"/"+self.maya_comment_scene+"_comment.txt")
        print(potential_comment)
        if potential_comment :
            if "ASSETS" in self.maya_comment_path :
                print('In Assets')
                self.comment_scene_opened = self.plainTextEdit_asset_comment.setPlainText(potential_comment)
            else : 
                print('In Shots')
                self.comment_scene_opened = self.plainTextEdit_shots_comment.setPlainText(potential_comment)
        else:
            print("No Comment")
        return self.last_project

    def switch_listview(self):
        self.folder_setter = functions.FolderSetter(self.folder_path,self.model_asset_type,self.listView_assets,self.btn_list_assets,self.listView_full_list)
        self.path_to_type = self.folder_setter.get_type_path()
        print(self.path_to_type)

    def getting_projet_name(self,name_folder):
        self.project_name = name_folder
        self.lab_projectM_project.setText(self.project_name)

    # FUNCTIONS FOR UPDATING THE ASSET PAGE LIST VIEWS
    def get_type_folder(self):
        self.path_to_type = ui_functions.update_mode(self.btn_list_projectM, self.path_mode_list, self.model_type_list, self.listView_mode_list, self.folder_path, self.btn_list_assets, self.path_type_list,self.path_to_stage,self.listView_under_mode_list)
        #print("The New Path to type is : " + self.path_to_stage) 
        return self.path_to_type 
    
    def get_stage_folder(self, index=QModelIndex()):
        self.path_to_stage = ui_functions.update_mode(self.btn_list_projectM, self.path_mode_list, self.model_type_list, self.listView_mode_list, self.folder_path, self.btn_list_assets, self.path_type_list,self.path_to_stage,self.listView_under_mode_list)
        #print("The New Path to stage is : " + self.path_to_stage)   
         
        if index.isValid():
            self.path_to_stage = ui_functions.update_stage_and_shots(index, self.model_asset_type, self.listView_stage, self.path_to_stage, self.maya_path)
            #print(self.path_to_stage)
            return self.path_to_stage
        else:
            print("No path found")

    def get_shot_folder(self,index=QModelIndex()):
        self.path_to_stage = ui_functions.update_mode(self.btn_list_projectM, self.path_mode_list, self.model_type_list, self.listView_mode_list, self.folder_path, self.btn_list_assets, self.path_type_list,self.path_to_stage,self.listView_under_mode_list)
        if index.isValid():
            self.path_to_stage = ui_functions.update_stage_and_shots(index, self.model_shot_shot, self.listView_shots, self.path_to_stage, self.maya_path)
            #print(self.path_to_stage)
            return self.path_to_stage
        else:
            print("No path found")

    def get_path_for_version_asset(self,index=QModelIndex()):
        self.path_for_version = ui_functions.update_version(index, self.model_asset_stage,self.listView_assets_version,self.listView_assets_publish,self.path_to_stage)
        #print("The New Path to version is : " + self.path_for_version[0])
        return self.path_for_version

    def get_path_for_version_shot(self,index=QModelIndex()):
        self.path_for_version = ui_functions.update_version(index, self.model_shot_shot,self.listView_shots_version,self.listView_shots_publish,self.path_to_stage)
        #print("The New Path to version is : " + self.path_for_version[0])
        return self.path_for_version

    # FUNCTIONS FOR UPDATING THE SHOT PAGE LIST VIEWS


    # FUNCTIONS FOR BUTTONS IN THE PAGES
    def open_maya_scenes(self):
        for listView in self.listView_version_and_publish_list:
            model = listView.selectionModel()
            indexes = model.selectedIndexes()
            if "version" in listView.objectName() :
                if indexes : 
                    index = indexes[0]
                    if index.isValid():
                        self.maya_file = index.data(Qt.DisplayRole)
                        #print(self.maya_file)
                        if self.maya_file:
                            if self.maya_file.endswith(".ma"):
                                maya_functions.set_project(self.path_for_version[0]+"/"+self.maya_file)
                                maya_functions.open_maya_scene(self.path_for_version[0]+"/"+self.maya_file)
                                ui_functions.show_message_status_bar(self.qstatusbar,"Scene opened and Project set")

                                self.clear_comments()
                                self.maya_comment_scene = maya_functions.get_maya_scene_name().split("/")[-1].strip(".ma")
                                potential_comment = functions.update_comment(self.folder_path+self.comment_path+"/"+self.maya_comment_scene+"_comment.txt")
                                print(potential_comment)
                                if potential_comment :
                                    if "ASSETS" in self.path_to_type :
                                        self.comment_scene_opened = self.plainTextEdit_asset_comment.setPlainText(potential_comment)
                                    else : self.comment_scene_opened = self.plainTextEdit_shots_comment.setPlainText(potential_comment)
                                else:
                                    print("No Comment")
                                return self.maya_file
                                 
            if "publish" in listView.objectName() :
                if indexes : 
                    index = indexes[0]
                    if index.isValid():
                        self.maya_file = index.data(Qt.DisplayRole)
                        #print(self.maya_file)
                        if self.maya_file:
                            if self.maya_file.endswith(".ma"):
                                maya_functions.set_project(self.path_for_version[1]+"/"+self.maya_file)
                                maya_functions.open_maya_scene(self.path_for_version[1]+"/"+self.maya_file) 
                                ui_functions.show_message_status_bar(self.qstatusbar,"Scene opened and Project set")

                                self.clear_comments()
                                self.maya_comment_scene = maya_functions.get_maya_scene_name().split("/")[-1].strip(".ma")
                                potential_comment = functions.update_comment(self.folder_path+self.comment_path+"/"+self.maya_comment_scene+"_comment.txt")
                                print(potential_comment)
                                if potential_comment :
                                    if "ASSETS" in self.path_to_type :
                                        self.comment_scene_opened = self.plainTextEdit_asset_comment.setPlainText(potential_comment)
                                    else : self.comment_scene_opened = self.plainTextEdit_shots_comment.setPlainText(potential_comment)
                                else:
                                    print("No Comment")
                                return self.maya_file

    def save_maya_files(self):
        self.path_to_save = maya_functions.defining_good_path_for_save(self.path_for_version,"v0001",is_increment=False)
        #print(self.path_to_save)
        self.clear_comments()
        maya_functions.set_project(self.path_to_save)
        maya_functions.save_maya_file(self.path_to_save)
        ui_functions.show_message_status_bar(self.qstatusbar,"Scene Saved and Project Set")
                                

    def incremental_save_files(self):
        self.increment = maya_functions.incremental_save(self.path_for_version[0])
        self.path_to_save = maya_functions.defining_good_path_for_save(self.path_for_version,self.increment,is_increment=True)
        self.clear_comments()
        maya_functions.set_project(self.path_to_save)
        maya_functions.save_maya_file(self.path_to_save)
        ui_functions.show_message_status_bar(self.qstatusbar,"Scene Incremented and Project Set")

    def publish_files(self):
        self.path_to_save = maya_functions.defining_good_path_for_save(self.path_for_version,"publish",is_increment=False)
        self.publish_path_to_save = self.path_to_save.replace("edit","publish")
        self.clear_comments()
        maya_functions.publish_file(self.publish_path_to_save)
        ui_functions.show_message_status_bar(self.qstatusbar,"Scene Published and Project Set")

    def folder_type_opener(self,btn):
        #print(btn)
        dialog = other_widgets.FolderTypeCreater(self.path_to_type,btn)
        result = dialog.exec_()
        if result == QDialog.Accepted:
            #print(self.path_to_stage)
            ui_functions.show_message_status_bar(self.qstatusbar,"Folder created")
            return self.path_to_stage
        
    def comment_creater(self):
        self.maya_comment_scene = maya_functions.get_maya_scene_name().split("/")[-1].strip(".ma")
        print(self.maya_comment_scene)

        if "ASSETS" in self.path_to_type:
            self.comment_scene_created = self.plainTextEdit_asset_comment.toPlainText()
            #print(self.comment_path)
            functions.create_comment(self.maya_comment_scene,self.folder_path+self.comment_path+"/",self.comment_scene_created)

        else:
            self.comment_scene_created = self.plainTextEdit_shots_comment.toPlainText()
            #print(self.comment_path)
            functions.create_comment(self.maya_comment_scene,self.folder_path+self.comment_path+"/",self.comment_scene_created)

    def clear_comments(self):
        self.plainTextEdit_asset_comment.clear()
        self.plainTextEdit_shots_comment.clear()

