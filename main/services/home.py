# -*- coding: utf-8 -*-

from . import services
from ..general.General import Result


@services.route('/home/menu_query', methods=['GET'])
def home_menu_query():
    data = [
        {
            "entity": {
                "id": 0,
                "name": "aa",
                "icon": "el-icon-message",
                "icon": "菜单一"
            }
        },
        {
            "entity": {
                "id": 1,
                "name": "systemManage",
                "icon": "el-icon-message",
                "alias": "菜单二"
            },

            "childs": [
                {
                    "entity": {
                        "id": 3,
                        "name": "authManage",
                        "icon": "el-icon-loading",
                        "alias": "权限管理",
                        "value": {"path": "/hello"}
                    }
                },
            ]
        }
    ]

    return Result.success_response(data)
