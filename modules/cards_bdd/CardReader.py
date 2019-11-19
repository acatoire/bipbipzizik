#
# BIPBIP ZIZIK
# cardReader class
#
#


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class Card:

    def __init__(self, card_dict):
        self.parameters = card_dict

    def print(self):
        """
        Function that print a card parameters found from its id
        :return:
        """

        if self.parameters is not None:
            print("Card found:")
            for param, value in self.parameters.items():
                print("    - " + param + ": " + value)
        else:
            print("Card not found in bdd\n")

    def get_command(self):
        """
        Function that create the command from card parameters found from its id
        :return:
        """

        # This dict can be easily completed with more command
        action_dict = {"spotify:album": "spotify/now/spotify:album:%DATA%",
                       "spotify:playlist": "spotify/now/spotify:user:spotify:playlist:%DATA%",
                       "spotify:track": "spotify/now/spotify:track:%DATA%",
                       "tunein": "tunein/play/%DATA%",
                       "command": "%DATA%",}

        if self.parameters is not None:
            # Card found create the command line
            action = self.parameters.get("action")
            data = self.parameters.get("data")

            if action in action_dict:
                command = action_dict.get(action).replace("%DATA%", data)
            else:
                command = None
        else:
            command = None

        return command

    def get_mode(self):
        if self.parameters is not None:
            # Card found create the command line
            mode = self.parameters.get("mode")

            if mode == "none" or mode == "":
                mode = None

        else:
            mode = None

        return mode

    def has_mode(self, mode):

        if self.parameters.get("mode") == mode:
            mode_exist = True
        else:
            mode_exist = False

        return mode_exist

    def is_command(self):

        if self.parameters.get("action") == "command":
            return True
        else:
            return False


class CardBdd:

    def __init__(self, bdd_addr, bdd_name):
        """
        Card reader constructor.
        :param bdd_addr:
        :param bdd_name:
        """

        # Fetch the service account key JSON file contents
        cred = credentials.Certificate('serviceAccountKey.json')

        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(cred, {
            'databaseURL': bdd_addr
        })

        self.cards_db = db.reference(bdd_name)
        self.cards_db_python = self.cards_db.get()  # Todo refresh the bdd periodically

    def get_card(self, card_id):
        """
        Function that get a dict of a searched card
        :param card_id: searched card id
        :return: the searched Card or None
        """

        for key, card in self.cards_db_python.items():
            if card_id in card.get("ids"):
                return Card(card)


    def write_card(self, ids, user, name, action, data, comment, mode):
        """
        Function thar write a new card in the bdd
        :param ids:
        :param user:
        :param name:
        :param action:
        :param command:
        :param comment:
        :param mode:
        :return:
        """

        # check if card already exist
        # If not creat
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

    def delete(self):
        """
        Function that clear the whole card bdd
        DANGEROUS
        :return:
        """

        print(self.cards_db.delete())

    def print(self):
        """
        Function that print the whole card bdd
        :return:
        """

        print(self.cards_db.get())


# For test purpose
def main():

    card_reader = CardBdd('https://bipbipzizik.firebaseio.com/', 'cards')

    card = card_reader.get_card('0013365376')

    card.print()
    print(card.get_command())


if __name__ == "__main__":
    main()
