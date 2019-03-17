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

        self.month = ('')
        self.day = ('')
        self.hour = ('')
        self.minute = ('')
        self.am_pm = ('')

#--------------update date/time--------o

        self.timer  = QTimer()
        self.timer.timeout.connect(self.update_time_date__)
        self.timer.start(1000)


    
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



#-------------function calls--------o

        
        self.labels__()
        self.initGUI()



    def labels__(self):

#---------------month label
        
        
        self.label_month = QLabel (self)
        self.label_month.setStyleSheet('font-size: 25pt; font-family: Ubuntu;')
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(0, 0, 153, 95))#<--change label color
        self.label_month.setPalette(self.palette)
        
        self.label_month.setText      (self.month)#<---value from psutil:boot
        #self.label_arch.setWordWrap  (True)#<---------allow more text in label----o
        self.label_month.setAlignment (Qt.AlignLeft)
        self.label_month.move         (10,20)
##        self.label_month.adjustSize ()#<-----------adj label size---o
        self.label_month.raise_()

        
#---------------comma label
        
       
        self.label_comma = QLabel (self)
        self.label_comma.setStyleSheet('font-size: 25pt; font-family: Ubuntu;')
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(5,25,25, 95))#<--change label color
        self.label_comma.setPalette(self.palette)
        
        self.label_comma.setText      (',')#<---value from psutil:boot
        #self.label_arch.setWordWrap  (True)#<---------allow more text in label----o
        self.label_comma.setAlignment (Qt.AlignLeft)
        self.label_comma.move         (102,20)
##        self.label_comma.adjustSize ()#<-----------adj label size---o
        self.label_comma.raise_()

        
#--------------- day label
        
        
        self.label_day = QLabel (self)
        self.label_day.setStyleSheet('font-size: 25pt; font-family: Ubuntu;')
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(5,25,55, 95))#<--change label color
        self.label_day.setPalette(self.palette)
        
        self.label_day.setText      (str(self.day))#<---value from psutil:boot
        #self.label_arch.setWordWrap  (True)#<---------allow more text in label----o
        self.label_day.setAlignment (Qt.AlignLeft)
        self.label_day.move         (105,20)
##        self.label_day.adjustSize ()#<-----------adj label size---o
        self.label_day.raise_()


#---------------hour label
        
        
        self.label_hour = QLabel (self)
        self.label_hour.setStyleSheet('font-size: 25pt; font-family: Ubuntu;')
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(5,25,25, 95))#<--change label color
        self.label_hour.setPalette(self.palette)
        
        self.label_hour.setText      (self.hour)#<---value from psutil:boot
        #self.label_arch.setWordWrap  (True)#<---------allow more text in label----o
        self.label_hour.setAlignment (Qt.AlignLeft)
        self.label_hour.move         (155,20)
##        self.label_hour.adjustSize ()#<-----------adj label size---o
        self.label_hour.raise_()

#---------------minute label
        
        
        self.label_min = QLabel (self)
        self.label_min.setStyleSheet('font-size: 25pt; font-family: Ubuntu;')
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(5,25,25, 95))#<--change label color
        self.label_min.setPalette(self.palette)
        
        self.label_min.setText      (str(self.minute))#<---value from psutil:boot
        #self.label_arch.setWordWrap  (True)#<---------allow more text in label----o
        self.label_min.setAlignment (Qt.AlignLeft)
        self.label_min.move         (200,20)
##        self.label_min.adjustSize ()#<-----------adj label size---o
        self.label_min.raise_()


#-------------------am/pm label --------------------------o
        
        
        self.label_am_pm = QLabel (self)
        self.label_am_pm.setStyleSheet('font-size: 18pt; font-family: Ubuntu;')
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(5,25,25, 95))#<--change label color
        self.label_am_pm.setPalette(self.palette)
        
        self.label_am_pm.setText      (str(self.am_pm))#<---value from psutil:boot
        #self.label_am_pm.setWordWrap  (True)#<---------allow more text in label----o
        self.label_am_pm.setAlignment (Qt.AlignLeft)
        self.label_am_pm.move         (250,25)
##        self.label_am_pm.adjustSize ()#<-----------adj label size---o
        self.label_am_pm.raise_()
##        self.label_am_pm.show()

        


    def update_time_date__(self):


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



#-----------------am/pm-------------------o

        self.hour = self.time[3]
        if self.hour in range(12,23):
            self.am_pm = ('p.m.')
        elif self.hour in range(0,11):
            self.am_pm = ('a.m.')
        else:
            pass


#--------------convert form military to normal time-----o

        if self.hour >= (13):
            self.hour = self.hour - 12
        elif self.hour == (0):
            self.hour = 12
        self.hour = str(self.hour) + ':'

        #print(self.hour)
        
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

        
        self.label_month.setText      (str(self.month))
        self.label_day.setText      (str(self.day))
        self.label_hour.setText      (str(self.hour))
        self.label_min.setText      (str(self.minute))
        self.label_am_pm.setText      (str(self.am_pm))



    def initGUI(self):

        self.setWindowFlags(Qt.FramelessWindowHint # hides the window controls     
                                | Qt.ToolTip
                                | Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
                        #position  #size
        self.setGeometry(1560,50, 350,525)#x,y  size,size
        self.setWindowTitle('date/time')
        self.move(200, 20)
        self.resize(500,350)
        
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
