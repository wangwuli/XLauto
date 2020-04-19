from flask import Flask
from . import routes
from exts import db

def create_app():

    xlauto = Flask(__name__)

    routes.init_app(xlauto)
    xlauto.config.from_object('main.settings')     #加载配置文件

    db.init_app(xlauto)        #db绑定app

    return xlauto

