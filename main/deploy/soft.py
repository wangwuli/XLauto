# -*- coding: utf-8 -*-
'''
@author: liww liww@cenboomh.com
@file: soft.py
@time: 2019/12/5 10:06
@desc:
'''

from . import deploy
from flask import current_app

@deploy.route('/deploy/soft')
def login():
    return "test"