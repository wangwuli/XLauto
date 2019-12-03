# -*- coding: utf-8 -*-
'''
@author: liww liww@cenboomh.com
@file: logio.py
@time: 2019/11/22 17:10
@desc:
'''

from . import services

@services.route('/login')
def login():
    return "hello world"