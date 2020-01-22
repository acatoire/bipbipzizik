#!/usr/bin/env python

"""
BIPBIPZIZIK
main application
"""

# Python import
from time import time, sleep
import requests

# Bipbipzizic import
from modules.rfid_reader.linux_reader import Reader
from modules.memory.timed_memory import TimedMemory
from modules.card_db.db_reader import DbReader
from modules.tools import get_serial

# Constants
UPDATE_PERIOD = 60


def main():
    """
    Application main function
    :return: None
    """

    reader = Reader()
    database = DbReader('https://bipbipzizik.firebaseio.com/', 'prod')

    app_serial = get_serial()
    cfg = database.get_config(app_serial)
    cfg.print()

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

        except OSError as exception:
            print("Execution failed:" + exception.strerror)

        # wait before restart
        sleep(0.5)


if __name__ == "__main__":
    main()
