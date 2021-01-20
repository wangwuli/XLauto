
import os
from src.dao.zip_method import unzip_distinguish
from src.deploy import deploy
from flask import request, current_app

from src.deploy.software_conf.dao import get_software_conf, save_software_conf
from src.general.General import Result


@deploy.route('/deploy/software_conf', methods=['GET', 'POST', 'PUT', 'DELETE'])
def software_conf():
    if request.method == 'GET':
        data = request.args
        return_data = get_software_conf(data['software_package_id'])
        return Result.success_response(data=return_data, msg='查询成功')

    elif request.method == 'POST':
        data_dict = request.get_json()
        software_conf_data = data_dict['software_conf_data']

        save_software_conf(software_conf_data)

        return Result.success_response(msg='保存成功')