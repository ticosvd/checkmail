from __future__ import  print_function
import imaplib
import config
import time

class Profiler(object):
#    def __enter__ (self):
#        self.delta=0
#        self.startTime=time.time()
    def __init__ (self):
        self.delta=0
        self.startTime=time.time()

    def ReadDelta(self):
        self.delta=time.time()-self.startTime
        return self.delta

    def __exit__(self,type,value,traceback):
        pass

def CheckNewEmail(username,password,server):
    p=Profiler()

    mail=imaplib.IMAP4_SSL(server)
    mail.login(username,password)
    mail.list()
    mail.select('INBOX')
    dp=p.ReadDelta()

    result,data=mail.uid('search',None,"UNSEEN")
    if result == 'OK' and  len(data)>0 and data[0]!='':
        return 'New messages, response time '+"%0.3f" % dp
    else:
        return 'No messages, response time '+"%0.3f" % dp


    # return result,data

def mainf():
#    print(config.username,config.password)
    print(CheckNewEmail(config.username,config.password,config.serverimap))

if __name__=="__main__":
    mainf()


