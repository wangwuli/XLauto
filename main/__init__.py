from flask import Flask
from . import routes
from exts import db

def create_app():

    app = Flask(__name__)

    routes.init_app(app)
    app.config.from_object('main.settings')     #加载配置文件
    db.init_app(app)        #db绑定app

    return app

