#systeme import 
import sys
import os
import importlib
#maya commands
import maya.cmds as cmds


script_directory = cmds.internalVar(userScriptDir=True)

pipeliam_path = os.path.join(script_directory,"pipeliam")

ui_path = os.path.join(pipeliam_path+"/", 'ui')
modules_path = os.path.join(pipeliam_path+"/", 'modules')
media_path = os.path.join(pipeliam_path+"/", 'media')

icon_path = os.path.join(media_path+"/", 'icons')
folder_base = os.path.join(media_path+"/", 'folder_base')
folder_type = os.path.join(media_path+"/", 'folder_type')
folder_comment = os.path.join(media_path+"/", 'comments')

paths = [pipeliam_path,ui_path,modules_path,icon_path]

#print(sys.path)

for path in paths :
    if path not in sys.path:
        sys.path.append(path)
        #print(sys.path)
    else :
        #print("Path Already appended")
        break
