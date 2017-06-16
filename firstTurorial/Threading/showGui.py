# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showUI.ui'
#
# Created: Fri Jun 09 18:02:25 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName("mainDialog")
        mainDialog.resize(274, 54)
        self.lineEdit = QtGui.QLineEdit(mainDialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.showButton = QtGui.QPushButton(mainDialog)
        self.showButton.setGeometry(QtCore.QRect(190, 20, 75, 23))
        self.showButton.setObjectName("showButton")

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)
        mainDialog.setTabOrder(self.showButton, self.lineEdit)

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(QtGui.QApplication.translate("mainDialog", "mainDialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setPlaceholderText(QtGui.QApplication.translate("mainDialog", "What is your name ?", None, QtGui.QApplication.UnicodeUTF8))
        self.showButton.setText(QtGui.QApplication.translate("mainDialog", "Show", None, QtGui.QApplication.UnicodeUTF8))



