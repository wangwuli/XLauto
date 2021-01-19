from flask import Blueprint

file_l = Blueprint('file', __name__)

from src.file.local_file  import views

from src.deploy.software_conf import views