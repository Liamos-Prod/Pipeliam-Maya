import sys
import os
import maya.cmds as cmds

script_directory = cmds.internalVar(userScriptDir=True)
pipeliam_path = os.path.join(script_directory, 'pipeliam')
print(f"Adding {pipeliam_path} to sys.path")
if pipeliam_path not in sys.path:
    sys.path.append(pipeliam_path)

def launch_pipeliam():
    try:
        import pipeliam.main as main
        print("Launching Pipeliam UI")
        main.launch_ui()
    except Exception as e:
        print(f"Failed to launch Pipeliam UI: {e}")

cmds.evalDeferred(launch_pipeliam)