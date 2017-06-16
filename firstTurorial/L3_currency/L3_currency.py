import sys
from PySide.QtCore import *
from PySide.QtGui import *
import urllib2 


class Form(QDialog):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)

        date =  self.getdate()
        rates =  sorted(self.rates.keys())

        dateLable =  QLabel(date)
        self.fromComboBox =  QComboBox()
        self.fromComboBox.addItems(rates)
        self.fromSpinBox =  QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01,10000000.00)
        self.fromSpinBox.setValue(1.00)
        self.toComboBox =  QComboBox()
        self.toComboBox.addItems(rates)
        self.toLable =  QLabel("1.00")

        grid =  QGridLayout()
        grid.addWidget(dateLable,0,0)
        grid.addWidget(fromComboBox,1,0)
        grid.addWidget(fromSpinBox,1,1)
        grid.addWidget(toComboBox,2,0)
        grid.addWidget(toLable,2,1)
        self.setLayout(grid)


        self.connect(self.fromComboBox , SIGNAL("currentIndexChanged(int)"),self.updateUI)
        self.connect(self.toComboBox , SIGNAL("currentIndexChanged(int)"),self.updateUI)
        self.connect(self.fromSpinBox , SIGNAL("valueChanged (double)"),self.updateUI)


    def updateUI(self):
        to =  self.toComboBox.currentText()
        from_ =  self.fromComboBox.currentText()
        amount  = (self.rates[from_]/self.rates[to] * self.fromSpinBox.value())
        self.toLable.setText("%0.2f" % amount)

    def getdate(self):
        self.rates =  {}

        try:
            date  =  "Unknown"
            fh =  "E:\user\atri\eurofxref.csv"
            for line in fh:
                line =  line.rstrip()
                if not line or line.startswith(("#","Closing")):
                    continue 
                fields =  line.split(",")
                if line.startswith("Date"):
                    date =  fields[-1]

                else:
                    try:
                        value = float(fields[-1])
                    except ValueError:
                        pass 
                return "Exchnage rates date: " + date 

        except Exception, e:
            return "failed to download "


    def getFiles(self):
        print 'Named explicitly:'
        for name in glob.glob(path+'subdir/*'):
            print '\t', name
        print 'Named with wildcard:'
        for name in glob.glob(path+'*/*'):
            print '\t', name


app =  QApplication(sys.argv)
form =  Form()
form.show()
app.exec_()





         

    
