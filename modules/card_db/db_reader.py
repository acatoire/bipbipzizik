

"""
BIPBIPZIZIK
Module to access in read only to firebase database
"""

from firebase import firebase

from modules.card_db.card import Card
from modules.card_db.app_config import AppConfig


class DbReader:
    """
    database reader class
    """

    def __init__(self, bdd_addr, bdd_name):
        """
        Card reader constructor.
        @return bdd_name:
        """

        self.config_bdd_name = "config_" + bdd_name
        self.card_bdd_name = "cards_" + bdd_name

        self.database = firebase.FirebaseApplication(bdd_addr, None)

        # Todo stop the app with error if db is empty

        self.cards_db_python = {}
        self.config_db_python = {}

        self.update()

    def update(self):
        """
        Function that update the bdd from the cloud
        @return: nothing
        """

        self.config_db_python = self.database.get('/' + self.config_bdd_name, None)
        self.cards_db_python = self.database.get('/' + self.card_bdd_name, None)

    def count_cards(self):
        """
        Function that return the number of cards in th bdd
        @return: the number of cards
        """

        return self.cards_db_python.__len__()

    def count_configs(self):
        """
        Function that return the number of configs in th bdd
        @return: the number of configs
        """

        return self.config_db_python.__len__()

    def get_card(self, card_id):
        """
        Function that get a dict of a searched card
        @return card_id: searched card id
        @return: the searched Card or None
        """

        for _, card in self.cards_db_python.items():
            if card_id in card.get("ids").split(","):
                return Card(card)

        # Card not found, return None
        return None

    def get_config(self, application_id):
        """
        Function that get searched configuration
        @return application_id: searched application id
        @return: the searched AppConfig or None
        """

        for _, config in self.config_db_python.items():
            if application_id in config.get("app_id"):
                # Create the config object from json and return it
                return AppConfig(
                    app_name=config.get("app_name"),
                    app_owner=config.get("app_owner"),
                    app_id=config.get("app_id"),
                    sonos_server_ip=config.get("sonos_server_ip"),
                    sonos_server_port=config.get("sonos_server_port"),
                    room_name=config.get("room_name"),
                    multi_read_mode=config.get("multi_read_mode"),
                    card_timeout=int(config.get("card_timeout"))
                    )

        # Config not found, return None
        return None

    def print(self):
        """
        Function that print the whole card bdd
        # todo make a print card ans print config
        @return:
        """

        for key, card in self.cards_db_python.items():
            print(key + ":" + str(card))
