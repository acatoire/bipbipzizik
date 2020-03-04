

"""
BIPBIPZIZIK
main application
"""

# Python import
from time import time, sleep

# Bipbipzizic import
from card_launcher import CardLauncher
from sys import platform

if platform == "linux" or platform == "linux2" or  platform == "darwin":
    # linux or OS X
    from modules.tools import get_linux_serial as get_serial
    from modules.rfid_reader.linux_reader import Reader
elif platform == "win32":
    # Windows
    from modules.tools import get_win_serial as get_serial
    from modules.rfid_reader.windows_reader import Reader

# Constants
UPDATE_PERIOD = 60


def main():
    """
    Application main function
    :return: None
    """

    reader = Reader()
    launcher = CardLauncher('https://bipbipzizik.firebaseio.com/', 'prod')
    launcher.config_update(get_serial())

    last_update_time = time()

    while True:
        print('Ready: place a card on top of the reader')

        # Wait for a card to be read
        read_id = reader.read_card()

        print('Read card: ', read_id)

        # Execute the card
        launcher.execute_card(read_id)

        # Update the database periodically
        if (time() - last_update_time) > UPDATE_PERIOD:
            print('Update the database')
            launcher.database_update()
            last_update_time = time()
            # TODO Write last update time on config database for usage tracking

        # wait before restart
        sleep(0.5)


if __name__ == "__main__":
    main()
