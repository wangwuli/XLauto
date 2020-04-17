# from .logio import login

# def init_app(app):
#     login.init_app(app)
from flask import Blueprint

services = Blueprint('services', __name__)

from src.services import logio, home, general