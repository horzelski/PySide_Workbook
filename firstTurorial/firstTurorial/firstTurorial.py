import sys
import PySide
from PySide.QtCore import *
from PySide.QtGui import *
import time

app =  QApplication(sys.argv)

try:
    due =  QTime.currentTime()
    message =  'Aleart'

    if len(sys.argv) < 2:
        raise ValueError

    hours,minutes =  (sys.argv[1]).split(':')
    due =  QTime(int(hours),int(minutes))

    if not due.isValid():
        raise ValueError
    
    if len(sys.argv) > 2 :
        message =  ' '.join(sys.argv[2:])

except ValueError:
    message =  "Usage: firstTutorial.py  HH:MM [optional message ]" #24 hour clock

while QTime.currentTime() < due:
    time.sleep(10)

lable =  QLabel("<font color =  red size =  72 > <b>" + message + "</b> </font>")
lable.setWindowFlags(Qt.SplashScreen)
lable.show()

QTimer.singleShot(20000,app.quit)
app.exec_()
    
    
