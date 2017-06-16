import sys
from PySide.QtCore import *
from PySide.QtGui import *

path  =  'E:/user/atri'


class Program(QDialog):

    def __init__(self, parent = None):
        super(Program, self).__init__(parent)

        openButton  =  QPushButton("Open")
        closeButton  =  QPushButton("Close")
        saveButton  =  QPushButton("save")
        dirButton  =  QPushButton("other")

        self.connect(openButton,SIGNAL("clicked()"),self.open)
        self.connect(dirButton,SIGNAL("clicked()"),self.mayaCmd)
        self.connect(saveButton,SIGNAL("clicked()"),self.save)

        layOut =  QVBoxLayout()
        layOut.addWidget(openButton)
        layOut.addWidget(closeButton)
        layOut.addWidget(saveButton)
        layOut.addWidget(dirButton)
        self.setLayout(layOut)

    def open(self):

        dir =  "."
        fileObj =  QFileDialog.getOpenFileName(self,'OpenFileDialog',dir = path,filter = "Images (*.png *.xpm *.jpg);;Text files (*.txt);;maya files (*.ma)")
        print fileObj
        print type(fileObj)
        filename =  fileObj[0]
        file =  open(filename,'r')
        read = file.read()
        file.close()
        print read

    def save(self):
        dir = "."
        fileObj =  QFileDialog.getSaveFileName (self,'saveFileDialog',dir = path,filter = "Text files (*.txt)")

        text  =  "Hellow from my test text " 
        text += "Put it in  & this is new which you will file awsome "

        filename =  fileObj[0]
        file =  open(filename,mode = "w")
        file.write(text)
        file.close()





    def mayaCmd(self):
        import maya.cmds as cmds
        cmds.polyCube()
        





app =  QApplication(sys.argv)
form = Program()
form.show()
app.exec_()