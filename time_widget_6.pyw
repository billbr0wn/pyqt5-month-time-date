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
        self.weekday = ('')
        
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

###---------------month label
##        
        
        self.label_month = QLabel (self)
        self.label_month.setStyleSheet('font-size: 25pt; font-family: Ubuntu;')
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(0, 0, 153, 95))#<--change label color
        self.label_month.setPalette(self.palette)
##        
        self.label_month.setText      (self.month)#<---value from psutil:boot
##        #self.label_arch.setWordWrap  (True)#<---------allow more text in label----o
        self.label_month.setAlignment (Qt.AlignRight)
        self.label_month.move         (0,35)
####        self.label_month.adjustSize ()#<-----------adj label size---o
        self.label_month.raise_()

        
#---------------comma label
        
       
        self.label_comma = QLabel (self)
        self.label_comma.setStyleSheet('font-size: 25pt; font-family: Ubuntu;')
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(5,25,25, 95))#<--change label color
        self.label_comma.setPalette(self.palette)
        
        self.label_comma.setText      (',')#<---value from psutil:boot
        #self.label_arch.setWordWrap  (True)#<---------allow more text in label----o
##        self.label_comma.setAlignment (Qt.AlignLeft)
        self.label_comma.move         (102,35)
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
        self.label_day.move         (112,35)
##        self.label_day.adjustSize ()#<-----------adj label size---o
        self.label_day.raise_()


#---------------hour label
        
        
        self.label_hour = QLabel (self)
        self.label_hour.setStyleSheet('font-size: 25pt; font-family: Ubuntu;')
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(5,25,25, 95))#<--change label color
        self.label_hour.setPalette(self.palette)
        
        self.label_hour.setText      (self.hour)#<---value from psutil:boot
        #self.label_arch.setWordWrap  (True)#<---------allow more text in label----o
        self.label_hour.setAlignment (Qt.AlignRight)
        self.label_hour.move         (105,35)
##        self.label_hour.adjustSize ()#<-----------adj label size---o
        self.label_hour.raise_()

#---------------minute label
        
        
        self.label_min = QLabel (self)
        self.label_min.setStyleSheet('font-size: 25pt; font-family: Ubuntu;')
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(5,25,25, 95))#<--change label color
        self.label_min.setPalette(self.palette)
        
        self.label_min.setText      (str(self.minute))#<---value from psutil:boot
        #self.label_arch.setWordWrap  (True)#<---------allow more text in label----o
        self.label_min.setAlignment (Qt.AlignRight)
        self.label_min.move         (143,35)
##        self.label_min.adjustSize ()#<-----------adj label size---o
        self.label_min.raise_()


#-------------------am/pm label --------------------------o
        
        
        self.label_am_pm = QLabel (self)
        self.label_am_pm.setStyleSheet('font-size: 18pt; font-family: Ubuntu;')
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(5,25,25, 95))#<--change label color
        self.label_am_pm.setPalette(self.palette)
        
        self.label_am_pm.setText      (str(self.am_pm))#<---value from psutil:boot
        #self.label_am_pm.setWordWrap  (True)#<---------allow more text in label----o
        self.label_am_pm.setAlignment (Qt.AlignRight)
        self.label_am_pm.move         (195,40)
##        self.label_am_pm.adjustSize ()#<-----------adj label size---o
        self.label_am_pm.raise_()
##        self.label_am_pm.show()



#------------------- weekday label------------------o

        
        self.label_weekday = QLabel (self)
        self.label_weekday.setStyleSheet('font-size: 28pt; font-family: Ubuntu;')
        self.pallete = self.palette.setColor(QPalette.Foreground,QColor.fromRgb(50,25,205, 95))#<--change label color
        self.label_weekday.setPalette(self.palette)
        
        self.label_weekday.setText      (str(self.weekday))#<---value from psutil:boot
        self.label_weekday.setAlignment (Qt.AlignLeft)
        self.label_weekday.move         (310,35)
        self.label_weekday.raise_()



    def update_time_date__(self):


        self.time = time.localtime()

#--------------set day of the week
        
        if self.time[6] == (0):
            self.weekday = 'Mon'
        elif  self.time[6] == (1):
            self.weekday = 'Tues'
        elif  self.time[6] == (2):
            self.weekday = 'Wed'
        elif  self.time[6] == (3):
            self.weekday = 'Thur'
        elif  self.time[6] == (4):
            self.weekday = 'Fri'
        elif  self.time[6] == (5):
            self.weekday = 'Sat'
        elif  self.time[6] == (6):
            self.weekday = 'Sun'
        #print(self.weekday)


#----
          
        if self.time[1] == (1):
            self.month = 'Jan'
        elif self.time[1] == (2):
            self.month = 'Feb'
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
            self.month = 'Aug'
        elif self.time[1] == (9):
            self.month = 'Sept'
        elif self.time[1] == (10):
            self.month = 'Oct'
        elif self.time[1] == (11):
            self.month = 'Nov'
        elif self.time[1] == (12):
            self.month = 'Dec'
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
        self.label_weekday.setText      (str(self.weekday))



    def initGUI(self):

        self.setWindowFlags(Qt.FramelessWindowHint # hides the window controls     
                                | Qt.ToolTip
                                | Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
                        #position  #size
        self.setGeometry(1560,50, 350,525)#x,y  size,size
        self.setWindowTitle('date/time')
        self.move(200, 20)
        self.resize(500,375)
        
        self.setVisible(False)
##        self.exitOnClose = False
        
        self.setGraphicsEffect(self.effect)
##        self.trayIcon = QSystemTrayIcon(QIcon(), self)
##        self.trayIcon.show()
        self.raise_()
        self.show()



        

if __name__ == '__main__':
    app = QApplication([])
    #tray = SystemTrayIcon()
    _Win_ = _Window_()
    app.exec_()
