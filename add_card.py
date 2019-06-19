#from readtest import *
from CardList import CardList
from Reader import Reader
reader = Reader()
cardList = CardList()

while True:
        print('Place the card in the reader')
        card = reader.readCard()
        plist=input('Specify Google Playlist Name-NoSpaces, q to quit')
        if plist=="q":
                break
	cardList.addPlaylist(card, plist)
print("Exiting")
