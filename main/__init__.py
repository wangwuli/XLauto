import os

from flask import Flask, current_app
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
    xlauto.xlautoenv = {}
    xlauto.xlautoenv['project_path'] = os.path.dirname(__file__)

    return xlauto

