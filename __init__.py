from flask import Flask

def create_app():
    from . import services
    app = Flask(__name__)
    services.init_app(app)
    return app