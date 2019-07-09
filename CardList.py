#
# BIPBIP ZIZIK
# Card List class
# Take cards from csv file and manage it
#

import os.path


class Card:
    def __init__(self, csv_line):

        try:
            self.id = csv_line.split(",")[0].strip()
            if "" == self.id:
                raise ValueError("Incorrect Value for id")
        except (IndexError, ValueError):
            self.id = "error"

        try:
            self.cmd = csv_line.split(",")[1].strip()
            if "" == self.cmd:
                raise ValueError("Incorrect Value for cmd")
        except (IndexError, ValueError):
            self.cmd = "error"

        try:
            self.modes = []

            raw_mode = csv_line.split(",")[2].strip()
            if "" == raw_mode:
                raise ValueError("Incorrect Value for mode")
            else:
                for element in raw_mode.split(";"):
                    self.modes.append(element.strip())
        except (IndexError, ValueError):
            self.modes.append("Normal")

        try:
            self.comment = csv_line.split(",")[3].strip()
            if "" == self.comment:
                raise ValueError("Incorrect Value for comment")
        except (IndexError, ValueError):
            self.comment = "no"

    def __str__(self):

        return "[" + self.id + ", " + self.cmd + ", " + self.str_modes() + ", " + self.comment + "]"

    def str_modes(self):
        modes_string = "("
        modes_string += ", ".join(self.modes)
        modes_string += ")"
        return modes_string

    def has_mode(self, mode):

        if 0 != self.modes.count(mode):
            mode_exist = True

        else:
            mode_exist = False

        return mode_exist


class CardList:

    def __init__(self):

        self.file_path = os.path.dirname(os.path.realpath(__file__)) + '/cardList.csv'  # TODO use relative path?
        self.card_list = self.update_list()

    def __str__(self):

        printed_list = self.card_list.__len__().__str__() + " Recorded cards:\n"

        for element in self.card_list:
            printed_list += element.__str__() + "\n"

        return printed_list

    def update_list(self):

        up_to_date_list = []

        file = open(self.file_path)

        for line in file:
            # Exclude comments and empty lines
            if (not line.startswith("#")) and (not "" == line.strip()):
                up_to_date_list.append(Card(line))

        file.close()

        return up_to_date_list

    def size(self):

        return self.card_list.__len__()

    def get_card(self, searched_id):

        # find first occurrence of searched card
        try:
            the_card = next(card for card in self.card_list if card.id == searched_id)
            return the_card

        except StopIteration:
            print("Card " + searched_id + " not found in bdd")
            return None


# For test purpose
def main():

    # Test the card list creation
    card_list = CardList()
    print(card_list)


if __name__ == "__main__":
    main()
