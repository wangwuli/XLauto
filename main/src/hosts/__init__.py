from flask import Blueprint

hosts = Blueprint('hosts', __name__)

from src.hosts.host_cmd import update_file
from src.hosts.host_management import views

