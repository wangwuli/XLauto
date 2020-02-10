import subprocess


class Shell_G:
    def __init__(self):
        pass

    def shell_exec(self, cmd):
        subprocess.Popen("%s" %cmd, shell=True)