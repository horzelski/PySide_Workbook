import sys
from PySide.QtCore import *
from PySide.QtGui import *
import mainUI

class MainDialog(QDialog,mainUI.Ui_mainDialog):
    def __init__(self, parent =None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)



app =  QApplication(sys.argv)
form =  MainDialog()
form.show()
app.exec_()