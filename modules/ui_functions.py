"""
PIPELIAM SERVICES IS PROVIDED TO YOU BY _LIAMOS ! 

THANKS FOR YOUR INTEREST AND IF YOU HAVE ANY BUGS, FEEL FREE TO SEND A MAIL TO pro.liamdocherty@gmail.com

SEE YOU SOON !

coding utf-8

"""

#systeme import 
import os
import importlib
import inspect
#pyside import
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *
#modules import


#----------------------------------------------------------------------------------------------------------------#
#------ MENU FRAME FUNCTIONS ------#
#----------------------------------------------------------------------------------------------------------------#
frame_states = {}
frame_animations = {}

def toggle_frame_visibility(frame, minWidth, maxWidth,statusbar=None):
    if frame not in frame_states:
        frame_states[frame] = False
    def toggle():
        if frame_states[frame]:
            collapse_frame(frame, minWidth, maxWidth)
            show_message_status_bar(statusbar,"Collapsed Frame")
        else:
            expand_frame(frame, minWidth, maxWidth)
            show_message_status_bar(statusbar,"Expanded Frame")
    return toggle

def expand_frame(frame, minWidth, maxWidth):
    if frame not in frame_animations:
        animation = QPropertyAnimation(frame, b'maximumWidth')
        animation.setDuration(250)
        animation.setStartValue(minWidth)
        animation.setEndValue(maxWidth)
        animation.setEasingCurve(QEasingCurve.OutBack)
        frame_animations[frame] = animation

    frame_animations[frame].setDirection(QPropertyAnimation.Forward)
    frame_animations[frame].start()

    frame_states[frame] = True

def collapse_frame(frame, minWidth, maxWidth):
    if frame not in frame_animations:
        animation = QPropertyAnimation(frame, b'maximumWidth')
        animation.setDuration(250)
        animation.setStartValue(maxWidth)
        animation.setEndValue(minWidth)
        animation.setEasingCurve(QEasingCurve.InBack)
        frame_animations[frame] = animation

    frame_animations[frame].setDirection(QPropertyAnimation.Backward)
    frame_animations[frame].start()

    frame_states[frame] = False

#----------------------------------------------------------------------------------------------------------------#
#------ BUTTONS FUNCTIONS------#
#----------------------------------------------------------------------------------------------------------------#



#----------------------------------------------------------------------------------------------------------------#
#------ TOOLTIP FUNCTIONS ------#
#----------------------------------------------------------------------------------------------------------------#
def toolTip_assigner(frame):
    list = frame.findChildren(QPushButton)
    #print(list)
    toolTip_stylesheet_icon_menu = """
    QToolTip {
        font-size: 12px;
        font-family: Quicksand;
        background-color: #FFF;
    }
    """
    for child in list :
        child_stylesheet = child.styleSheet()
        combined_stylesheet = child_stylesheet + toolTip_stylesheet_icon_menu
        child.setStyleSheet(combined_stylesheet)

#----------------------------------------------------------------------------------------------------------------#
#------ STACKED WIDGET FUNCTIONS ------#
#----------------------------------------------------------------------------------------------------------------#
        
def switch_page_menu(stackedWidget,page):
        stackedWidget.setCurrentWidget(page)
        #print(page.objectName())

#----------------------------------------------------------------------------------------------------------------#
#------ TAB WIDGET FUNCTIONS ------#
#----------------------------------------------------------------------------------------------------------------#*
def grouping_tabs(btn_list,group_button_tabs):
    for btn in btn_list :
        #print(btn.objectName())
        group_button_tabs.addButton(btn)

def switch_tab(tabW,tab,list_under_mode):
    tabW.setCurrentIndex(tab)
    clear_selections_in_listViews(list_under_mode)

def set_icons_to_tab(tabW,tab_index,icon):
    tabW.setTabIcon(tab_index,icon)

#----------------------------------------------------------------------------------------------------------------#
#------ STATUS BAR FUNCTIONS ------#
#----------------------------------------------------------------------------------------------------------------#
def show_message_status_bar(statusbar,message=None):
    statusbar.showMessage("COMMAND LAUNCHED : "+message+" ",10000)

