from flask import Blueprint

deploy = Blueprint('deploy', __name__)

from src.deploy import soft
from src.deploy.kubernetes_d import views