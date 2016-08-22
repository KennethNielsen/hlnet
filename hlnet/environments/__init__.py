"""Module that gathers up all the real environments"""

from __future__ import absolute_import

from importlib import import_module

from os import listdir
from os.path import abspath, dirname

def get_environments():
    """Return all available environments instances"""
    environments = []
    for filename in listdir(dirname(abspath(__file__))):
        if not filename.endswith('.py'):
            continue
        if filename.startswith('__') or filename == 'base.py':
            continue

        modulename = '.' + filename.replace('.py', '')
        module = import_module(modulename, __name__)        
        environments.append(module.Environment())

    return environments
