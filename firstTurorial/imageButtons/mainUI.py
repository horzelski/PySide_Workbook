# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created: Tue Jun 13 17:23:38 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName("mainDialog")
        mainDialog.resize(400, 100)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainDialog.sizePolicy().hasHeightForWidth())
        mainDialog.setSizePolicy(sizePolicy)
        mainDialog.setMinimumSize(QtCore.QSize(400, 100))
        mainDialog.setMaximumSize(QtCore.QSize(400, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/RSS-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(mainDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.linkedInButton = QtGui.QPushButton(mainDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linkedInButton.sizePolicy().hasHeightForWidth())
        self.linkedInButton.setSizePolicy(sizePolicy)
        self.linkedInButton.setMinimumSize(QtCore.QSize(120, 80))
        self.linkedInButton.setMaximumSize(QtCore.QSize(120, 80))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/LinkedIn-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.linkedInButton.setIcon(icon1)
        self.linkedInButton.setIconSize(QtCore.QSize(32, 32))
        self.linkedInButton.setObjectName("linkedInButton")
        self.horizontalLayout.addWidget(self.linkedInButton)
        self.facebookButton = QtGui.QPushButton(mainDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.facebookButton.sizePolicy().hasHeightForWidth())
        self.facebookButton.setSizePolicy(sizePolicy)
        self.facebookButton.setMinimumSize(QtCore.QSize(120, 80))
        self.facebookButton.setMaximumSize(QtCore.QSize(120, 80))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Facebook-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.facebookButton.setIcon(icon2)
        self.facebookButton.setIconSize(QtCore.QSize(32, 32))
        self.facebookButton.setObjectName("facebookButton")
        self.horizontalLayout.addWidget(self.facebookButton)
        self.twitterButton = QtGui.QPushButton(mainDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twitterButton.sizePolicy().hasHeightForWidth())
        self.twitterButton.setSizePolicy(sizePolicy)
        self.twitterButton.setMinimumSize(QtCore.QSize(120, 80))
        self.twitterButton.setMaximumSize(QtCore.QSize(120, 80))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/Twitter Bird-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twitterButton.setIcon(icon3)
        self.twitterButton.setIconSize(QtCore.QSize(32, 32))
        self.twitterButton.setObjectName("twitterButton")
        self.horizontalLayout.addWidget(self.twitterButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(QtGui.QApplication.translate("mainDialog", "Pick and OS", None, QtGui.QApplication.UnicodeUTF8))
        self.linkedInButton.setText(QtGui.QApplication.translate("mainDialog", "LinkedIn", None, QtGui.QApplication.UnicodeUTF8))
        self.facebookButton.setText(QtGui.QApplication.translate("mainDialog", "Facebook", None, QtGui.QApplication.UnicodeUTF8))
        self.twitterButton.setText(QtGui.QApplication.translate("mainDialog", "Twiter", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
