# Solar
# handsome
from WYGL.first.addperson import *
from HTMLTestRunner import HTMLTestRunner
import time
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
import os

dis = unittest.defaultTestLoader.discover ('WYGL/first', pattern ='addperson.py')

def pao () :
    t1 = time.strftime ('%Y-%m-%d-%H-%M-%S')
    t2 = t1 + '_result.html'
    lujing = 'WYGL/HTML_Port/' + t2
    lujing1 = open (lujing,'wb')
    runs = HTMLTestRunner (stream = lujing1, verbosity = 2, title = '物业管理添加居民', description = '详情如下')
    runs.run (dis)
    lujing1.close ()

def email (wenjian) :
    sever = 'smtp.qq.com'
    port = 465
    us1 = '1054989422@qq.com'
    pw1 = 'rxnvcvqfulwebcgh'
    rev = '1054989422@qq.com'

    file = open (wenjian,'rb')
    all2 = file.read ()
    file.close ()

    message = MIMEMultipart ()
    message ['from'] = 'Solar'
    message ['to'] = rev
    message ['subject'] = '物业管理系统新增居民正确流程测试用例'

    body = MIMEText (all2,'html','utf-8')
    message.attach (body)

    fu = MIMEText (all2,'base64','utf-8')
    fu ['Content-Type'] = 'application/octet-stream'
    fu ['Content-Disposition'] = 'attachment; filename = "WYGL_Test_Port.html"'
    message.attach (fu)

    smtp = smtplib.SMTP_SSL (sever,port)
    smtp.login (us1,pw1)
    smtp.sendmail (us1,rev,message.as_string ())
    smtp.quit ()

pao ()

lujing2 = os.listdir ('WYGL/HTML_Port')
lujing3 = 'WYGL/HTML_Port/' + lujing2 [-1]
email (lujing3)