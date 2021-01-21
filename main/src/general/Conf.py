import configparser
import re

from src.general.File import get_file_text


class Configuration():
    def get_dict(self, head):
        dict_a = {}
        for servername in head:
            dict_a[servername[0]] = servername[1]
        return dict_a

    def ini_conf_analysis(self, file_path):
        """
        适用于 Mysql、samba
        :param file_path:
        :return:
        """
        conff = configparser.ConfigParser()
        conff.read(file_path)
        secs = conff.sections()  # 文件内所有[XXX]的内容

        server_all = {}
        for head in secs:
            server = conff.items(head)  # 某个[XXX]以下的内容
            server_all[head] = self.get_dict(server)
        return server_all

    def template_conf_analysis(self, file_path):
        """
        读取模板类配置，里面包含{{ }}的替换项的内容
        :param file_path:
        :return:
        """
        conf_text = get_file_text(file_path)
        pattern = re.compile(r"[{](.*?)[}]")
        pass_list = pattern.findall(conf_text)
        return pass_list