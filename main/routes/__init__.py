from main import services


def init_app(app):
    app.register_blueprint(services)