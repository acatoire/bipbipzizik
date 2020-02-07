"""
Module containing useful tools
"""

# pylint: disable=import-outside-toplevel

def print_my_path():
    """
    For debug purpose, print path
    :return: None
    """
    from os import path, getcwd
    print('DEBUG: cwd:     {}'.format(getcwd()))
    print('DEBUG: __file__:{}'.format(__file__))
    print('DEBUG: abspath: {}'.format(path.abspath(__file__)))


def get_serial() -> str:
    """
    Extract serial from raspberry pi cpuinfo file
    :return: serial as string
    """
    serial = "0000000000000000"
    try:
        with open('/proc/cpuinfo', 'r') as file_handler:
            for line in file_handler:
                if line[0:6] == 'Serial':
                    serial = line[10:26]
    except FileNotFoundError:
        serial = "ERROR00000000000"

    return serial
