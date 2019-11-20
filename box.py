#!/usr/bin/env python

#
# MUSIC CARD
# Application
#

# Python import
import subprocess
import time
import requests

# Bipbip Music import
from modules.rfid_reader.Reader import Reader
from modules.card_memory.CardMemory import CardMemory
from modules.cards_bdd.CardFirebase import CardBdd

import config as cfg    # Get config from file

def main():

    # Get config
    try:
        # Get it from config
        memory_duration = cfg.previousCardTimeout
    except AttributeError:
        # Default value
        memory_duration = 30

    reader = Reader()
    bdd = CardBdd('https://bipbipzizik.firebaseio.com/', 'cards')
    previous_card = CardMemory(memory_duration)

    # Create address path
    address = cfg.ip + ':' + cfg.port

    # Create command line
    if cfg.roomName == '':
        # Command for global playing
        addr_with_room = address + '/'
    else:
        # Command for local playing
        addr_with_room = address + '/' + cfg.roomName + '/'


    while True:
        print('Ready: place a card on top of the reader')

        # Wait for a card to be read
        read_id = reader.read_card()

        try:
            print('Read card : ', read_id)

            # Find the card in bdd
            card = bdd.get_card(read_id)

            if card is None:
                print('Failed to read card from bdd')

            else:
                # Card execution
                mode = card.get_mode()
                command = card.get_command()

                print('Command : ', command)
                print('Modes : ', mode)

                if (previous_card.get() == read_id) and ("cancel" == cfg.multiReadMode) and (not card.is_command()):
                    # Cancel the read
                    print('Multi read : card canceled')
                else:
                    # Update the previous card memory
                    previous_card.set(read_id)

                    if card.has_mode("ClearQueue"):
                        command_line = "http://" + addr_with_room + "clearqueue"
                        print(command_line)
                        response = requests.get(command_line)
                        print(response.text)

                    if command is not None:
                        command_line = "http://" + addr_with_room + command
                        print(command_line)
                        response = requests.get(command_line)
                        print(response.text)

                    list(range(10000)) # some payload code
                    time.sleep(0.2)    # sane sleep time

        except OSError as e:
            print("Execution failed:" + e)
            # wait before restart
            time.sleep(0.5)


if __name__ == "__main__":
    main()
