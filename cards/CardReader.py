#
# BIPBIP ZIZIK
# cardReader class
#
#


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class CardReader:

    def __init__(self, bdd_name):

        # Fetch the service account key JSON file contents
        cred = credentials.Certificate('serviceAccountKey.json')

        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://bipbipzizik.firebaseio.com/'
        })

        self.cards_db = db.reference(bdd_name)

    def get_card(self, id):

        cards_db_python = self.cards_db.get()

        for card in cards_db_python.items():

            if card[1]["ids"] == id:  # todo multi card with split

                print("Card " + id + " found: \n" +
                      "    - user    : " + card[1]["user"] + "\n" +
                      "    - name    : " + card[1]["name"] + "\n" +
                      "    - ids     : " + card[1]["ids"] + "\n" +
                      "    - mode    : " + card[1]["mode"] + "\n" +
                      "    - type    :" + card[1]["type"] + "\n" +
                      "    - command :" + card[1]["command"] + "\n")

    def write_card(self, user, name, ids, mode, type, command):

        # check if card already exist
        # If not creat
        # If yes update

        self.cards_db.push({
            'user': user,
            'name': name,
            'ids': ids,
            'mode': mode,
            'type': type,
            'command': command
        })

    def read_cards(self):

        print(self.cards_db.get())


# For test purpose
def main():

    card_reader = CardReader('cards')

    #card_reader.write_card( user="axel",
    #                        name="M - Lettre Infinie",
    #                        ids="0013365376",
    #                        mode="none",
    #                        type="spotify:album",
    #                        command="spotify/now/spotify:album:4yYVqX2KierVI3nDV0M2UL")

    #card_reader.write_card( user="axel",
    #                        name="Aldebert Enfantillage 1",
    #                        ids="0013200813",
    #                        mode="ClearQueue",
    #                        type="spotify:album",
    #                        command="spotify/now/spotify:album:1xhy7WWxO28XoPKuFlnxSZ")

    #card_reader.write_card( user="bertrand",
    #                        name="test",
    #                        ids="00000000000",
    #                        mode="ClearQueue",
    #                        type="spotify:album",
    #                        command="spotify/now/spotify:album:1xhy7WWxO28XoPKuFlnxSZ")

    card_reader.read_cards()
    card_reader.get_card('0013365376')


if __name__ == "__main__":
    main()
