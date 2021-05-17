#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 9; CPH1923 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36')]


def keluar():
	print "\033[0;39m[!] \x1b[0;39mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO  #####
logo = """ 
print("✾●●✦WELLCOM TO BABA KHATRA✦●●✾")
print("❍❍❍❍❍❍❍❍✬✥✬❍❍❍❍❍❍❍❍")
print("៚CREATED BY : BABA KHATRAツ")
print("៚FACEBOOK : https://www.facebook.com/RE4L.H4CK3R")
print("៚COUNTRY : NEPAL⚒⚒")
print("៚✮✦NEPALI HACKER✦✮")
print("៚DESIGNER⚒RAHUL MISHRA")
print("៚ⓓⓞⓝⓣ ⓒⓞⓟⓨ ⓜⓨ ⓢⓒⓡⓘⓟⓣ")
print("❍❍❍❍❍❍❍❍✬✥✬❍❍❍❍❍❍❍❍")
print("✾●●✦WELLCOM TO BABA KHATRA✦●●✾")
print("❍❍❍❍❍❍❍❍✬✥✬❍❍❍❍❍❍❍❍")
from requests.exceptions import ConnectionError
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N950N Build/NMF26X) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188828013;FBCR/Advance Info Service;FBMF/samsung;FBDV/SM-N950N;FBSV/5.1.1;FBCA/x86;armeabi-v7a;FBDM{density=2.0,width=900,height=1600};FB_FW;FBRV/0;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
os.system('termux-setup-storage')
os.system('clear')
logo = '\n\n\x1b[1;92m
CorrectUsername = 'baba'
loop = 'true'
while loop == 'true':
    print logo
    print '\x1b[1;97m               FIRST STEP LOGIN'
    print '\x1b[1;97m'
    print '\x1b[1;97m '
    username = raw_input('              \x1b[1;94mTOOL USERNAME: ')
    if username == CorrectUsername:
        print '\x1b[1;95m '
        print '         ||\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2 WELLCOME \xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2|| '
        time.sleep(5)
        loop = 'false'
        print '\x1b[1;92m '
        print '               ACTIVATION START ! '
        time.sleep(10)
        print ' FREE MODE ACTIVATE !'
        os.system('clear')
    else:
        print ' FREE MODE ACTIVATE !'
        os.system('clear')

def reg():
    os.system('clear')
    print logo
    print ''
    print '\t    Generating connection'
    print ''
    print ''
    print '\x1b[1;93m            Connecting...'
    time.sleep(5)
    print ''
    print ''
    print '\x1b[1;92m  [Connected With BABA KHATRA]'
    print ''
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd RRR && npm install')
    os.system('cd RRR && node index.js &')
    os.system('clear')
    time.sleep(5)
    reg2()
