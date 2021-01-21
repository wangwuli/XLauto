from flask import Blueprint

deploy = Blueprint('deploy', __name__)

from src.deploy import soft
from src.deploy.kubernetes_d import views
from src.deploy.zabbix import templates, host_groups, views
from src.deploy.soft_package import views
from src.deploy.software_conf import views
from src.deploy.software_conf_parameter import views