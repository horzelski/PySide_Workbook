# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\user\atri\PySide\firstTurorial\contaxtMenu\contextbutUI.ui'
#
# Created: Tue Jun 13 23:17:41 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 70, 75, 23))
        self.pushButton.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtGui.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(150, 170, 82, 17))
        self.radioButton.setObjectName("radioButton")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.radioButton.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("Dialog", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))

