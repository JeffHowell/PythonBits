# from subprocess import call
import subprocess
import os


class SystemCaller:

    def system_call(self, command, shell=False):
        return subprocess.call(command, shell)

    def os_system_call(self, command):
        return os.system(command)