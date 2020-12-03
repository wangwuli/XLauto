# -*- coding: utf-8 -*-
'''
@author: liww
@file: auxiliary.py
@time: 2020/11/20 17:40
@desc:
'''

import json
import re
from src.deploy.zabbix.login import zabbix_api_login


class OmnisCollect:
    def __init__(self):
        self.log("开始登录")
        self.zapi = zabbix_api_login()
        self.log("登录成功")

    def log(self, msg):
        self.logger.info(msg + getDateTime())

    def get_temp_group(self):
        """
        查询模板组
        :return:
        """
        info = self.zapi.hostgroup.get(output="extend")
        return_info = []
        for info_one in info:
            if re.match('\[Templates\]', info_one['name']):
                return_info.append(info_one)

        return return_info

    def post_group(self, group_name):
        """
        新增组
        :return:
        """
        info = self.zapi.hostgroup.create(name=group_name)
        return info

    def del_group(self, *groupids):
        """
        删除组get_item_desc
        :param groupids:
        :return:
        """
        info = self.zapi.hostgroup.delete(*groupids)
        return info

    def get_templated_item(self, templateids):
        """
          查询模板的监控项
          :param templateids:
          :return:
          """

        self.log("开始获取模板数据"+json.dumps(templateids))
        info = self.zapi.item.get(templateids=templateids)
        self.log("结束获取模板")

        return info

    def get_trigger(self, itemid):
        """

        :param itemid:
        :return:
        """
        info = self.zapi.trigger.get(itemids=itemid, expandExpression=1, selectItems=['itemid'])

        return info

    def add_trigger(self, description, expression, serverity):
        info = self.zapi.trigger.create(description=description, expression=expression, priority=serverity)

        return info

    def get_triggerinfo_byhost(self, hostid):
        """
            功能说明：获取主机包含的所有trigger信息
            参数说明：
                hostid:主机id
        """
        trigger_info = self.zapi.trigger.get(hostids=hostid,expandExpression=1,selectHosts=['host'])
        return trigger_info

    def get_triggerinfo(self, triggerid):
        """
            功能说明：根据triggerid获取trigger信息
            参数说明：
                triggerid: 触发器id
        """
        get_info = self.zapi.trigger.get(triggerids=triggerid, selectHosts=['host'])
        return get_info

    def post_triggerinfo(self, trigger_args):
        """
            功能说明：update trigger
            参数说明：
                triggerid: 触发器id
        """
        update_info = self.zapi.trigger.update(**trigger_args)
        return update_info

    def del_triggerinfo(self, triggerids):
        """
        删除 trigger
        :param triggerids:
        :return:
        """
        delete_info = self.zapi.trigger.delete(*triggerids)
        return delete_info


    def get_groupsinfo(self, project=None):
        """
        :param project: 分组名称字段
        :return: 返回主机组信息，如果为空，则返回所有主机组信息
        by: 吴威
        """
        if project:
            # 按项目搜索分组
            group_info = self.zapi.hostgroup.get(output=['groupid', 'name'], search={"name": project})
        else:
            # real_hosts=1表示只查询包含主机的主机组
            group_info = self.zapi.hostgroup.get(output=['groupid', 'name'], real_hosts=1)
        return group_info


    def del_template(self, templateids):
        info = self.zapi.template.delete(*templateids)
        return info


    def get_template(self, templateids):
        info = self.zapi.template.get(filter={"groupids":templateids},
                                      output="extend",
                                      selectGroups=['groupid', 'name'])
        return info