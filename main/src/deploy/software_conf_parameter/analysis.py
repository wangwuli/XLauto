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
        software_conf_info = data_dict['software_conf_info']

        conf = Configuration()
        software_conf_parameter_list = []
        for software_conf_info_one in software_conf_info:
            if data_dict['software_conf_type'] == "template":
                software_conf_path = software_conf_info_one['software_conf_path']
                software_conf_parameter = conf.template_conf_analysis(software_conf_path)

            software_conf_parameter_dict_list = []
            for software_conf_parameter_one in software_conf_parameter:
                software_conf_parameter_dict = {
                    'replacement_entry': software_conf_parameter_one,
                    'default_value': ''
                }
                software_conf_parameter_dict_list.append(software_conf_parameter_dict)


            software_conf_parameter_list.append(
                {
                    'software_conf_id': software_conf_info_one['software_conf_id'],
                    'software_conf_parameter': software_conf_parameter_dict_list
                }
            )


        # save_software_conf_parameter(software_conf_ids)

        # for software_conf_info_one in software_conf_info:
        #     try:
        #         conf_content = conf.ini_conf_analysis(software_conf_info_one['software_conf_path'])
        #     except Exception as e:
        #         return Result.fail_response(msg='解析失败：%s' %e)

        return Result.success_response(data=software_conf_parameter_list, msg='解析成功')