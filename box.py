#!/usr/bin/env python

#
# BIPBIPZIZIK
# Main Application
#

# Python import
import subprocess
from time import time, sleep
import requests

# Bipbipzizic import
from modules.rfid_reader.Reader import Reader
from modules.card_memory.CardMemory import CardMemory
from modules.cards_bdd.Card import Card
from modules.cards_bdd.AppConfig import AppConfig
from modules.cards_bdd.DbManager import DbManager
from modules.tools import get_serial


def main():

    UPDATE_PERIOD = 60

    reader = Reader()
    database = DbManager('https://bipbipzizik.firebaseio.com/', 'prod', 'modules/cards_bdd/serviceAccountKey.json')

    app_serial = get_serial()
    cfg = database.get_config(app_serial)
    cfg.print() #TODO investigate why config db is empty sometimes if no print is done

    previous_card = CardMemory(cfg.cfg_card_timeout)
    last_update_time = time()

    while True:
        print('Ready: place a card on top of the reader')

        # Wait for a card to be read
        read_id = reader.read_card()

        try:
            print('Read card : ', read_id)

            # Find the card in database
            card = database.get_card(read_id)

            if card is None:
                print('Failed to read card from database')

            else:
                # Card execution
                mode = card.get_mode()
                command = card.get_command()

                print('Command : ', command)
                print('Modes : ', mode)

                if (previous_card.get() == read_id) and ("cancel" == cfg.cfg_multi_read_mode) and (not card.is_command()):
                    # Cancel the read
                    print('Multi read : card canceled')
                else:
                    # Update the previous card memory
                    previous_card.set(read_id)

                    if card.has_mode("ClearQueue"):
                        command_line = cfg.get_sonos_cmd("clearqueue")
                        print(command_line)
                        response = requests.get(command_line)
                        print(response.text)

                    if command is not None:
                        command_line = cfg.get_sonos_cmd(command)
                        print(command_line)
                        response = requests.get(command_line)
                        print(response.text)

            # Update the database periodically
            if (time() - last_update_time) > UPDATE_PERIOD:
                database.update()
                last_update_time = time()
                # TODO Write last update time on config database

        except OSError as e:
            print("Execution failed:" + e.strerror)

        # wait before restart
        sleep(0.5)


if __name__ == "__main__":
    main()
