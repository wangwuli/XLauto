# -*- coding: utf-8 -*-
'''
@author: liww
@file: log.py
@time: 2020/6/16 17:54
@desc:
'''
import json
import os
import time

from flask import current_app
from src.socket import socket

@socket.route('/socket/log/happened')
def execute_script_query(ws):
    happened_log_path = os.path.join(current_app.config.xlautoenv['PROJECT_PATH'], current_app.config['HAPPENED_LOG'])

    with open(happened_log_path, 'r') as f:
        f.seek(0, 2)   #指针移动到文件末尾
        while not ws.closed:
            # message = ws.receive()
            line = f.readline()     #从末尾开始读取
            if len(line) == 0:     #假如空等待几秒在读取
                time.sleep(3)
            else:
                log_text = line.decode('utf-8')
                data = {'data': log_text, "success": 1, "msg": "加载主机信息成功"}
                # data = {"msg": "%s" %e, "success":0,}
                ws.send(json.dumps(data))
    f.close()