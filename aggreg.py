# -*- coding: utf-8 -*-
from __future__ import  print_function
import config
import time
import sqlite3
import datetime
import matplotlib.pyplot as plt
from matplotlib import dates


class ApplyData:
    def __init__(self):
        self.database=config.database_for_check
        self.conn=sqlite3.connect(self.database)

    def SaveData(self,datatime,response):
        c=self.conn.cursor()
        c.execute("INSERT INTO time1 VALUES(?,?)",(datatime,response))
        for bb in range (0,120):
            try:
                self.conn.commit()
            except  sqlite3.Error:
                print ('Database is locked !!! ')
                time.sleep(1)
        return 0

    def ShowDatatimes(self,times,timef):
       c=self.conn.cursor()
       return c.execute("SELECT datetime from time1 where datetime BETWEEN ? and ?",(times,timef))

    def Showdata(self,times,timef):
       c=self.conn.cursor()
       return c.execute("SELECT response from time1 where datetime BETWEEN ? and ?",(times,timef))

    def ShowChart(self,times,timef):
       fig=plt.figure(figsize=(16,8),dpi=1200)
       plt.xlabel('Time')
       plt.ylabel('Response')
       plt.title('Report: response of Yandex imap servers in last 24hours')
       hmft=dates.DateFormatter('%m/%d %H:%M:%S')

       yyd=map ((lambda x: x[0]),self.Showdata(times,timef).fetchall())
       xxd=map((lambda x: dates.date2num(datetime.datetime.fromtimestamp(x[0]))),self.ShowDatatimes(times,timef).fetchall())
       print ([xxd[0],xxd[-1],yyd[0],yyd[-1]], len(xxd))
       ax=plt.gca()
       ax.xaxis.set_major_formatter(hmft)

       plt.locator_params(axis='x',nbins=20)
       plt.xticks(size=8,rotation=15)
       plt.yticks(size=8)
       plt.plot(xxd,yyd,'r-')
     #  plt.autoscale(tight=True)
       plt.grid()

       fig.savefig("ddd.png")







def mainf():
#    print(config.username,config.password)
    dd=[0.1,2,0.77,24]
    da=ApplyData()
    for s1 in dd:
  #      tt=time.mktime(time.localtime()).__int__()
        tt=time.mktime(time.localtime())
        print (s1 , " " ,tt)
#        da.SaveData(tt,s1)
        time.sleep(1)

    tt2=time.mktime(time.localtime())

    for d2 in da.Showdata(tt2-86400,tt2):
        print (d2[0])

    da.ShowChart(0,tt2)

if __name__=="__main__":
    mainf()


