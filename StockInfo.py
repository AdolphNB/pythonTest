'''
Date:2018-02-02
Author: adolphZhang(304633698@qq.com)
This module write for get stock information, you can enter a number to this Class
and then could be get message that what want to get.
'''
import re
import time
import threading
from urllib.request import urlopen

class StockInfo():
    
    def __init__(self, values = '600550'):
        self.stockNumber = values
        html=urlopen('http://hq.sinajs.cn/list=sh%s' % self.stockNumber)
        self.cBuffer = html.read().decode('gbk')
        self.buff = self.cBuffer.split(",")
        self.ThreadCtrl = False
        '''Must use daemon thread, if not, main thread exit, this this thread will
        continue running.'''
        self.thrd = threading.Thread(target=self.postValue, daemon = True).start()
    
    def postValue(self):
        while True:
            if self.ThreadCtrl == True:
                html=urlopen('http://hq.sinajs.cn/list=sh%s' % self.stockNumber)
                self.cBuffer = html.read().decode('gbk')
                self.buff = self.cBuffer.split(",")
                #print(self.buff)
            time.sleep(2)
            
    def resetStockNumber(self, values):
        self.stockNumber = values
    
    def setPostStatus(self, opt):
        self.ThreadCtrl = opt
    
    def getNumber(self):
        numBuf = re.findall(r'var hq_str_(.*)=', self.buff[0], re.S|re.M)
        return numBuf[0]
    
    def getName(self):
        numName = re.findall(r'="(.*)', self.buff[0], re.S|re.M)
        return numName[0]
    
    def getOpenPrice(self):
        return self.buff[1]
    
    def getLastClosingPrice(self):
        return self.buff[2]
    
    def getCurrentPrice(self):
        return self.buff[3]
    
    def getHighestPrice(self):
        return self.buff[4]
    
    def getLowestPrice(self):
        return self.buff[5]
        
    def getCurrentBuy1(self):
        return self.buff[6]

    def getCurrentSale1(self):
        return self.buff[7]
    
    def getCurrentVolume(self):
        return self.buff[8]
    
    def getCurrentYield(self):
        return self.buff[9]



if __name__ == '__main__':
    stc = StockInfo("600122")
    
    while True:
        print(stc.getName())
        print(stc.getNumber())
        print(stc.getOpenPrice())
        print(stc.getLastClosingPrice())
        print(stc.getCurrentPrice())
        print(stc.getHighestPrice())
        print(stc.getLowestPrice())
        print(stc.getCurrentBuy1())
        print(stc.getCurrentSale1())
        print(stc.getCurrentVolume())
        print(stc.getCurrentYield())
        time.sleep(5);
    
    