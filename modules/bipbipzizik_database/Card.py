#
# BIPBIPZIZIK
# Manage cards
#
#


class Card:

    def __init__(self, card_dict):
        self.parameters = card_dict

    def print(self):
        """
        Function that print a card parameters found from its id
        :return:
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


# For test purpose
def main():

    card_dict = {
                    'ids': 'ids',
                    'user': 'user',
                    'name': 'name',
                    'action': 'action',
                    'data': 'data',
                    'mode': 'mode',
                    'comment': 'comment',
                }

    card_test = Card(card_dict)
    card_test.print()


if __name__ == "__main__":
    main()
