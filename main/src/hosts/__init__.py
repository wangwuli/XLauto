from flask import Blueprint

host_cmd = Blueprint('host_cmd', __name__)

from src.hosts.host_cmd import update_file
