# coding: utf-8

import urllib
import urllib2
import re
import pdb
import os
import cookielib
import StringIO
import ConfigParser

class Smzdm:

    def __init__(self):
        self.cookies = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        self.headers = {
            'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36',
            'Referer' : 'http://www.smzdm.com/',
            'Origin' : 'http://www.smzdm.com/'
        }

    # 登录
    def login(self, account):
        user_login = account['username']
        user_pass = account['password']
        rememberme = 1
        is_pop = 1
        url = "http://www.smzdm.com/user/login/jsonp_check?callback=jQuery111004638147682417184_1439357637485&user_login=%s&user_pass=%s&rememberme=%s&is_pop=%s&captcha=&_=1439357637487" % (user_login, user_pass, rememberme, is_pop)
        request = urllib2.Request(url, headers = self.headers)
        self.opener.open(request)

    # 退出
    def logout(self):
        url = "http://www.smzdm.com/user/logout"
        request = urllib2.Request(url, headers = self.headers)
        self.opener.open(request)

    # 签到
    def checkin(self):
        url = "http://www.smzdm.com//user/qiandao/jsonp_checkin"
        request = urllib2.Request(url, headers = self.headers)
        self.opener.open(request)


    def start_checkin(self):
        parser = ConfigParser.RawConfigParser()
        parser.read("account.ini")
        for user in parser.sections():
            account = {}
            account['username'] = parser.get(user, 'username')
            account['password'] = parser.get(user, 'password')
            smzdm.login(account)
            smzdm.checkin()
            smzdm.logout()

smzdm = Smzdm()
smzdm.start_checkin()
