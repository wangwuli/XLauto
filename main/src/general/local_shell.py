import subprocess


class Shell_G:
    def __init__(self):
        pass

    def shell_exec(self, cmd):
        subprocess.Popen("%s" %cmd, shell=True)


    # def execrealtime(self, shell_cmd, object_=None):
    #     """
    #     执行单条命令, 实时获取命令执行结果
    #     :param shell_cmd:
    #     :param object_: 实时接收处理消息的方法
    #                      比如：
    #                          def object_(text):
    #                             print(text)
    #     :return:
    #     """
    #     if not object_:
    #         object_ = self.execcmdout
    #     cmd = shlex.split(shell_cmd)
    #     p = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1)
    #     for line in iter(p.stdout.readline, b''):
    #         object_(line)
    #     p.stdout.close()
    #     p.wait()