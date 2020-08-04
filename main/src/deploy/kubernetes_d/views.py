import os

from src.deploy import deploy
from multiprocessing import Pool
from src.general.Connect_G import Sshmet
from src.general.General import ReturnG, Result
from flask import request, current_app
from src.general.Sqla import Sqla


@deploy.route('/deploy/kubernetes_install', methods=['GET', 'POST', 'PUT', 'DELETE'])
def kubernetes_install():
    sqla = Sqla(current_app)
    configuration_info = request.get_json()

    sql = """
    SELECT * FROM system_function a
    WHERE a.system_name = "centos"
    AND a.system_version = "8"
    AND a.system_action IN ()
    """
    host_user_info = sqla.fetch_to_dict(sql, {'host_id' :configuration_info['']})

    return Result.success_response(msg='安装成功')