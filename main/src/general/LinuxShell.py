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
            info_s_s = info_s[1].split('users')
            data['server_start_time'] = info_s_s[0][:-2].replace(',','').strip()
            data['login_user_number'] = info_s_s[0][-2]
            data['cpu_loadaverage'] = info_s_s[1].split(':')[1]
        return data

    def get_freeinfo(self):
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
            data['mem_mem_buffcache'] = freeinfo_mem[6]

            swapinfo_mem = freeinfo[2].split()
            data['swap_total'] = swapinfo_mem[1]
            data['swap_used'] = swapinfo_mem[2]
            data['swap_free'] = swapinfo_mem[3]

        return data

