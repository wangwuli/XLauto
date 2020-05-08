from flask import Blueprint

socket = Blueprint('sockets', __name__)

from src.socket import hosts
