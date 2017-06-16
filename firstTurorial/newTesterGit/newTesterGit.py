import sys
from PySide.QtCore import *
from PySide.QtGui import *

#super test 

class FORM(QDialog):
    def __init__(self, parent=None):
        super(FORM, self).__init__(parent)
        dial =  QDial()
        dial.setNotchesVisible(True)
        spinBox =  QSpinBox()

        layout =  QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinBox)
        self.setLayout(layout)

        self.connect(dial,SIGNAL("valueChanged(int)"),spinBox.setValue)
        self.connect(spinBox,SIGNAL("valueChanged(int)"),dial.setValue)


        self.setWindowTitle("Signals and Slots")



app = QApplication(sys.argv)
form =  FORM()
form.show()

app.exec_()
