import sys
from PySide.QtCore import *
from PySide.QtGui import *
from math import *

class Form(QDialog):
    def __init__(self, parent = None):
        super(Form, self).__init__(parent)

        self.browser =  QTextBrowser()
        self.button = QPushButton("call some Func")
        self.lineEdit = QLineEdit()
        self.lineEdit.selectAll()

        layout =  QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.lineEdit.setFocus()

        self.connect(self.lineEdit,SIGNAL("returnPressed()"),self.updateUi)
        self.connect(self.button,SIGNAL("clicked()"),self.printMe)
        self.setWindowTitle("Calculator")

    def updateUi(self):
        
        try:
            text =  self.lineEdit.text()
            self.browser.append("%s = <b>%s </b>" % (text, eval(text)))

        except:
            self.browser.append("<font color =  red > %s is  invalid</font>" % text)

    def printMe(self):
        print "I am working as button func"

app =  QApplication(sys.argv)
form = Form()
form.show()
app.exec_()


           
    




 
    


