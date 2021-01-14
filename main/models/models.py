# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, SmallInteger, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class HostInstance(db.Model):
    __tablename__ = 'host_instance'

    host_id = db.Column(db.Integer, primary_key=True)
    host_ip = db.Column(db.String(50), nullable=False)
    host_name = db.Column(db.String(50))
    host_port = db.Column(db.Integer)
    host_type_key = db.Column(db.String(50), nullable=False)
    host_project = db.Column(db.String(50))
    is_remove = db.Column(db.Integer)
    comment = db.Column(db.String(50))



class HostServerSoftware(db.Model):
    __tablename__ = 'host_server_software'

    server_software_id = db.Column(db.Integer, primary_key=True)
    host_id = db.Column(db.Integer, index=True)
    soft_type = db.Column(db.String(50), index=True)
    soft_port = db.Column(db.Integer)
    start_soft_cmd = db.Column(db.String(50))
    stop_soft_cmd = db.Column(db.String(50))
    restart_soft_cmd = db.Column(db.String(50))
    soft_log_path = db.Column(db.String(50))
    software_install_id = db.Column(db.Integer)
    is_remove = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    modify_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    comments = db.Column(db.String(50))



class HostUser(db.Model):
    __tablename__ = 'host_users'

    user_id = db.Column(db.Integer, primary_key=True)
    host_id = db.Column(db.Integer, nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    user_pass = db.Column(db.String(50), nullable=False)
    user_role = db.Column(db.String(50), nullable=False)



class Project(db.Model):
    __tablename__ = 'projects'

    project_id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(50))
    project_code = db.Column(db.String(50))
    controller_ip = db.Column(db.String(50))
    order_id = db.Column(db.Integer)
    is_remove = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
    modify_time = db.Column(db.DateTime)
    comments = db.Column(db.String(500))



class ScriptFileCabinet(db.Model):
    __tablename__ = 'script_file_cabinet'

    script_file_id = db.Column(db.Integer, primary_key=True)
    script_file_path = db.Column(db.String(300))
    script_file_name = db.Column(db.String(50))
    script_file_group = db.Column(db.String(50))
    script_file_type = db.Column(db.String(50))
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    modify_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    comment = db.Column(db.String(50))



class ScriptFileExecuteEvent(db.Model):
    __tablename__ = 'script_file_execute_event'

    script_file_execute_event_id = db.Column(db.Integer, primary_key=True)
    script_execute_event_batch_id = db.Column(db.String(50))
    script_file_id = db.Column(db.Integer)
    execute_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    execute_end_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    execute_result = db.Column(db.Integer, info='sys_code.script_file_execute_result_ype   1为成功，0为失败')
    script_file_content = db.Column(db.String)
    host_id = db.Column(db.Integer)



class SoftwareConf(db.Model):
    __tablename__ = 'software_conf'

    software_conf_id = db.Column(db.Integer, primary_key=True)
    software_package_id = db.Column(db.Integer, nullable=False, index=True)
    software_conf_name = db.Column(db.String(50))
    software_conf_type = db.Column(db.String(50), info='sys_code.software_conf__type')
    software_conf_path = db.Column(db.String(50))
    comment = db.Column(db.String(50))



class SoftwareConfCopy(db.Model):
    __tablename__ = 'software_conf_copy'

    software_conf_id = db.Column(db.Integer, primary_key=True)
    software_conf_name = db.Column(db.String(50))
    project_id = db.Column(db.Integer)
    server_software_type = db.Column(db.String(50), info='sys_code.server_software_type')
    software_parameter_id = db.Column(db.Integer, info='software_parameter.software_parameter_id')
    software_conf_path = db.Column(db.String(50))
    comment = db.Column(db.String(50))



class SoftwarePackage(db.Model):
    __tablename__ = 'software_package'

    software_package_id = db.Column(db.Integer, primary_key=True)
    software_name = db.Column(db.String(50), info='软件名称 会下/package/software/下创建一个软件目录')
    software_versions = db.Column(db.String(50))
    package_path = db.Column(db.String(200), info='安装包位置，项目/package/software/{{software_versions}}/{{software_name}}下面')
    software_package_zip_type = db.Column(db.String(50), info='sys_code.sys_type=software_package_zip_type')
    package_storage_type = db.Column(db.String(50), info='sys_code.sys_type=package_storage_type')
    comment = db.Column(db.String(50), info='备注')



