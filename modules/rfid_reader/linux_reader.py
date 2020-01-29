

"""
MUSIC CARD
Card Reader
"""

import os.path
import sys

from select import select
from evdev import InputDevice, ecodes, list_devices


class Reader:
    """
    Reader class to handle card read on linux
    """

    def __init__(self):
        """
        Constructor
        """

        path = os.path.dirname(os.path.realpath(__file__))
        self.keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"

        if not os.path.isfile(path + '/deviceName.txt'):
            sys.exit('Please run setup_reader.py first')
        else:
            with open(path + '/deviceName.txt', 'r') as file_handler:
                device_name = file_handler.read()

            devices = [InputDevice(fn) for fn in list_devices()]

            for device in devices:
                if device.name == device_name:
                    self.dev = device
                    break
            try:
                self.dev
            except:
                sys.exit('Could not find the device %s\n. Make sure is connected' % device_name)

    def read_card(self):
        """
        Function to read the cards.
        It concatenate all characters until finding 'KEY_ENTER'
        The final word is returned
        :return: card key as string
        """
        keys_input = ''
        key = ''

        while key != 'KEY_ENTER':
            read, write, execute = select([self.dev], [], [])
            for event in self.dev.read():
                if event.type == 1 and event.value == 1:
                    keys_input += self.keys[event.code]
                    # print( keys[ event.code ] )
                    key = ecodes.KEY[event.code]

        return keys_input[:-1]
