import maya.cmds as cmds
import os, re

def open_maya_scene(file):
    cmds.file(file, o=True,force=True)
    #print(cmds.workspace(q=True, rd=True))

def workspace_exists(path):
    path = os.sep.join((path, 'workspace.mel'))
    #print(path)
    return os.path.isfile(path)

def set_project(maya_file):
    file_path = maya_file
    print(file_path)
    if file_path:
        file_path = os.path.normpath(file_path)
        path, file = os.path.split(file_path)

        psplit = path.split("scenes")
        #print(psplit)
        if psplit[0].endswith('maya\\'):
            newWsDir = psplit[0].replace('maya\\',"maya/")
            #print(newWsDir)
            if workspace_exists(newWsDir):
                cmds.workspace(newWsDir, openWorkspace=True)
                currentWsDir = cmds.workspace(q=True, fn=True)
                print('Project set to: '+currentWsDir)


def save_maya_file(path):
    cmds.file(rename= path)
    cmds.file(save=True, type='mayaAscii')


def defining_good_path_for_save(path,count,is_increment=False):
    maya_path_version = path[0]
    maya_path_publish = path[1]
    #print(maya_path_version)
    #print(maya_path_publish)
    maya_possible_scene = cmds.file(q=True ,sn=True)
    if maya_possible_scene:
        #print(maya_possible_scene)
        if maya_path_version in maya_possible_scene:
            if is_increment == False :
                full_path_file = maya_possible_scene
                #print(full_path_file)
                return full_path_file
            else :
                splitted_path = maya_path_version.split("maya")
                #print(splitted_path)
                name_type = splitted_path[0].split("/")
                if len(name_type) > 2 :
                    name_type = name_type[-2]
                    #print(name_type)
                else :
                    ("Please select a good path, if the error occurs more, please send a mail to pro.liamdocherty@gmail.com")
                name_stage = splitted_path[1].split("/")
                name_stage = name_stage[-1]
                #print(name_stage)
                full_name_file = name_type+"_"+name_stage+"_"+"E_"+count
                full_path_file = maya_path_version+"/"+full_name_file+".ma"
                #print(full_path_file)
                return full_path_file

        else :
            splitted_path = maya_path_version.split("maya")
            #print(splitted_path)
            name_type = splitted_path[0].split("/")
            if len(name_type) > 2 :
                name_type = name_type[-2]
                #print(name_type)
            else :
                ("Please select a good path, if the error occurs more, please send a mail to pro.liamdocherty@gmail.com")
            name_stage = splitted_path[1].split("/")
            name_stage = name_stage[-1]
            #print(name_stage)
            full_name_file = name_type+"_"+name_stage+"_"+"E_"+count
            full_path_file = maya_path_version+"/"+full_name_file+".ma"
            #print(full_path_file)
            return full_path_file

    else:
        splitted_path = maya_path_version.split("maya")
        #print(splitted_path)
        name_type = splitted_path[0].split("/")
        if len(name_type) > 2 :
            name_type = name_type[-2]
            #print(name_type)
        else :
            ("Please select a good path, if the error occurs more, please send a mail to pro.liamdocherty@gmail.com")
        name_stage = splitted_path[1].split("/")
        name_stage = name_stage[-1]
        #print(name_stage)
        full_name_file = name_type+"_"+name_stage+"_"+"E_"+count
        full_path_file = maya_path_version+"/"+full_name_file+".ma"
        #print(full_path_file)
        return full_path_file
        



def contains_ma_file(path):
    files = []
    if not os.path.isdir(path):
        print(f"Folder does not exist: {path}")
        return []
    
    files = [f for f in os.listdir(path) if f.lower().endswith(".ma")]
    #print(files)
    return files


def incremental_save(path):
    files = contains_ma_file(path)
    increment_list = [0]
    for file in files :
        #print(file)
        i = os.path.splitext(file)[0]
        try : 
            num = re.findall('[0-9]+$', i)[0]
            increment_list.append(int(num))
        except IndexError:
            pass
    increment_list = sorted(increment_list)
    new_increment = increment_list[-1]+1 if increment_list else 1
    new_good_increment = "v"+f"{new_increment:04d}"
    #print(new_good_increment)
    return new_good_increment


def publish_file(path):
    path_split =path.split("_E_")
    #print(path_split)
    good_path = path_split[0]+"_P.ma"
    cmds.file(rename= good_path)
    cmds.file(save=True, type='mayaAscii')


def get_maya_scene_name():
    try :
        maya_scene_name = cmds.file(q=True,sn=True)
        return maya_scene_name
    except :
        maya_scene_name == None 
        print("Please open a file to create a comment")
