IPython-quick-file-dialog
=========================

This repository contains a couple of programs for starting IPython in a different folder via GUI.

Until IPython has multi-directory support, these short programs can be used to open up IPython in 
different directories using a directory dialog.  Once there they execute the following command:

    ipython notebook --pylab inline
    
or 

    ipython3 notebook --pylab inline


You can set a default directory with a simple edit of the code.  My default directory is the one 
that contains all the directories of my notebooks.
