from main.services import services
from main.deploy import deploy

def init_app(app):
    app.register_blueprint(services)
    app.register_blueprint(deploy)