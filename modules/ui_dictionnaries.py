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

#modules import
from main import pipeliam_path,icon_path


# Dictionnaries
frames_dict = {
    "stylesheets" : {
        "no_color": "background-color: transparent;",
        "dark": "background-color: #313134;",
        "light_blue": "background-color: #414752;",
        "dark_border_radius": "background-color: #313134; border-radius: 5px;",
        "frame_menu_background" :"background-color : #626A79; border-top-right-radius: 15px; border-bottom-right-radius: 15px;",
    },
    "max_sizes" : {
        "frame_top": QSize(16777215, 40),
        "frame_menu_bar": QSize(50, 16777215),
        "frame_menu" : QSize(100, 16777215),
    },
    "min_sizes" : {
        "frame_menu" : QSize(0, 0),
    },
}

policies_size_dict = {
    "expanding" : QSizePolicy.Expanding,
    "minimum" : QSizePolicy.Minimum,
    "maximum" : QSizePolicy.Maximum,
    "fixed" : QSizePolicy.Fixed,
}

layouts_dict = {
    "margins" : {
        "layout_center" : QMargins(0, 9, 9, 9),
        "small": QMargins(0, 0, 0, 0),
        "menu": QMargins(9, 9, 9, 9),
        "menu_bar":QMargins(9, 9, 9, 9),
        "title": QMargins(10, 0, 0, 0),
    },
    "spacings" : {
        "small": 0,
    },

}

labels = {
    "stylesheets" : {
        "title": "font: 63 20pt \"Quicksand SemiBold\"; color: #414752",
    },
    
}

icon_button_dict = {
    "menu_icons" : { 
        "stylesheets" :
            """
            /* Normal state */
            QPushButton {
                background-color:transparent;
            }
            
            /* Hover state */
            QPushButton:hover {
            }

            /* QToolTip */
            QToolTip {
                font-size: 12px;
                font-family: Quicksand;
                background-color: #FFF;
            }
            """,

                "size_icon" : QSize(33, 33),
    },
    "tool_tips" : {
        "icon_categories" : "Get access to all of the tools by clicking on this button ! ( It's magic )"
    },
}

paths_to_icon = {
    "icon_categories" : os.path.join(icon_path, "categories.png"),
    "icon_user" : os.path.join(icon_path, "user.png"),
    "icon_infos" : os.path.join(icon_path, "infos.png"),
}

switch_pages_menu_dict = {
    "page_home" : 0,
    "page_projectM" : 1,
    "page_tools" : 2,
    "page_infos" : 3,
    "page_user" : 4,
}
# Variables
suffix_hover = "_h"

minWidth_frame_inner_menu = 0
maxWidth_frame_inner_menu = 100