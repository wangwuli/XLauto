from main.selfhealing import selfhealing
from main.services import services
from main.deploy import deploy
from main.independent import independent


def init_app(app):
    app.register_blueprint(services)
    app.register_blueprint(deploy)
    app.register_blueprint(independent)
    app.register_blueprint(selfhealing)
