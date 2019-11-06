#!/usr/bin/env python

#
# MUSIC CARD
# Application
#

# Python import
import subprocess
import time

# Bipbip Music import
from modules.rfid_reader.Reader import Reader
from modules.card_memory.CardMemory import CardMemory
from modules.cards_bdd.CardReader import CardBdd

import config as cfg    # Get config from file

# TODO check if bdd is automatically updated


def main():

    reader = Reader()
    bdd = CardBdd('https://bipbipzizik.firebaseio.com/', 'cards_test')

    # Previous card id memory
    try:
        # Get it from config
        previous_card = CardMemory(cfg.previousCardTimeout)
    except AttributeError:
        # Default value
        previous_card = CardMemory(30)

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

            # Find the card in bdd
            card = bdd.get_card(read_id)
            mode = card.get_mode()
            command = card.get_command()

            if card is not None:
                # Card execution
                print('Command : ', command)
                print('Modes : ', mode)

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
            list(range(10000))       # some payload code                TODO needed??
            time.sleep(0.2)          # sane sleep time of 0.1 seconds   TODO needed??


if __name__ == "__main__":
    main()
