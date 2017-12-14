#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from random import randint



WINDOW_HEIGHT=770
WINDOW_WIDTH=500
SCRIPT_PATH='/Users/lukyanyan/desktop/artware/tinder.py'
num_buttons=0

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
	self.personID = randint(1,5)-1
        self.initGUI()

    def initGUI(self):

        self.setGeometry(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowTitle("Tinder")

        self.background = Background(self, self.personID, WINDOW_WIDTH, WINDOW_HEIGHT)

	self.buttonNext = QPushButton(self)
	self.buttonNext.setIcon(QIcon('images/cross.png'))
	self.buttonNext.setIconSize(QtCore.QSize(150,150))
	self.buttonNext.setGeometry(0,WINDOW_HEIGHT-150,150,150)
	self.buttonNext.clicked.connect(self.handleNextButton)

	self.buttonAccept = QPushButton(self)
	self.buttonAccept.setIcon(QIcon('images/heart.png'))
	self.buttonAccept.setIconSize(QtCore.QSize(150,150))
	self.buttonAccept.setGeometry(WINDOW_WIDTH-150,WINDOW_HEIGHT-150,150,150)
	self.buttonAccept.clicked.connect(self.handleAcceptButton)

	self.buttonYes = QPushButton(self)
	self.buttonYes.setIcon(QIcon('images/yes.png'))
	self.buttonYes.setIconSize(QtCore.QSize(WINDOW_WIDTH,120))
	self.buttonYes.setGeometry(0,WINDOW_HEIGHT-250,WINDOW_WIDTH,120)
	self.buttonYes.clicked.connect(self.handleYesButton)
	self.buttonYes.hide()

	self.buttonQuit = QPushButton(self)
	self.buttonQuit.setIcon(QIcon('images/quit.png'))
	self.buttonQuit.setIconSize(QtCore.QSize(WINDOW_WIDTH,120))
	self.buttonQuit.setGeometry(0,WINDOW_HEIGHT-130,WINDOW_WIDTH,120)
	self.buttonQuit.clicked.connect(self.handleQuitButton)
	self.buttonQuit.hide()


	num_buttons = randint(0,10)
	for i in range(0,num_buttons):
	   print 'Added random button!'
	   self.showRandomButton()
        self.show()

    def handleNextButton(self):
	self.background.showNextPerson()

    def handleAcceptButton(self):
	print 'Button accept pressed!'
	self.buttonAccept.hide()
	self.buttonNext.hide()
	self.background.showFailed()
	self.buttonYes.show()
	self.buttonQuit.show()

	self.update()


    def showRandomButton(self):
	randomButton = RandomButton(self)
	return randomButton

    def handleYesButton(self):
	# todo reset everything to initial state
	print 'And again...'
	QtCore.QProcess.startDetached(SCRIPT_PATH)
	sys.exit(0)

    def handleQuitButton(self):
	# quit the app
	sys.exit(0)


class RandomButton(QWidget):
    def __init__(self, parent):
        super(RandomButton, self).__init__(parent)
        self.initGUI()

    def initGUI(self):
	buttonWidth = 100
	buttonHeight = 100
	buttonRandom = QPushButton(self)
	buttonRandom.setIcon(QIcon('images/annoying.png'))
	buttonRandom.setIconSize(QtCore.QSize(buttonWidth,buttonHeight))
	xrandom = randint(0,WINDOW_WIDTH-buttonWidth)
	yrandom = randint(0,WINDOW_HEIGHT-buttonHeight)
	buttonRandom.setGeometry(xrandom, yrandom, buttonWidth,buttonHeight)
	buttonRandom.clicked.connect(self.hideButton)

    def hideButton(self):
	print 'buttons open: '+str(num_buttons)
	self.hide()

class Background(QWidget):
    def __init__(self, parent, number=0,width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
        super(Background, self).__init__(parent)
	self.personID = number
	self.width=width
	self.height=height
	self.setGeometry(0, 0, width, height)
	self.failed = False

    def showNextPerson(self):
	self.failed = False
	#self.personID = self.personID + 1

	# set random person
	oldPersonID = self.personID
	while True:
		self.personID = randint(1,5)-1
		if self.personID != oldPersonID:
			break

	#if self.personID == 5:
	#   self.personID = 0
	print 'Button cancel pressed! Showing person: '+str(self.personID)
	self.update()

    def showFailed(self):
	self.failed = True
	self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
	picpath = ''
	if not self.failed:
        	picpath = 'images/bg'+str(self.personID)+'.png'
	else:
		picpath = 'images/failed_no_buttons.png'

	pic = QPixmap(picpath).scaled(self.width, self.height,QtCore.Qt.KeepAspectRatio)
        qp.drawPixmap(0,0,self.width,self.height,pic)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = MainWindow()
    sys.exit(app.exec_())
