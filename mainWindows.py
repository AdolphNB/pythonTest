import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QFrame, QLabel,
                QLineEdit, QGridLayout)
from PyQt5.QtGui import QColor,QFont
from PyQt5.QtCore import QTimer, QThread

from StockInfo import *


class MainDaemonThread(QThread):
    def __init__(self):
        super().__init__()
        self.srcData = 0
        self.dataOpt = 0
    
    def run(self):
        while True:
            if self.srcData <= self.dataOpt:
                print("Thread>>>>")
            time.sleep(1)
    
    def compareValue(srcData, datOpt):
        self.srcData = srcData
        self.dataOpt = datOpt
        


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.initLabel()
        self.initButton()
        self.initStockInfo()
        self.initQLineEdit()
        self.mainDTh = MainDaemonThread()
        self.mainDTh.start()
        self.setWindowTitle('PyQt5-Label')
        self.setGeometry(300, 300, 280, 170)
        self.show()
        
    def initStockInfo(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.operate)
        self.timer.start(2000)
        self.stock = StockInfo('600550')
    
    def initLabel(self):
        self.label = QLabel(self)
        self.label.setText("000000")
        self.label.move(140,25)
        self.label.setFont(QFont("0",20,QFont.Bold))
    
    def initQLineEdit(self):
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(10,100)
        self.lineEdit.setText('600550')
    
    #this button is a flag that start/stop stock-data update by press or release it.
    def initButton(self):
        self.qbtn = QPushButton("START", self)
        self.status = False
        self.qbtn.clicked.connect(self.signalBtn_START_STOP)
        self.qbtn.move(10,30)
    
    #this method is a SIGNAL-response callback method, initialize method see initButton()
    def signalBtn_START_STOP(self):
        if self.status == False:
            self.status = True
            self.stock.setPostStatus(True)
            self.qbtn.setText("STOP")
            self.stock.resetStockNumber(self.lineEdit.text())
            #print("START")
        else:
            self.status = False
            self.stock.setPostStatus(False)
            self.qbtn.setText("START")
            #print("STOP")
    
    def operate(self):
        buf = self.stock.getCurrentPrice()
        self.label.setText(buf)
    
    def closeEvent(self, event):
        print("closeEvent.......")
    
    def mousePressEvent(self, event):
        print("hello")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
