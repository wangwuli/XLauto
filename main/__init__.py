import os

from flask import Flask
from . import routes
from exts import db
from flask_sockets import Sockets

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

    return xlauto

