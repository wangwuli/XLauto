# -*- coding: utf-8 -*-

from . import services
from ..general.General import Result


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
                        "title": "网络2",
                        "path": "/test"
                    }
                }
            ]
        }
    ]

    return Result.success_response(data)
