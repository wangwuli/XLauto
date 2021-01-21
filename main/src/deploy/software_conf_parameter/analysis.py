from src.deploy import deploy
from flask import request, current_app

from src.deploy.software_conf_parameter.dao import save_software_conf_parameter, get_software_conf_parameter
from src.general.Conf import Configuration
from src.general.General import Result


@deploy.route('/deploy/software_conf_parameter/analysis', methods=['GET', 'POST', 'PUT', 'DELETE'])
def software_conf_parameter_analysis():
    if request.method == 'GET':
        # data = request.args
        # return_data = get_software_conf_parameter(data['software_conf_id'])
        return Result.success_response(data='', msg='参数查询成功')

    elif request.method == 'POST':
        data_dict = request.get_json()
        software_conf_ids = data_dict['software_conf_ids']

        # save_software_conf_parameter(software_conf_ids)
        conf = Configuration()

        return Result.success_response(msg='保存成功')