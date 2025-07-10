"""
PIPELIAM SERVICES IS PROVIDED TO YOU BY _LIAMOS ! 

THANKS FOR YOUR INTEREST AND IF YOU HAVE ANY BUGS, FEEL FREE TO SEND A MAIL TO pro.liamdocherty@gmail.com

SEE YOU SOON !

coding utf-8
"""

# System imports
import sys
import os
import importlib
# Maya commands
import maya.cmds as cmds

print("main.py is being executed")

# Define script directory and various paths
script_directory = cmds.internalVar(userScriptDir=True)

pipeliam_path = os.path.join(script_directory, "pipeliam")
ui_path = os.path.join(pipeliam_path, 'ui')
modules_path = os.path.join(pipeliam_path, 'modules')
media_path = os.path.join(pipeliam_path, 'media')
icon_path = os.path.join(pipeliam_path, 'icons')

paths = [pipeliam_path, ui_path, modules_path, media_path, icon_path]

# Append paths to sys.path if not already there
for path in paths:
    if path not in sys.path:
        sys.path.append(path)
    else:
        print(f"Path {path} already appended")

# Modules import
import ui.pipeliamUI as pipeliamUI
importlib.reload(pipeliamUI)

# Launching UI
def launch_ui():
    global pipeliam_ui
    try:
        if 'pipeliam_ui' in globals():
            pipeliam_ui.close()  # pylint: disable=E0601
            pipeliam_ui.deleteLater()
    except Exception as e:
        print(f"Error closing UI: {e}")
        
    pipeliam_ui = pipeliamUI.PipeliamUI()
    pipeliam_ui.show(dockable=True, area='right', allowedArea='right')
    print("Pipeliam UI launched.")

if __name__ == "__main__":
    launch_ui()