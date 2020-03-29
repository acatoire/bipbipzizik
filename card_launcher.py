

"""
BIPBIPZIZIK
launcher for card
"""

# Python import
import requests

# Bipbipzizic import
from modules.card_db.db_reader import DbReader
from modules.memory.timed_memory import TimedMemory


class CardLauncher:
    """
    Class that manage a card and config database to run cards in it
    """
    def __init__(self, database_address, database_name):

        self.database = DbReader(database_address, database_name)
        self.database_update()

        # Followings members will be updated by a config_update()
        self.config = None
        self.memory = None

    def database_update(self):
        """
        Update the database
        @return: None
        """
        self.database.update()

    def config_update(self, config_id):
        """
        Update used config
        @return config_id: id of the config to be used
        @return: None
        """
        self.config = self.database.get_config(config_id)

        if self.config is None:
            raise Exception("The config for " + config_id + " is not present in the bipbipzizik database." +
                            "Did you create it?")

        self.memory = TimedMemory(self.config.cfg_card_timeout)

        print(self.config)

    def execute_card(self, card_id):
        """
        Execute a card command
        @return card_id: card to be run
        @return: error code
        - 0 if all OK
        - 1 if card is not found
        - 2 if card is canceled by the memory
        - 3 if card command was not valid
        """

        if None is self.config:
            raise Exception('No config found, you should execute a config_update first')

        # Find the card in database
        card = self.database.get_card(card_id)

        # Check card validity
        if card is None:
            print('Card not found in database')
            return 1

        # Card execution
        mode = card.get_mode()
        command = card.get_command()

        print('Command : ', command)
        print('Modes : ', mode)

        if self.config.cfg_multi_read_mode == "cancel" and not card.is_command():
            # Card cancel is allowed
            if self.memory.get() == card_id:
                # Cancel the read
                print('Card not executed: the card is still active in th memory')
                return 2

        # Update the memory with the new card
        self.memory.set(card_id)

        # Handle the clear queue needs
        if card.has_mode("ClearQueue"):
            # request a clear queue before command line execution
            self.__cmd_execution("clearqueue")

        if command is None:
            #  Cancel the execution
            print('Card not executed: the card command was not valid')
            return 3

        # request the command line execution
        self.__cmd_execution(command)
        return 0

    def __cmd_execution(self, command):

        command_line = self.config.get_sonos_cmd(command)
        print("Execute command: {}".format(command_line))

        try:
            response = requests.get(command_line)
            print("Command response: {}".format(response.text))
        except requests.exceptions.ConnectionError:
            print("Connexion Failed! Is the server up and running?")
