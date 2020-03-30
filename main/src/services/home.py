# -*- coding: utf-8 -*-
from models.models import HostInstance, SysCode, db
from . import services
from src.general.General import Result
from src.general.Transform import model_to_dict


@services.route('/home/menu_query', methods=['GET'])
def home_menu_query():
    data = [
        {
            "entity": {
                "id": 0,
                "name": "home",
                "icon": "el-icon-s-home",
                "title": "主页"
            }
        },
        {
            "entity": {
                "id": 1,
                "name": "instrument",
                "icon": "el-icon-s-cooperation",
                "title": "工具"
            },

            "childs": [
                {
                    "entity": {
                        "id": 3,
                        "name": "network",
                        "icon": "el-icon-place",
                        "title": "网络",
                        "path": "/network"
                    }
                },
                {
                    "entity": {
                        "id": 2,
                        "name": "test",
                        "icon": "el-icon-place",
                        "title": "主机",
                        "path": "/test"
                    }
                }
            ]
        },
        {
            "entity": {
                "id": 4,
                "name": "deploy",
                "icon": "el-icon-s-claim",
                "title": "部署"
            }
        },
        {
            "entity": {
                "id": 5,
                "name": "info_record",
                "icon": "el-icon-s-custom",
                "title": "维护"
            }
        },
    ]

    return Result.success_response(data,'菜单加载成功')


@services.route('/home/hosts_query', methods=['GET'])
def home_hosts_query():

    host_obj = db.session.query(HostInstance.host_id, HostInstance.host_ip, HostInstance.host_name,
                             SysCode.code_name.label('type_name')).join(HostInstance, HostInstance.host_type == SysCode.code_key).filter(
        SysCode.code_type == "host_type").all()
    data = model_to_dict(host_obj)

    db.session.close()
    return Result.success_response(data,'目标主机加载成功')