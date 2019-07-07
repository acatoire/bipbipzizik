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
            self.mode = csv_line.split(",")[2].strip()
            if "" == self.mode:
                raise ValueError("Incorrect Value for mode")
        except (IndexError, ValueError):
            self.mode = "Normal"

        try:
            self.comment = csv_line.split(",")[3].strip()
            if "" == self.comment:
                raise ValueError("Incorrect Value for comment")
        except (IndexError, ValueError):
            self.comment = "no"

    def __str__(self):
        return "[" + self.id + "," + self.cmd + "," + self.mode + "," + self.comment + "]"


class CardList:

    def __init__(self):
        self.file_path = os.path.dirname(os.path.realpath(__file__)) + '/cardList.csv'  # TODO use relative path?
        self.card_list = self.update_list()

    def __str__(self):
        # return [print("[" + element.id + " " + element.cmd + " " + element.mode + "]") for element in self.cardList]
        printed_list = self.card_list.__len__().__str__() + " Recorded cards:\n"
        for element in self.card_list:
            printed_list = printed_list + element.__str__() + "\n"

        return printed_list

    def update_list(self):

        up_to_date_list = []

        for line in open(self.file_path):
            # Exclude comments and empty lines
            if (not line.startswith("#")) and (not "" == line.strip()):
                up_to_date_list.append(Card(line))

        return up_to_date_list

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

    # Test the card creation
    card_test = Card("1,2,3,4")
    print(card_test)
    card_test = Card(",,,")
    print(card_test)
    card_test = Card("")
    print(card_test)

    # Test the card list creation
    card_list = CardList()
    print(card_list)

    # Test the search of card in list
    card = card_list.get_card("0013200813")     # Existing
    if card is not None:
        print(card)

    card = card_list.get_card("0")              # Not Existing
    if card is not None:
        print(card)


if __name__ == "__main__":
    main()
