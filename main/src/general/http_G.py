# -*- coding: utf-8 -*-
'''
@author: liww
@file: http_G.py
@time: 2020/1/15 16:47
@desc:
'''
import os
import re
import urllib.request
import requests


class HttpClass():

    def __init__(self, headers='', timeout=300):
        if not headers:
            self.headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        else:
            self.headers = headers
            self.timeout = timeout
            self.session = requests.session()
            self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor)

    def open_html(self, home_page):
        self.response = self.opener.open(home_page)
        if self.response.geturl() == home_page:
            self.html_text = self.response.read().decode('utf-8')
            return True
        else:
            return False

    def save_verification_code_img(self, domain_name='', research_str='', down_location='./'):
        """
        将验证码图片保存到本地
        :param home_page: example{ www.baidu.com/login }
        :param research_str: example { src="(.*?)" onclick="reloadVerifyCode }
        :return:
        """
        imgurl = re.search(research_str, self.html_text)
        if domain_name:
            url = domain_name + imgurl.group(1)
        else:
            url = imgurl.group(1)

        imgb = self.opener.open(url)
        local_file = open(os.path(down_location, 'vv.jpg'), 'wb')
        local_file.write(imgb.read())
        local_file.close()

    def get_csrf_token(self, research_str=''):
        """
        获取csrf_token
        :param research_str: { "<input type='hidden' name='csrftoken' value='(.*?)'/>" }
        :return:
        """
        self.csrf_token0 = re.search(research_str, self.html_text).group(1)

    def login(self, loginurl, params, method='POST'):
        """
        登陆或者打开页面
        :param loginurl:
        :param params: {'userCode':'liww@cenboom.com', 'userPasswd':'123456', 'verifyCode':'4567', 'csrftoken':'45asdiuch' }
        :return:
        """
        self.request = urllib.request.Request(loginurl, urllib.parse.urlencode(params).encode('utf-8'),
                                              headers=self.headers, method=method)
        self.response = self.opener.open(self.request)
        self.html_text = str(self.response.read(), 'utf-8')
