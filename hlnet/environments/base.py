"""The baseclass for all environments"""

class EnvironmentBase(object):
    """Base class for all environments"""

    @property
    def name(self):
        """Return the name of the environment"""
        raise NotImplementedError()

    def get_executable(self):
        """Return the path to the executable"""
        raise NotImplementedError()


class NoExecutable(Exception):
    """Exception that indicates that no executable was found for a numerical environment"""
