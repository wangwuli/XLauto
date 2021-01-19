from src.setting import setting
from src.hosts import hosts
from src.selfhealing import selfhealing
from src.services import services
from src.deploy import deploy
from src.independent import independent
from src.socket import socket
from src.file import file_l


def init_app(app):
    # app.register_blueprint(services)
    app.register_blueprint(deploy)
    app.register_blueprint(independent)
    app.register_blueprint(selfhealing)
    app.register_blueprint(services)
    app.register_blueprint(hosts)
    app.register_blueprint(setting)
    app.register_blueprint(file_l)


def init_sapp(sockets):
    sockets.register_blueprint(socket)