from flask import Blueprint

setting = Blueprint('setting', __name__)

from src.setting import views