#----------------------------------------------------------------------------------------------------------------#
#------ MODELS FUNCTIONS ------#
#----------------------------------------------------------------------------------------------------------------#
    
def setting_model(model,list_view,path):
    model.setRootPath(path)
    list_view.setModel(model)
    #print(model)
    root_index = model.index(path)
    #print(root_index)
    list_view.setRootIndex(root_index)
    #print(path)
    return path

def setting_maya_model(model, list_view, path):
    model.setRootPath(path)
    list_view.setModel(model)
    #print(model)
    root_index = model.index(path)
    #print(root_index)
    list_view.setRootIndex(root_index)
    #print(path)
    return path

def update_mode(btn_mode_list,path_mode_list,model_type_list,listView_mode_list, 
                main_path,
                btn_type_list,path_type_list,
                path_to_stage,
                list_under_mode):
    path_to_stage_new = path_to_stage
    for btn, mode_path, model, listView in zip(btn_mode_list,path_mode_list, model_type_list, listView_mode_list):
        if btn.isChecked():
            path_to_stage = main_path + mode_path
            if "assets" in btn.objectName():
                for btn_type, path_type in zip(btn_type_list,path_type_list):
                    if btn_type.isChecked():
                        path_to_stage = path_to_stage + path_type
                        #print(path_to_stage)
                        clear_selections_in_listViews(list_under_mode)
                        setting_model(model,listView,path_to_stage)
                        return path_to_stage
            if "shots" in btn.objectName():
                path_to_stage = path_to_stage
                #print(path_to_stage)
                clear_selections_in_listViews(list_under_mode)
                setting_model(model,listView,path_to_stage)
                return path_to_stage
    return path_to_stage_new
            
def update_stage_and_shots(index,model_type,listView_stage,path,maya_path): #Both stage and shots listViews are using this function to update
    # Retrieve the text of the selected folder
    selected_index = index.data(Qt.DisplayRole)
    #print("Selected text:", selected_index)
    if selected_index :
        #print(selected_index)
        path_stage_or_shot = path +"/"+ selected_index + maya_path
        #print(path_stage_or_shot)
        setting_model(model_type, listView_stage, path_stage_or_shot)
        return path_stage_or_shot
    

def update_version(index,model_stage,list_view_version,list_view_publish,path_stage):
    selected_folder = index.data(Qt.DisplayRole)
    #print("Selected text:", selected_folder)
    if selected_folder :
        path_to_versions = path_stage + selected_folder
        #print(path_to_versions)
        setting_maya_model(model_stage, list_view_version, path_to_versions)
        list_view_version.selectionModel().selectionChanged.connect(lambda selected, deselected : onSelectionChangedListView( selected, deselected, list_view_version,list_view_publish ))
        path_to_publish = update_publish(path_stage,selected_folder,model_stage,list_view_publish,list_view_version)
        return path_to_versions,path_to_publish


def update_publish(path_stage,selected_folder,model_stage,list_view_publish,list_view_version):
    path_to_publish = path_stage.replace("edit","publish") + selected_folder
    #print(path_to_publish)
    setting_maya_model(model_stage, list_view_publish, path_to_publish)
    list_view_publish.selectionModel().selectionChanged.connect(lambda selected, deselected : onSelectionChangedListView(selected, deselected, list_view_publish, list_view_version))
    return path_to_publish


def onSelectionChangedListView(selected, deselected, source_list_view, target_list_view):
    if selected.indexes():
        source_selection_model = source_list_view.selectionModel()
        target_selection_model = target_list_view.selectionModel()
        
        target_selection_model.clearSelection()
        

        selected_indexes = selected.indexes()
        selected_strings = [index.data(Qt.DisplayRole) for index in selected_indexes]
        #print(f"Selected in {source_selection_model.objectName()}: {selected_strings}")
        
    if deselected.indexes():
        deselected_indexes = deselected.indexes()
        deselected_strings = [index.data(Qt.DisplayRole) for index in deselected_indexes]
        #print(f"Deselected in {source_selection_model.objectName()}: {deselected_strings}")


def clear_selections_in_listViews(list_under_mode):
    for listView in list_under_mode:
        if listView:
            model = listView.selectionModel()
            if model :
                model.clearSelection()





    