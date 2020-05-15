from flask import Blueprint

hosts = Blueprint('host_cmd', __name__)

from src.hosts.host_cmd import update_file
