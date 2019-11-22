from .logio import login

def init_app(app):
    app.register_blueprint(login,url_prefix='/')