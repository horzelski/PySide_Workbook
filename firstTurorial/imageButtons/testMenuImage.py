# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\user\atri\PySide\firstTurorial\imageButtons\testMenuImage.ui'
#
# Created: Wed Jun 14 00:20:47 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuAaa = QtGui.QMenu(self.menubar)
        self.menuAaa.setObjectName("menuAaa")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBbb = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/LinkedIn-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBbb.setIcon(icon)
        self.actionBbb.setObjectName("actionBbb")
        self.menuAaa.addAction(self.actionBbb)
        self.menubar.addAction(self.menuAaa.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAaa.setTitle(QtGui.QApplication.translate("MainWindow", "aaa", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBbb.setText(QtGui.QApplication.translate("MainWindow", "bbb", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
