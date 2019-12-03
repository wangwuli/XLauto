from flask import Flask
from main.services import services
from . import routes

def create_app():


    app = Flask(__name__)

    routes.init_app(app)
    #services.init_app(app)
    # register_blueprint(app)

    return app

# def register_blueprint(app):
#     app.register_blueprint(services)