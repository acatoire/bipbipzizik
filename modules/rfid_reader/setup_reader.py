

"""
Create a device file
"""


import os.path
from evdev import InputDevice, list_devices

DEVICES_LIST = [InputDevice(fn) for fn in list_devices()]
FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '/deviceName.txt')


i = 0

print("Choose the reader from list")

for dev in DEVICES_LIST:
    print(i, dev.name)
    i += 1

DEVICE_ID = int(input('Device Number: '))

with open(FILE_PATH, 'w') as f:
    f.write(DEVICES_LIST[DEVICE_ID].name)
    f.close()
