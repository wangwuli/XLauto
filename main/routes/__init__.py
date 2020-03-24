from src.selfhealing import selfhealing
from src.services import services
from src.deploy import deploy
from src.independent import independent


def init_app(app):
    app.register_blueprint(services)
    app.register_blueprint(deploy)
    app.register_blueprint(independent)
    app.register_blueprint(selfhealing)
