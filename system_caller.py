# from subprocess import call
import shlex, subprocess
import os


class SystemCaller:

    def system_call(self, command, shell=False):
        return subprocess.call(command, shell)

    def os_system_call(self, command):
        return os.system(command)

    def subprocess_check_output_call(self, command):
        result = subprocess.check_output(shlex.split(command))
        # result = subp.returncode

        return result
        # proc = subprocess.Popen(shlex.split(command))
        # proc.communicate()

    def subprocess_call(self, command):
        subprocess.Popen(command)
        return "foo"