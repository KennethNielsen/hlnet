
from __future__ import print_function

import argparse

import environments
import tests


def parse_args():
    """Parse command line arguments and return them"""
    description = 'Run tests on high level numerical environments'
    parser = argparse.ArgumentParser(description=description)
    # Add arguments
    parser.add_argument('-e', '--list-environments', default=False, action='store_true',
                        help='List environments and exit')
    parser.add_argument('-t', '--list-tests', default=False, action='store_true',
                        help='List tests and exit')
    args = parser.parse_args()
    return args


def get_environments():
    """Return all environments

    Returns:
        tuple: Return list of available and not available environments
    """
    available = []
    unavailable = []
    for env in environments.get_environments():
        if env.has_executable:
            available.append(env)
        else:
            unavailable.append(env)
    return available, unavailable


def get_tests():
    """Collect and return the tests"""
    pass


def list_environments(available_envs, unavailable_envs):
    """Print the envisonments out to stdout"""
    print('# Available environments\n')
    for env in available_envs:
        print('*', env.name)

    if unavailable_envs:
        print('\n# Unavailable environments\n')
        for env in unavailable_envs:
            print('*', env.name)
    print()


def list_tests():
    pass

def main():
    """The main function"""
    args = parse_args()
    available_envs, unavailable_envs = get_environments()
    tests = get_tests()

    # Execute list only actions
    if args.list_environments:
        list_environments(available_envs, unavailable_envs)
        return
    elif args.list_tests:
        list_tests(tests)


main()
