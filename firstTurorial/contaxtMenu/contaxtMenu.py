import sys
from PySide.QtCore import *
from PySide.QtGui import *

class MainForm(QMainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)

        self.bnt  =  QPushButton("Open Dialog",self)
        self.bnt.resize(100,30)

        ##context menu policy 
        self.bnt.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.bnt,SIGNAL("customContextMenuRequested()"),self.contextMenuEvent)
        layout  =  QVBoxLayout()      

        layout.addWidget(self.bnt)
        self.setLayout(layout)

        self.createActions()
        

        #creating popupMenu 
    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction(self.cutAct)
        menu.addAction(self.copyAct)
        menu.addAction(self.pasteAct)
        menu.exec_(event.globalPos())


    def createActions(self):

        self.cutAct = QAction("Cu&t", self,
                shortcut=QKeySequence.Cut,
                statusTip="Cut the current selection's contents to the clipboard",
                triggered=self.cut)

        self.copyAct = QAction("&Copy", self,
                shortcut=QKeySequence.Copy,
                statusTip="Copy the current selection's contents to the clipboard",
                triggered=self.copy)

        self.pasteAct = QAction("&Paste", self,
                shortcut=QKeySequence.Paste,
                statusTip="Paste the clipboard's contents into the current selection",
                triggered=self.paste)

    def cut(self):
        self.infoLabel.setText("Invoked <b>Edit|Cut</b>")
        

    def copy(self):
        self.infoLabel.setText("Invoked <b>Edit|Copy</b>")

    def paste(self):
        self.infoLabel.setText("Invoked <b>Edit|Paste</b>")








    #def myContextMenu(self,point):
    #    print "I will make context"
    #    self.popMenu.exec_(self.button.mapToGlobal(point))



app =  QApplication(sys.argv)
form = MainForm()
form.show()
app.exec_()