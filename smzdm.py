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
        content = self.opener.open(request)
        return content

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

    # 查看是否签到
    def is_checkin(self):
        url = "http://www.smzdm.com/user/info/jsonp_get_current?"
        request = urllib2.Request(url, headers = self.headers)
        response = self.opener.open(request)
        content = response.read()
        pattern = re.compile('\"has_checkin\"\:(.*?),')
        item = re.search(pattern, content)
        if item and item.group(1).strip() == 'true':
            print(u'签到成功！')
        else:
            print(u'签到失败！')

    def start_checkin(self):
        parser = ConfigParser.RawConfigParser()
        parser.read("account.ini")
        for user in parser.sections():
            account = {}
            account['username'] = parser.get(user, 'username')
            account['password'] = parser.get(user, 'password')
            self.login(account)
            self.checkin()
            self.is_checkin()
            self.logout()

smzdm = Smzdm()
smzdm.start_checkin()
