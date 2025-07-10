# Pipeliam-Maya
A pipeline built in Maya for optimisation performance

Built with python 3.14 - PySide and QT Designer


USING OF THE PIPELIAM Alpha v0.1 : 

To make the pipeliam open at maya's start, please put the userSetup.py in : $MAYA_DIR$\2022(or Higher)\scripts or copy the code inside the userSetup.py and place it in yours
If you just want to launch it manually, please copy the code in userSetup.py and place it in you script editor

Global -->

PLEASE USE MAYA 2022 to test it.

I created a folder tree that is based on the ESMA-Lyon folder tree
You can find it at : $PATH_TO_PIPELIAM$/media/folder_base

If you need to change stuff for your own folder tree make sure to keep the global names and hierarchy

The menu button at the top left will give you access to all the pages. 


Home page --> 

You can create / open / re-open last project on this page

	Create --> 
	put the folder wherever you want and put a name

	Open --> 
	give you all the last projects that you have made, if you delete one, or move it, it will not be counted inside

	Re-open last project -->
	it will open the last project you worked on with the pipeliam unless it has been moved or deleted. 

Project page --> 

The project page is the only page working for now, it will allow you to create folders and set projects… 

	Asset button --> 
	give you access to the asset page & folders 

		Character Page -->
		you can create your character folders here

		Props Page -->
		you can create your props folders here

		Sets Page -->
		you can create your sets folders here
	
	Shots button -->
	gives you access to the shot page & folders

	
	Asset or Shot --> 
	click on any folder of asset or shot to see the stages of the selected folder 

	+ button under assets or shots -->
	allows you to create a folder for your asset or shot
	

	Stages --> 
	gives you access to the different stages of your progress

	+ button under stage --> 
	Coming soon
	
	Versions --> 
	gives you a list of all the versions of your scene in this specific folder

	Publish -->
	gives you the published version of your scene in the specific folder

	Comment --> 
	Write a comment with an opened scene and add it with the V button, it will save it and each time you reopen your scene,
	you will find your comment and you can modify it and re validate it with the V button which will resave your comment. 

	Reference tool button --> 
	Coming Soon

	Open Scene button -->
	Opens the selected scene, either version or published and sets the project to the current maya folder location.

	Save button -->
	Saves the actual opened scene with the same name, if it's a new scene, it will rename it and place it in the version
	of your selected folder with an according name. e.g : if in myChara/modeling : Name of the scene = myChara_modeling_E_v001.ma


	Save incremental button -->
	will increment the actual save you made adding +1 to the version of it, if it's a new scene, it will save it as v001

	Publish button -->
	will create and open a copy of your actual scene saved as a Published file. 
	e.g : if Name of the scene = myChara_modeling_E_v001.ma --> myChara_modeling_P.ma


These are all the buttons that actually work, more are to come after the testing month, please make sure to share your projects made with the pipeliam tool : 

Bisous de France ! 

Liamos
