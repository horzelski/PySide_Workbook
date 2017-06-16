from PySide import QtGui 
from PySide import QtCore

import sys
path =  'C:\\Users\\Admin\\Downloads\\darkorange-pyside-stylesheet-master\\darkorange\\'

sys.path.append(path)

import darkorange 

app = QtGui.QApplication(sys.argv) 
app.setStyleSheet(darkorange.getStyleSheet()) 
app.setStyle("plastique") 

win = QtGui.QColorDialog() 
win.show() 

app.exec_() 
sys.exit()
