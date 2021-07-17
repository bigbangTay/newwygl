# Solar
# handsome
import random

# 打开文件获取帐号密码
url = ''
us = ''
pw = ''
with open ('WYGL/data/login.txt','r',encoding = 'utf-8') as rfile :
    result = rfile.read ()
    result1 = result.split (',')
    url = result1 [0]
    us = result1 [1]
    pw = result1 [2]

# 获取随机居民账号
houzhui = random.randint (100,99999)
jmus = 'Solar' + str (houzhui)

# 获取随机居民姓名
name = ''
with open ('WYGL/data/name.txt','r',encoding = 'utf-8') as rfile1 :
    all = rfile1.read ()
    all1 = all.split ('\n')
    suoyin = random.randint (0,len (all1 [0]) - 1)
    xing = all1 [0][suoyin]
    suoyin1 = random.randint (0,len (all1 [1]) - 1)
    ming = all1 [1][suoyin1]
    name = xing + ming

# 身份证
year = str (random.randint (1960,2021))
month = str (random.randint (1,9))
day = str (random.randint (10,28))
san = str (random.randint (100,999))
last = [str (i) for i in range (10)] + ['X']
last1 = random.choice (last)
idcard = f'510122{year}0{month}{day}{san}{last1}'

# sex随机
sex = ['/html/body/div[5]/div[1]/div[1]/ul/li[1]/span','/html/body/div[5]/div[1]/div[1]/ul/li[2]/span']
sex1 = random.choice (sex)

# 电话号码随机
eight = (random.randint (0,9) for i in range (8))
phone = '183'
for i in eight :
    phone += str (i)

# 入住时间随机
ruyear = str (random.randint (2008,2021))
rumonth = random.randint (1,12)
ruday = random.randint (1,28)
if rumonth < 10 and ruday < 10 :
    ru = f'{ruyear}-0{str (rumonth)}-0{str (ruday)}'
elif rumonth < 10 :
    ru = f'{ruyear}-0{str (rumonth)}-{str (ruday)}'
elif ruday < 10 :
    ru = f'{ruyear}-{str (rumonth)}-0{str (ruday)}'
else :
    ru = f'{ruyear}-{str (rumonth)}-{str (ruday)}'