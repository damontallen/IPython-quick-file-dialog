#!/usr/bin/python

from PySide import QtGui
import os
import subprocess
import sys

def main():
    app = QtGui.QApplication([])
    msgBox = QtGui.QMessageBox()
    msgBox.setText("You are now starting a Python2.7 version of IPython.")
    msgBox.exec_()
    dialog = QtGui.QFileDialog()
    ver = "Python %s "%sys.version[:3]
    dialog.setWindowTitle("Select Root Directory for %s - IPython"%ver)
    dialog.setDirectory("/home/damon/Documents/CODE/Programing/Python/IPython Notebook Folders (links)")
    dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)
    dialog.setFileMode(QtGui.QFileDialog.Directory)
    chose_ = dialog.exec_()
    if chose_==1:
        directory = dialog.directory()
        print(directory.path())
        os.chdir(directory.path())
        cmd = "ipython2 notebook"
        try:
            subprocess.call(cmd,shell=True)
        except OSError:
            print >>sys.stderr, "Execution failed:"+cmd
    sys.exit()
    
if __name__ == '__main__':
    main()
