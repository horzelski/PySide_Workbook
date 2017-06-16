import sys
from PySide.QtCore import *
from PySide.QtGui import *

__appname__ =  "standerdDialog"

class Program(QDialog):

    def __init__(self, parent = None):
        super(Program, self).__init__(parent)

        self.setWindowTitle(__appname__)

        
        self.mainSpinBox  =  QSpinBox()
        self.mainCheckBox  =  QCheckBox("main CheckBox Value")
        bnt  =  QPushButton("Open Dialog")

        layout  =  QVBoxLayout()
        
        layout.addWidget(self.mainSpinBox)
        layout.addWidget(self.mainCheckBox)
        layout.addWidget(bnt)
        self.setLayout(layout)

        self.connect(bnt,SIGNAL("clicked()"),self.dialogOpen)

    def dialogOpen(self):
        initValue  =  {"mainSpinBox" : self.mainSpinBox.value(),"mainCheckBox" : self.mainCheckBox.isChecked()}
        dialog = Dialog(initValue)
        if dialog.exec_():
            self.mainSpinBox.setValue(dialog.spinBox.value())
            self.mainCheckBox.setChecked(dialog.checkBox.isChecked())





class Dialog(QDialog):

    def __init__(self, initValue, parent = None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle('Dialog.')

        self.checkBox = QCheckBox("Check me out")
        self.spinBox =  QSpinBox()
        buttonOk =  QPushButton("Ok")
        buttonCancle =  QPushButton("Cancle")


        layout  =  QGridLayout()
        layout.addWidget(self.spinBox ,0,0)
        layout.addWidget(self.checkBox ,0,1)
        layout.addWidget(buttonOk)
        layout.addWidget(buttonCancle)
        self.setLayout(layout)

        self.spinBox.setValue(initValue["mainSpinBox"])
        self.checkBox.setChecked(initValue["mainCheckBox"])


        self.connect(buttonOk,SIGNAL("clicked()"),self,SLOT("accept()"))
        self.connect(buttonCancle,SIGNAL("clicked()"),self,SLOT("reject()"))

    def accept(self):

        print "Hello I am running from overwritten Function ans dont foget self"

        
        class GreaterThenFive(Exception):
           pass
        class IsZero(Exception):
           pass

        try:
            if self.spinBox.value() > 5 :
                print "it is more then five"
                raise GreaterThenFive, ("The spinBox cannnot be greater then 5")
            elif self.spinBox.value() == 0:
                raise IsZero,("The spinBox cannnot be 0")
            else:
                QDialog.accept(self)

        except GreterThenFive, e:
            QMessageBox.warning(self,__appname__,str(e))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return

        except IsZero, e:
            QMessageBox.warning(self,__appname__,str(e))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return 



           









app =  QApplication(sys.argv)
form = Program()
form.show()
app.exec_()
