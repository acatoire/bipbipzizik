

"""
BIPBIPZIZIK
Manage cards
"""


class Card:
    """
    Card class
    """

    def __init__(self, card_dict):
        self.parameters = card_dict

    def print(self):
        """
        Function that print a card parameters found from its id
        @return:
        """

        if self.parameters is not None:
            print("Card content:")
            for param, value in self.parameters.items():
                print("    - " + param + ": " + value)
        else:
            print("Card error: no parameters found\n")

    def get_command(self):
        """
        Function that create the command from card parameters found from its id
        @return:
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
        """
        Get the card mode or None if not found
        @return: the mode
        """
        if self.parameters is not None:
            # Card found create the command line
            mode = self.parameters.get("mode")

            if mode in ("none", ""):
                mode = None

        else:
            mode = None

        return mode

    def has_mode(self, mode):
        """
        Check if the card mode is the expected one
        @return mode: expected mode
        @return: True if exist, else otherwise
        """

        mode_exist = self.parameters.get("mode") == mode

        return mode_exist

    def is_command(self):
        """
        Check if the card is a command card
        @return: True if the card is a command, else otherwise
        """

        return self.parameters.get("action") == "command"


def main():
    """
    For test purpose
    Quick card test
    @return: None
    """

    card_dict = dict(
        ids='ids',
        user='user',
        name='name',
        action='action',
        data='data',
        mode='mode',
        comment='comment'
    )

    card_test = Card(card_dict)
    card_test.print()


if __name__ == "__main__":
    main()
