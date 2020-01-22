#!/usr/bin/env python

"""
BIPBIPZIZIK
windows application to test the BIPBIPZIZIK libraries
"""

# Python import
import requests

# Bipbipzizic import
from modules.card_db.db_reader import DbReader

# Constants
UPDATE_PERIOD = 60


def main(card_id):
    """
    Application main function
    :param card_id: card to be run
    :return: None
    """

    database = DbReader('https://bipbipzizik.firebaseio.com/', 'prod')

    app_serial = "000000008e3c2b91"  # Fix serial for test purpose
    cfg = database.get_config(app_serial)
    cfg.print()

    # Find the card in database
    card = database.get_card(card_id)

    if card is None:
        print('Failed to read card from database')

    else:
        # Card execution
        mode = card.get_mode()
        command = card.get_command()

        print('Command : ', command)
        print('Modes : ', mode)

        if (cfg.cfg_multi_read_mode == "cancel") and (not card.is_command()):
            # Cancel the read
            print('Multi read : card canceled')
        else:

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


if __name__ == "__main__":
    # main("0013397903")  # playpause
    main("0013365376")  # Mathieu Shedid
    # main("0005585628")  # Gorillaz

