#!/usr/bin/env python

#
# MUSIC CARD
# Application
#

import subprocess
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
    read_id = reader.read_card()
    # Todo clear previousCard after some time (cfg.previousCardTimeout)

    try:
        print('Read card : ', read_id)

        # Update Card bdd TODO do it every X minutes
        cardList.update_list()

        # Find the card in bdd
        card = cardList.get_card(read_id)

        if card is not None:
            # Card execution
            print('Command : ', card.cmd)
            print('Modes : ', card.str_modes())

            if (previousCard == read_id) and ("cancel" == cfg.multiReadMode) and (not card.has_mode("Command")):
                # Cancel the read
                print('Multi read : card canceled')
            else:
                # Update the previous card memory
                previousCard = read_id

                if card.has_mode("ClearQueue"):
                    subprocess.check_call(["./sonosplay.sh " + commandLine + "clearqueue"], shell=True)

                if card.cmd != 'error':
                    # TODO, direct python implementation without using sh script
                    subprocess.check_call(["./sonosplay.sh " + commandLine + card.cmd], shell=True)

                list(range(10000)) # some payload code
                time.sleep(0.2)    # sane sleep time

    except OSError as e:
        print("Execution failed:")
        list(range(10000))       # some payload code
        time.sleep(0.2)    # sane sleep time of 0.1 seconds

