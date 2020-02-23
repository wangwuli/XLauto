#系统阻碍故障自愈处理

# def init_app(app):
#     login.init_app(app)
from flask import Blueprint

selfhealing = Blueprint('selfhealing', __name__)

from main.selfhealing import opost