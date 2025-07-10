"""
PIPELIAM SERVICES IS PROVIDED TO YOU BY _LIAMOS ! 

THANKS FOR YOUR INTEREST AND IF YOU HAVE ANY BUGS, FEEL FREE TO SEND A MAIL TO pro.liamdocherty@gmail.com

SEE YOU SOON !

coding utf-8

"""
#systeme import
import sys 
import os
import shutil
import importlib

import modules.path_appender
importlib.reload(modules.path_appender)
from modules.path_appender import folder_base,folder_type,folder_comment
from modules.ui_functions import setting_model,clear_selections_in_listViews
from main import media_path

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *


pipeliam_version = " ALPHA v0.1"

def projectFolder(folder_name):
    try :
        shutil.copytree(folder_base+"/__NOMCLIENT_Date_Projet",folder_name)
    except Exception as e:
        raise RuntimeError("Failed to create folder: " + str(e))
        


class FolderSetter():
    def __init__(self, folder_path, model, list_view, btn_list,list_under_mode):
        self.folder_path = folder_path
        self.model = model
        self.list_view = list_view
        self.btn_list = btn_list
        self.getting_paths()
        self.switching_model(list_under_mode)
        
    def getting_paths(self):
        #adding the paths of the Assets QLists
        self.asset_path = self.folder_path + "/03_3D/01_ASSETS/"
        self.charaters_path = self.asset_path + "01_CHARACTERS/"
        self.props_path = self.asset_path + "02_PROPS/"
        self.sets_path = self.asset_path + "03_SETS/"
        #adding the paths of the Shots QLists
        self.shot_path = self.folder_path + "/03_3D/02_SHOTS/"

        self.list_paths = [self.charaters_path,self.props_path,self.sets_path,self.shot_path]
    
    def switching_model(self,list_under_mode):
        clear_selections_in_listViews(list_under_mode)
        for btn,path in zip(self.btn_list,self.list_paths) :
            if btn.isChecked():
                #print(btn.objectName())
                setting_model(self.model, self.list_view, path)
                #print(path)
                self.path = path
                return
            
    def get_type_path(self):
        return getattr(self,'path',None)



#Getting the paths appended in my string 
def file_path_appender(project_path) : 
    file_path_folder = media_path+"/file_manager/"
    file_name = "file_paths.txt" 
    file_path = file_path_folder + file_name

    # Check if the file exists
    #print(file_path)
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    # If the folder path is not appended, append it to the file
    with open(file_path, "a") as file:
        file.write("\n" + project_path )
    #print("Folder path appended successfully to " +project_path)

def get_paths_from_file():
    file_path_folder = media_path+"/file_manager/"
    file_name = "file_paths.txt" 
    file_path = file_path_folder + file_name
    # Check if the file exists
    if not os.path.exists(file_path):
        print("File does not exist.")
        return []

    # Read the contents of the text file
    with open(file_path, "r") as file:
        paths = file.readlines()

    # Strip newline characters from each path and return as a list
    paths = [path.strip() for path in paths]
    valid_paths = validate_project_paths(paths)
    unique_paths = keep_last_occurency(valid_paths)
    return unique_paths

def validate_project_paths(paths):
    """Check if each path exists and return the list of valid paths."""
    valid_paths = [path for path in paths if os.path.exists(path)]
    return valid_paths


def keep_last_occurency(paths):
    unique_paths = []
    for path in paths :
        if path not in unique_paths:
            unique_paths.append(path)
    #print(unique_paths)
    return unique_paths

def get_last_project():
    file_path_folder = media_path+"/file_manager/"
    file_name = "file_paths.txt" 
    file_path = file_path_folder + file_name
    # Check if the file exists
    if not os.path.exists(file_path):
        print("File does not exist.")
        return []
    with open(file_path) as f:
        for line in f:
            pass
        last_line = line
        return last_line
    
def create_new_folder_type(folder_name):
    try :
        if "ASSETS" in folder_name :
            shutil.copytree(folder_type+"/ASSETS/__name_chara",folder_name)
        else :
            shutil.copytree(folder_type+"/SHOTS/__temp_sq0000_sh0000",folder_name)
    except Exception as e:
        raise RuntimeError("Failed to create folder: " + str(e)) 
    #print("Creation of the new folder")


def create_comment(maya_comment_scene,path,comment):
    if path :
        comment = comment
        path_to_comment_folder = path
        #print(path_to_comment_folder)
        print(maya_comment_scene)
        if not maya_comment_scene == "" :
            full_name_comment = maya_comment_scene + "_comment.txt"
            new_comment_path = os.path.join(path_to_comment_folder,full_name_comment)
            print(new_comment_path)
            with open(new_comment_path, "w") as file:
                file.write(comment)
            print("comment created")
            return new_comment_path
        else :
            print("Please open a file to create a comment")
    else :
        print("No comment folder")


def update_comment(path):
    if path :
            path_to_comment = path
            print(path_to_comment)
            try :
                with open(path_to_comment, "r") as file:
                    existing_comment = file.read()
                    print("comment exists")
                    return existing_comment
            except FileNotFoundError :
                pass
    else :
        print("No comment folder")
    







