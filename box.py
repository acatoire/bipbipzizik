#!/usr/bin/env python

#
# MUSIC CARD
# Application
#

import re
import sys
import subprocess
import os
import time
from CardList import CardList
from Reader import Reader

import config as cfg    # Get config from file

reader = Reader()
cardList = CardList()


# Create address path
address = cfg.ip + ':' + cfg.port

# Create command line
if cfg.roomName == '':
    # Command for global playing
    commandLine = address + ' '
else:
    # Command for local playing
    commandLine = address + ' ' + cfg.roomName + '/'

# Previous card id memory
previousCard = ""

print('Ready: place a card on top of the reader')

while True:
    card = reader.readCard()
    # Todo clear previousCard after some time (cfg.previousCardTimeout)

    try:
        print('Read card : ', card)

        if (previousCard == card) and ("cancel" == cfg.multiReadMode):
            print('Multi read : card canceled')
        else:
            previousCard = card

            # Card execution
            plist = cardList.getPlaylist(card)
            print('Command : ', plist)
            if plist != '':
                # Check if sonosplay.sh is executable, if not write an error message
                subprocess.check_call(["./sonosplay.sh %s" % commandLine + plist], shell=True)

                list(range(10000))       # some payload code
                time.sleep(0.2)    # sane sleep time

    except OSError as e:
        print("Execution failed:")
        list(range(10000))       # some payload code
        time.sleep(0.2)    # sane sleep time of 0.1 seconds

