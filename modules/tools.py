

def print_my_path():
    from os import path, getcwd
    print('DEBUG: cwd:     {}'.format(getcwd()))
    print('DEBUG: __file__:{}'.format(__file__))
    print('DEBUG: abspath: {}'.format(path.abspath(__file__)))


def get_serial():
    # Extract serial from cpuinfo file
    serial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                serial = line[10:26]
        f.close()
    except:
        serial = "ERROR000000000"

    return serial
