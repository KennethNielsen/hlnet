"""A Python 2 environment"""

import sys
import subprocess
from .base import EnvironmentBase, NoExecutable

class Environment(EnvironmentBase):

    name = 'Not available test env'
    test_suffix = 'na.py'

    def get_executable(self):
        """Return the Python 2 executable"""
        message = 'No not_available executeable on this platform'
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