class SoftwarePackageInstallEvent(db.Model):
    __tablename__ = 'software_package_install_event'

    software_package_install_event_id = db.Column(db.Integer, primary_key=True)
    host_id = db.Column(db.Integer, nullable=False, info='host_instance.host_id')
    software_package_id = db.Column(db.Integer, info='software_package.software_package_id')
    execute_result = db.Column(db.String(1000), info='执行结果收集')
    server_software_action_type = db.Column(db.String(50), info='执行动作 code_key：sys_code.code_type=server_software_action_type')
    execute_status = db.Column(db.String(50), info='执行动作 code_key：sys_code.code_type=tandard_execution_results')
    execute_time = db.Column(db.String(50), info='第一次执行时间')
    re_execute_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后一次执行时间')



class SoftwareParameter(db.Model):
    __tablename__ = 'software_parameter'

    software_parameter_id = db.Column(db.Integer, primary_key=True)
    software_conf_id = db.Column(db.Integer, nullable=False, info='software_conf.software_conf_id')
    replacement_entry = db.Column(db.String(50), nullable=False)
    replacement_value = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.String(50), nullable=False)



class SysCode(db.Model):
    __tablename__ = 'sys_code'

    code_id = db.Column(db.Integer, primary_key=True)
    code_key = db.Column(db.String(500))
    code_name = db.Column(db.String(50), nullable=False)
    code_type = db.Column(db.String(50), nullable=False)
    f_code = db.Column(db.String(50))
    order_queue = db.Column(db.SmallInteger)
    comments = db.Column(db.String(50))



class SysMenu(db.Model):
    __tablename__ = 'sys_menu'

    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer)
    title = db.Column(db.String(50))
    name = db.Column(db.String(50))
    path = db.Column(db.String(50))
    icon = db.Column(db.String(50))
    statu = db.Column(db.Integer)
    comments = db.Column(db.String(50))



class SystemFunction(db.Model):
    __tablename__ = 'system_function'

    system_function_id = db.Column(db.Integer, primary_key=True)
    system_name = db.Column(db.String(50), nullable=False, info='操作系统名称')
    system_version = db.Column(db.String(50), nullable=False, info='系统版本')
    function_type = db.Column(db.String(50), nullable=False, info='文件新增、文件内容追加、指定内容替换、执行命令')
    system_content = db.Column(db.String, nullable=False, info='操作文本内容')
    system_content_file = db.Column(db.String(200), info='文件文本路径')
    system_action = db.Column(db.String(50), nullable=False, info='动作归类')
    system_action_name = db.Column(db.String(50), info='动作归类名')
    action_service_switch = db.Column(db.Integer, info='服务类动作，启动，停止标记。1启动，2停止')
    force = db.Column(db.Integer, info='标记为码值，禁止全部删除')
    order_by = db.Column(db.Integer, info='排序')
    comment = db.Column(db.String(100), info='备注')



class SystemOtherPortal(db.Model):
    __tablename__ = 'system_other_portals'

    system_other_portals_id = db.Column(db.Integer, primary_key=True)
    portal_disabled = db.Column(db.Integer, info='是否禁用，1为禁用')
    portal_label = db.Column(db.String(50), nullable=False)
    portal_name = db.Column(db.String(50))
    portal_url = db.Column(db.String(500))
    portal_login_user = db.Column(db.String(50))
    portal_login_pwd = db.Column(db.String(50))
    portal_icon = db.Column(db.String(50))
    force = db.Column(db.Integer, info='系统项，是否禁止删除')
    comments = db.Column(db.String(50))



class ZabbixAgent(db.Model):
    __tablename__ = 'zabbix_agent'

    zabbix_install_id = db.Column(db.Integer, primary_key=True)
    host_id = db.Column(db.Integer, info='host_instance.host_id')
    install_info = db.Column(db.String)
    execute_result = db.Column(db.Integer, info='-1错误、1成功、2警告、3未知')
    zabbix_host_name = db.Column(db.String(50), info='主机名')
    zabbix_hostid = db.Column(db.String(100))
    zabbix_groupids = db.Column(db.String(100), info='主机组')
    zabbix_templateids = db.Column(db.String(100), info='关联模板')
    monitored_by_proxy_id = db.Column(db.String(50), info='代理ID')
    operate_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
