#!/usr/bin/env python

#
# MUSIC CARD
# Application
#

# Python import
import subprocess
import time

# Bipbip Music import
from CardMemory import CardMemory
from CardList import CardList
from Reader import Reader

import config as cfg    # Get config from file


def main():

    # Previous card id memory
    previous_card = CardMemory()

    reader = Reader()
    card_list = CardList()

    # Create address path
    address = cfg.ip + ':' + cfg.port

    # Create command line
    if cfg.roomName == '':
        # Command for global playing
        command_line = address + ' '
    else:
        # Command for local playing
        command_line = address + ' ' + cfg.roomName + '/'

    print('Ready: place a card on top of the reader')

    while True:
        read_id = reader.read_card()
        # Todo clear previous_card after some time (cfg.previousCardTimeout)

        try:
            print('Read card : ', read_id)

            # Update Card bdd TODO do it every X minutes
            card_list.update_list()

            # Find the card in bdd
            card = card_list.get_card(read_id)

            if card is not None:
                # Card execution
                print('Command : ', card.cmd)
                print('Modes : ', card.str_modes())

                if (previous_card.get() == read_id) and ("cancel" == cfg.multiReadMode) and (not card.has_mode("Command")):
                    # Cancel the read
                    print('Multi read : card canceled')
                else:
                    # Update the previous card memory
                    previous_card.set(read_id)

                    if card.has_mode("ClearQueue"):
                        subprocess.check_call(["./sonosplay.sh " + command_line + "clearqueue"], shell=True)

                    if card.cmd != 'error':
                        # TODO, direct python implementation without using sh script
                        subprocess.check_call(["./sonosplay.sh " + command_line + card.cmd], shell=True)

                    list(range(10000)) # some payload code
                    time.sleep(0.2)    # sane sleep time

        except OSError as e:
            print("Execution failed:")
            list(range(10000))       # some payload code
            time.sleep(0.2)    # sane sleep time of 0.1 seconds


if __name__ == "__main__":
    main()