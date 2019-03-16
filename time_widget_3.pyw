#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.uic import *
import time

#-------------------------------------------------
    
__author__ = '__Bill__'



class _Window_(QMainWindow):
    """
    -------------------(_Time_Gadget_)------------------
    """
    def __init__(self):
        super().__init__()
        print(_Window_.__doc__)


        self.time = time.localtime()

        if self.time[1] == (1):
            self.month = 'January'
        elif self.time[1] == (2):
            self.month = 'Febuary'
        elif self.time[1] == (3):
            self.month = 'March'
        elif self.time[1] == (4):
            self.month = 'April'
        elif self.time[1] == (5):
            self.month = 'May'
        elif self.time[1] == (6):
            self.month = 'June'
        elif self.time[1] == (7):
            self.month = 'July'
        elif self.time[1] == (8):
            self.month = 'August'
        elif self.time[1] == (9):
            self.month = 'September'
        elif self.time[1] == (10):
            self.month = 'October'
        elif self.time[1] == (11):
            self.month = 'November'
        elif self.time[1] == (12):
            self.month = 'December'
        else:
            print('error...')



#--------------convert form military to normal time-----o
            
        self.hour = self.time[3]
        if self.hour >= 12:
            self.hour = self.hour - 12
        self.hour = str(self.hour) + ':'

    
#---minute
            
        self.minute = self.time[4]
        if self.minute == (0):
            self.minute = '0' + str(self.minute)
        if self.minute == (1):
            self.minute = '0' + str(self.minute)
        if self.minute == (2):
            self.minute = '0' + str(self.minute)
        if self.minute == (3):
            self.minute = '0' + str(self.minute)
        if self.minute == (4):
            self.minute = '0' + str(self.minute)
        if self.minute == (5):
            self.minute = '0' + str(self.minute)
        if self.minute == (6):
            self.minute = '0' + str(self.minute)
        if self.minute == (7):
            self.minute = '0' + str(self.minute)
        if self.minute == (8):
            self.minute = '0' + str(self.minute)
        if self.minute == (9):
            self.minute = '0' + str(self.minute)

#------day
        
        self.day = self.time[2]



    
#---------------create drop shadow-------------------o
        
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setBlurRadius(10)
        self.effect.setXOffset(5)
        self.effect.setYOffset(-5)
        self.effect.setColor(Qt.black)


#<--------------- set QPalette for label----------------->#

        self.palette = QPalette()
        self.brush = self.palette.setBrush
        self.background = QPalette.Background
        self.brush(self.background, QBrush(QImage("brushed1")))
        self.setPalette(self.palette)


#---------------month label
        
        self.setStyleSheet('font-size: 25pt; font-family: Ubuntu;')
        self.label_arch = QLabel (self)
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(0, 0, 153, 95))#<--change label color
        self.label_arch.setPalette(self.palette)
        
        self.label_arch.setText      (self.month)#<---value from psutil:boot
        #self.label_arch.setWordWrap  (True)#<---------allow more text in label----o
        self.label_arch.setAlignment (Qt.AlignLeft)
        self.label_arch.move         (10,20)
        self.label_arch.adjustSize ()#<-----------adj label size---o
        self.label_arch.raise_()

        
#---------------comma label
        
        self.setStyleSheet('font-size: 25pt; font-family: Ubuntu;')
        self.label_arch = QLabel (self)
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(5,25,25, 95))#<--change label color
        self.label_arch.setPalette(self.palette)
        
        self.label_arch.setText      (',')#<---value from psutil:boot
        #self.label_arch.setWordWrap  (True)#<---------allow more text in label----o
        self.label_arch.setAlignment (Qt.AlignLeft)
        self.label_arch.move         (100,20)
        self.label_arch.adjustSize ()#<-----------adj label size---o
        self.label_arch.raise_()

        
#--------------- day label
        
        self.setStyleSheet('font-size: 25pt; font-family: Ubuntu;')
        self.label_arch = QLabel (self)
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(5,25,25, 95))#<--change label color
        self.label_arch.setPalette(self.palette)
        
        self.label_arch.setText      (str(self.day))#<---value from psutil:boot
        #self.label_arch.setWordWrap  (True)#<---------allow more text in label----o
        self.label_arch.setAlignment (Qt.AlignLeft)
        self.label_arch.move         (115,20)
        self.label_arch.adjustSize ()#<-----------adj label size---o
        self.label_arch.raise_()


#---------------hour label
        
        self.setStyleSheet('font-size: 25pt; font-family: Ubuntu;')
        self.label_arch = QLabel (self)
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(5,25,25, 95))#<--change label color
        self.label_arch.setPalette(self.palette)
        
        self.label_arch.setText      (self.hour)#<---value from psutil:boot
        #self.label_arch.setWordWrap  (True)#<---------allow more text in label----o
        self.label_arch.setAlignment (Qt.AlignLeft)
        self.label_arch.move         (175,20)
        self.label_arch.adjustSize ()#<-----------adj label size---o
        self.label_arch.raise_()

#---------------minute label
        
        self.setStyleSheet('font-size: 25pt; font-family: Ubuntu;')
        self.label_arch = QLabel (self)
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(5,25,25, 95))#<--change label color
        self.label_arch.setPalette(self.palette)
        
        self.label_arch.setText      (str(self.minute))#<---value from psutil:boot
        #self.label_arch.setWordWrap  (True)#<---------allow more text in label----o
        self.label_arch.setAlignment (Qt.AlignLeft)
        self.label_arch.move         (200,20)
        self.label_arch.adjustSize ()#<-----------adj label size---o
        self.label_arch.raise_()


        
        self.initGUI()



    def initGUI(self):

        self.setWindowFlags(Qt.FramelessWindowHint # hides the window controls     
                                | Qt.ToolTip
                                | Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
                        #position  #size
        self.setGeometry(1560,50, 350,525)#x,y  size,size
        self.setWindowTitle('date/time')
        self.move(200, 20)
        self.resize(500,300)
        
        self.setVisible(False)
        self.exitOnClose = False
        
        self.setGraphicsEffect(self.effect)
##        self.trayIcon = QSystemTrayIcon(QIcon(), self)
##        self.trayIcon.show()
        self.lower()
        self.show()



        

if __name__ == '__main__':
    app = QApplication([])
    #tray = SystemTrayIcon()
    _Win_ = _Window_()
    app.exec_()
