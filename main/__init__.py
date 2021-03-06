import os

from flask import Flask

from models.models import db
from src.setting.startup import setting_control
from . import routes
# from exts import db
from flask_sockets import Sockets
import logging

def create_app():

    xlauto = Flask(__name__)
    sockets = Sockets(xlauto)
    routes.init_app(xlauto)
    routes.init_sapp(sockets)
    xlauto.config.from_object('main.settings')     #加载配置文件

    db.init_app(xlauto)     #db绑定app


    #使用current_app全局变量
    project_path = os.path.dirname(__file__)
    xlauto.config.xlautoenv = {}
    xlauto.config.xlautoenv['PROJECT_PATH'] = project_path

    #日志
    xlauto.debug = True
    try:
        handler = logging.FileHandler('./log/xlauto.log', encoding='UTF-8')  # 输出句柄
    except FileNotFoundError:
        os.makedirs('./log')
        handler = logging.FileHandler('./log/xlauto.log', encoding='UTF-8')
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')  # 打印格式
    handler.setFormatter(logging_format)   # 设置格式
    xlauto.logger.addHandler(handler)  # 生成对象，添加句柄

    #项目启动动作
    setting_control(xlauto)

    return xlauto

