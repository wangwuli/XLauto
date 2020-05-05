from src.general.Connect_G import Sshmet


class ServerInfo(Sshmet):
    def get_updateinfo(self):
        """
        server_current_time: 系统时间
        server_start_time: 运行时间
        login_user_number: 在线用户
        cpu_loadaverage: CPU loadaverage负载
        :return:
        """
        info = self.execcmd("uptime")
        data = {}
        if info:
            info_s = info.split('up')
            data['server_current_time'] = info_s[0]
            info_s_s = info_s[1].split('user')
            data['server_start_time'] = info_s_s[0][:-2].replace(',','').strip()
            data['login_user_number'] = info_s_s[0][-2]
            data['cpu_loadaverage'] = info_s_s[1].split('load average: ')[1]
            data['cpu_loadaverage'] = list(map(float ,data['cpu_loadaverage'].split(',')))
        return data

    def get_freeinfo(self):
        """
        mem_total : 总内存
        mem_used : 内存使用
        mem_free : 内存空闲
        mem_shared : 共享内存
        mem_buffcache : 内存缓存
        mem_available : 内存可用
        swap_total: 总虚拟内存
        swap_used: 虚拟内存使用
        swap_free: 虚拟内存空闲
        :return:
        """
        info = self.execcmd("free -m")
        data = {}
        if info:
            data = {}
            freeinfo = info.split('\n')
            freeinfo_mem = freeinfo[1].split()
            data['mem_total']= freeinfo_mem[1]
            data['mem_used'] = freeinfo_mem[2]
            data['mem_free'] = freeinfo_mem[3]
            data['mem_shared'] = freeinfo_mem[4]
            data['mem_buffcache'] = freeinfo_mem[5]
            data['mem_available'] = freeinfo_mem[6]

            swapinfo_mem = freeinfo[2].split()
            data['swap_total'] = swapinfo_mem[1]
            data['swap_used'] = swapinfo_mem[2]
            data['swap_free'] = swapinfo_mem[3]

        return data

    def get_disk(self):
        info = self.execcmd("df -m | grep ^/dev")
        data = {}
        if info:
            info_disk_list = info.split('\n')
            for info_disk_list_one in info_disk_list:
                data_dict = {}
                info_disk_one_list = info_disk_list_one.split()
                data_dict['total_partition_size'] = int(info_disk_one_list[1])
                data_dict['surplus_partition_size'] = int(info_disk_one_list[2])
                data_dict['use_partition_size'] = int(info_disk_one_list[3])
                data_dict['usage_partition_size'] = info_disk_one_list[4]
                data_dict['mount_partition_dir'] = info_disk_one_list[5]
                data_dict['partition_name'] = info_disk_one_list[0]
                data[data_dict['partition_name']] = data_dict
        return_data = {'hard_disk': data}

        return return_data

    def get_ss(self):
        info_u = self.execcmd("ss -s")
        if info_u:
            info_socket_list = info_u.split('\n')
            state_list = info_socket_list[1].split('(')[1].split(')')[0].split(',')
            name_list = []
            value_list = []
            for state_list_one in state_list:
                name_list.append(state_list_one.split()[0])
                value_list.append(int(state_list_one.split()[1]))

        data = {"socket_tu_name":name_list, "socket_tu_value":value_list}

        return data


