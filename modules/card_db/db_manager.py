

"""
BIPBIPZIZIK
Manage Firebase db with credential
"""
import sys

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from .card import Card
from .app_config import AppConfig


class DbManager:
    """
    Manage Firebase db with credential
    """

    def __init__(self, bdd_addr, bdd_name, path_to_key_file):
        """
        Card reader constructor.
        @return bdd_addr:
        @return bdd_name:
        @return path_to_key_file:
        """

        self.config_bdd_name = "config_" + bdd_name
        self.card_bdd_name = "cards_" + bdd_name

        try:
            # Fetch the service account key JSON file contents
            credential = credentials.Certificate(path_to_key_file)
        except FileNotFoundError:
            credential = None
            print("FATAL ERROR: Impossible to access to bdd key file \"" + path_to_key_file + "\"")
            sys.exit()

        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(credential, {'databaseURL': bdd_addr})

        self.config_db = db.reference(self.config_bdd_name)
        self.cards_db = db.reference(self.card_bdd_name)

        # TODO stop the app with error if db is empty

        self.cards_db_python = {}
        self.config_db_python = {}

        self.update()

    def update(self):
        """
        Function that update the bdd from the cloud
        @return: nothing
        """

        self.config_db_python = self.config_db.get()
        self.cards_db_python = self.cards_db.get()

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
            if card_id in card.get("ids"):
                return Card(card)

        # Card not found, return None
        return None

    def write_card(self, ids, user, name, action, data, comment, mode):
        """
        Function thar write a new card in the bdd
        @return ids:
        @return user:
        @return name:
        @return action:
        @return data:
        @return comment:
        @return mode:
        @return:
        """

        # TODO check if card already exist
        # If not create it
        # If yes update

        self.cards_db.push({
            'ids': ids,
            'user': user,
            'name': name,
            'action': action,
            'data': data,
            'mode': mode,
            'comment': comment,
        })

    def get_config(self, application_id):
        """
        Function that get searched configuration
        @return application_id: searched application id
        @return: the searched AppConfig or None
        """

        for _, config in self.config_db_python.items():
            if application_id in config.get("app_id"):
                # Creat the config object from json and return it
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

    def write_config(self, app_name, app_owner, app_id, sonos_server_ip,
                     sonos_server_port, room_name, multi_read_mode, card_timeout):
        """
        Function thar write a new card in the bdd
        @return app_name:
        @return app_id:
        @return app_owner:
        @return sonos_server_ip:
        @return sonos_server_port:
        @return room_name:
        @return multi_read_mode:
        @return card_timeout:
        @return:
        """

        self.config_db.push({
            'app_name': app_name,
            'app_owner': app_owner,
            'app_id': app_id,
            'sonos_server_ip': sonos_server_ip,
            'sonos_server_port': sonos_server_port,
            'room_name': room_name,
            'multi_read_mode': multi_read_mode,
            'card_timeout': card_timeout,
        })

    def delete(self, bdd_name):
        """
        Function that clear the whole bdd given in argument
        DANGEROUS: for safety only matching bdd name can be deleted
        @return:
        """
        if bdd_name == self.card_bdd_name:
            print("Delete database: " + bdd_name)
            print(self.cards_db.delete())
        elif bdd_name == self.config_bdd_name:
            print("Delete database: " + bdd_name)
            print(self.config_db.delete())
        else:
            print("Delete Canceled: Database not recognized")

    def print(self):
        """
        Function that print the whole card bdd
        # todo make a print card ans print config
        @return:
        """

        for key, card in self.cards_db_python.items():
            print(key + ":" + str(card))


def main():
    """
    For test purpose
    """
    database = DbManager('https://bipbipzizik.firebaseio.com/', 'prod', 'WriteKey.json')

    # database.print()
    card_test = database.get_card("template")
    card_test.print()
    config_test = database.get_config("template")
    config_test.print()




if __name__ == "__main__":
    main()
