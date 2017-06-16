import sys
from PySide.QtCore import *
from PySide.QtGui import *

import time


import showGui

class MainDialog(QDialog,showGui.Ui_mainDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.showButton.setText("Press")
        self.connect(self.showButton,SIGNAL("clicked()"),self.processData)
        self.workerThread =  WorkerThread()
        self.connect(self.workerThread,SIGNAL("threadDone(QString)"),self.threadDone ,Qt.DirectConnection)

    def processData(self):
        self.workerThread.start()     
        QMessageBox.information(self,'DOne',"Done There !!" + self.lineEdit.text())

    def threadDone(self,text):
        self.lineEdit.setText("Threading is done !!!")
        print text
        

class WorkerThread(QThread):
        def __init__(self, parent=None):
            super(WorkerThread, self).__init__(parent)

        def run(self):
            time.sleep(3)
            self.emit(SIGNAL("threadDone(QString)"), "Conformation that the thread is finished !!!")
          




app =  QApplication(sys.argv)
form =  MainDialog()
form.show()
app.exec_()


