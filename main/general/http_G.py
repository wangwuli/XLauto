# -*- coding: utf-8 -*-
'''
@author: liww liww@cenboomh.com
@file: http_G.py
@time: 2020/1/15 16:47
@desc:
'''
import os
import re
import urllib.request
import http.cookiejar
import requests


class HttpClass():

    def __init__(self, username='', password='', headers='', timeout=300):
        if not headers:
            self.headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        else:
            self.headers = headers
            self.timeout = timeout
            self.session = requests.session()
            self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor)


    def save_verification_code_img(self, home_page='', domain_name='', research_str='', down_location='./'):
        """
        将验证码图片保存到本地
        :param home_page: example{ www.baidu.com/login }
        :param research_str: example { src="(.*?)" onclick="reloadVerifyCode }
        :return:
        """
        response = self.opener.open(home_page)
        if response.geturl() == home_page:
            html_text = response.read().decode('utf-8')
            imgurl = re.search(research_str, html_text)
            if domain_name:
                url = domain_name + imgurl.group(1)
            else:
                url = imgurl.group(1)
        imgb = self.opener.open(url)
        local_file = open(os.path(down_location, 'vv.jpg'), 'wb')
        local_file.write(imgb.read())
        local_file.close()

    #def get_csrf_token(self):




