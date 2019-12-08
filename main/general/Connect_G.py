# -*- coding: utf-8 -*-
'''
@author: liww
@file: Connect_G.py
@time: 2019/12/5 17:02
@desc:
'''

class SSHDao():
    def __init__(self):
        self.ip = None
        self.username = None
        self.password = None
        self.port = None

    def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.ip, self.port, self.user, self.pwd, timeout=10, banner_timeout=10)
