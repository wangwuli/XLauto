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

# import paramiko
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# host = '9.10.11.12'
# port, user, password = 22, 'usr', 'pass'
# ssh.connect(host, port,  user, password)
# stdin,stdout,stderr = c.exec_command("ping 192.168.1.1")
#
# for line in iter(stdout.readline,""):
#     print(line)


ssh.set_info(a)
c = ssh.connect()
stdin, stdout, stderr = ssh.run("ping 192.168.1.1", console)
c.close()



