"""A Python 2 environment"""

import sys
import subprocess
from .base import EnvironmentBase, NoExecutable

class Environment(EnvironmentBase):

    name = 'Python 2'
    test_suffix = 'py2.py'

    def get_executable(self):
        """Return the Python 2 executable"""
        platform = sys.platform
        if platform == 'linux':
            try:
                return subprocess.check_output('which python2', shell=True).strip().decode('ascii')
            except subprocess.CalledProcessError:
                pass

        message = 'No executeable could be found for Python 2'
        raise NoExecutable(message)

    @property
    def has_executable(self):
        """A property that indicates whether this environment has an executable on this
        platform
        """
        try:
            self.get_executable()
        except NoExecutable:
            return False
        return True

if __name__ == '__main__':
    env = Python2()
    print(env.get_executable())
    print(env.has_executable)
