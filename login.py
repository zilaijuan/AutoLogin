# -*- coding: utf-8 -*-
"""
Created on Mon Sep 03 09:55:09 2018

@author: Lenovo
"""

#import beautifullysoup as bs
from requests import sessions
from re import match
from os import path
from ConfigParser import ConfigParser
from argparse import ArgumentParser
import urlparse
#from configobj import ConfigObj

username=''
password=''

parser = ArgumentParser(description='auto login in the network. use -u input username, -p input password. Or use config file "login.conf"')
parser.add_argument('-u', type=str, default = None, help='username')
parser.add_argument('-p', type=str, default=None, help='password')
    
def readConf():
    flag = True
    dirname = path.dirname(path.realpath(__file__))
    conf = path.join(dirname,"login.conf")
    if path.exists(conf):
        cf=ConfigParser()
        cf.read(conf)
        user=cf.get('loginInfo','username')
        passwd=cf.get('loginInfo','password')
        if user is not None:
            global username
            username= user
        else:
            parser.print_help()
            flag = False
        if passwd is not None:
            global password
            password= passwd
        else:
            parser.print_help()
            flag = False
    return flag

def login():
    sina = "http://www.sina.com"
    portal = "https://portalnew.dhu.edu.cn/"
    headers = {
            'Accept':'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection':'keep-alive',
            'Host':'www.sina.com',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/57.0'
            }

    s = sessions.Session() 
    sina = s.get(sina,allow_redirects=False)
    sina.encoding = 'UTF-8-SIG'
#    print(sina.text)
    if match(".*html.*", sina.text) == None:
        switch_hm1 = s.get(sina.headers['Location'],allow_redirects=False)
#        print(switch_hm1.headers)
        switchphp = s.get(portal+switch_hm1.headers['Location'],allow_redirects=False)
#        print(switchphp.cookies.get_dict())
        ck = switchphp.cookies
#        print(ck)
        loginInfo = {'username':username,'password':password}
        #ck = {"PHPSESSID":"t25bao5qm3219mndrhdltgo455"}
#        print(username)
#        print(password)
        resp = s.post('https://portalnew.dhu.edu.cn/post.php',data = loginInfo,cookies=ck,allow_redirects=False)
        resp.encoding = 'UTF-8'
#        print(resp.text)
#        print(resp.headers)
        h = resp.headers
        h = dict(h)
#        print(h)
#        print(type(h))
#        print(h)
#        print(h['location'])
        
        query = resp.headers['Location']
        params = urlparse.parse_qs(query.split('?')[1],True)
#        print(params)
        if(params['p'][0] == 'status'):
            print("Success! ")
        else:
            print(params['error'][0])
        
    else:
        print("Already connect to Internet!")
    
if __name__ == '__main__':
#    parser = argparse.ArgumentParser(description='auto login in the network')
#    parser.add_argument('-u', type=str, default = None)
#    parser.add_argument('-p', type=str, default=None)
    args = parser.parse_args()
#    print(args.u)
#    print(args.p)
    username = args.u
    password = args.p
    flag = True
    if username is None or password is None:
#        print("none")
        dirname = path.dirname(path.realpath(__file__))
        conf = path.join(dirname,"login.conf")
        if path.exists(conf):
            flag = readConf()
        else:
            parser.print_help()
            flag = False
    if flag:
        login()