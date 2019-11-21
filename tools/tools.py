

def print_my_path():
    from os import path, getcwd
    print('DEBUG: cwd:     {}'.format(getcwd()))
    print('DEBUG: __file__:{}'.format(__file__))
    print('DEBUG: abspath: {}'.format(path.abspath(__file__)))
