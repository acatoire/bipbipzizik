

from modules.cards_csv.CardList import CardList
from modules.rfid_reader.linux_reader import Reader

reader = Reader()
cardList = CardList()

while True:
    print('Place the card in the reader')
    card = reader.read_card()
    plist = input('Specify Google Playlist Name-NoSpaces, q to quit')
    if plist == "q":
        break
    cardList.add_card(card, plist)

print("Exiting")
