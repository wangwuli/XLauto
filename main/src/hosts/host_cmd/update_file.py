# -*- coding: utf-8 -*-
'''
@author: liww
@file: update_file.py
@time: 2020/5/15 14:41
@desc:
'''
from flask import request
from src.hosts import host_cmd


@host_cmd.route('/host_m/update_file', methods=['POST'])
def update_file():
    f = request.files['file']