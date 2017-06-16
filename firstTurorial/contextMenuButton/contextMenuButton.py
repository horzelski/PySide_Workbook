
import sys
from PySide.QtCore import *
from PySide.QtGui import *

__appname__ =  "contextMenuButton"

class Program(QDialog):

    def __init__(self, parent = None):
        super(Program, self).__init__(parent)

        self.setWindowTitle(__appname__)        
        self.bnt  =  QPushButton("Open Dialog")
                        
        self.bnt.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.bnt, SIGNAL("customContextMenuRequested(QPoint)"), self.myConMenu)   


        layout  =  QVBoxLayout()
        layout.addWidget(self.bnt)
        self.setLayout(layout)



        

    def myConMenu(self,point):
        self.popMenu = QMenu(self)
        self.actionPrint = QAction('print me',self, triggered=self.printMe) 
        self.popMenu.addAction(self.actionPrint)
        icon = QIcon()
        icon.addPixmap(QPixmap("E:/user/atri/PySide/firstTurorial/imageButtons/icons/LinkedIn-32.png"), QIcon.Normal, QIcon.Off)
        self.actionPrint.setIcon(icon)        
        self.popMenu.addAction(QAction('xxx', self))
        self.popMenu.addSeparator()
        self.popMenu.addAction(QAction('zzz', self))  
        self.popMenu.exec_(self.bnt.mapToGlobal(point))
    
    def createActions(self):
        self.printMe = 'Print hello'

    def printMe(self):
        print 'As you command'
        import maya.cmds as cmds
        cmds.polyCube()









app =  QApplication(sys.argv)
form = Program()
form.show()
app.exec_()
