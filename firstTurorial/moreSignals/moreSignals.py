import sys
from PySide.QtCore import *
from PySide.QtGui import *

class ZeroSpinBox(QSpinBox):

    zeros =  0 

    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)

        self.connect(self,SIGNAL("valueChanged(int)"),self.checkZero)

    def checkZero(self):
        if self.value() == 0:
            self.zeros += 1
            self.emit(SIGNAL("atzero(int)"),self.zeros)

class FORM(QDialog):
    def __init__(self, parent=None):
        super(FORM, self).__init__(parent)

        dial =  QDial()
        dial.setNotchesVisible(True)
        zeroSpinBox =  ZeroSpinBox()

        layout =  QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(zeroSpinBox)
        self.setLayout(layout)

        self.connect(dial,SIGNAL("valueChanged(int)"),zeroSpinBox.setValue)
        self.connect(zeroSpinBox,SIGNAL("valueChanged(int)"),dial.setValue)
        self.connect(zeroSpinBox,SIGNAL("atzero(int)"),self.announce)


        self.setWindowTitle("Signals and Slots")

    def announce(self,zeros):
        print "ZeroSPinBox has been  at zero " + str(zeros) + "times."




app = QApplication(sys.argv)
form =  FORM()
form.show()

app.exec_()


    
    