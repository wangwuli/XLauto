import os

from src.deploy import deploy
from multiprocessing import Pool
from src.general.Connect_G import Sshmet
from src.general.General import ReturnG, Result
from flask import request


@deploy.route('/deploy/kubernetes_install', methods=['GET', 'POST', 'PUT', 'DELETE'])
def kubernetes_install():
    configuration_info = request.get_json()

    return Result.success_response(msg='安装成功')