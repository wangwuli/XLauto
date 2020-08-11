import re

from src.general.Connect_G import Sshmet

ssh = Sshmet()

a = {
    "host_ip": "192.168.20.163",
    "user_name": "root",
    "user_pass": "thzk211!",
    "host_port": "22",
}

def console(text):
    print(text)


ssh.set_info(a)
c = ssh.connect()
stdin, stdout, stderr = ssh.run("ping 192.168.1.1", console)



