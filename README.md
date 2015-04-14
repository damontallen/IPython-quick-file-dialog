IPython-quick-file-dialog
=========================

This repository contains a couple of programs for starting IPython in a different folder via GUI.

Until IPython has multi-directory support, these short programs can be used to open up IPython in 
different directories using a directory dialog.  Once there they execute the following command:

    ipython notebook
    
or 

    ipython3 notebook


You can set a default directory with a simple edit of the code.  My default directory is the one 
that contains all the directories of my notebooks.

###Note on Executing Scripts and Programs (Ubuntu specific)

In order to be able to run a script by clicking on it you will need to enable nautilus within dconfg-editor.
The following instructions were written by Basharat Sial [here](http://askubuntu.com/questions/138908/how-to-execute-a-script-just-by-double-clicking-like-exe-files-in-windows).

	Hit Alt+F2, type dconf-editor and hit Enter.
	In dconfg-editor goto: org ➤ gnome ➤ nautilus ➤ preferences
	Click on executable-text-activation and from drop down menu select:
	launch: to launch scripts as programs.
	OR
	ask: to ask what to do via a dialog.
	Close dconf-editor. Thats it!
