# from subprocess import call
import subprocess
import os


class SystemCaller:

    def system_call(self, command, shell=False):
        return subprocess.call(command, shell)

    def os_system_call(self, command):
        return os.system(command)

    def os_popen_call(self, command):
        proc = subprocess.Popen(shell=True)
        proc.communicate()

    def subprocess_call(self, command):
        subprocess.Popen(command)
        return "foo"