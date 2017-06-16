from PySide.QtCore import *
from PySide.QtGui import *
import sys
import mainUI

class MainWindow(QMainWindow,mainUI.Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent) 
        self.setupUi(self)

        self.connect(self.actionCloseFile,SIGNAL("triggered()"), self.exitApp)

       

    def exitApp(self):
        MainWindow.close(self)
        print 'hello'









app =  QApplication(sys.argv)
form =  MainWindow()
form.show()
app.exec_()