import os

from flask import Flask
from . import routes
from exts import db
from flask_sockets import Sockets
import logging

def create_app():

    xlauto = Flask(__name__)
    sockets = Sockets(xlauto)
    routes.init_app(xlauto)
    routes.init_sapp(sockets)
    xlauto.config.from_object('main.settings')     #加载配置文件

    db.init_app(xlauto)        #db绑定app

    #使用current_app全局变量
    xlauto.config.xlautoenv = {}
    xlauto.config.xlautoenv['PROJECT_PATH'] = os.path.dirname(__file__)

    #日志
    xlauto.debug = True
    handler = logging.FileHandler('./log/xlauto.log', encoding='UTF-8')  # 输出句柄
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')  # 打印格式
    handler.setFormatter(logging_format)   # 设置格式
    xlauto.logger.addHandler(handler) # 生成对象，添加句柄

    return xlauto

