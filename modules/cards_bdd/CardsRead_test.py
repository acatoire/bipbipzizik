#
# BIPBIPZIZIK
# Unit test for Card and FirebaseBdd classes
# It test the read of cards on production database with a public key
#

import unittest

from modules.cards_bdd.Card import Card
from modules.cards_bdd.DbManager import DbManager


class CardsRead(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.bdd = DbManager('https://bipbipzizik.firebaseio.com/', 'prod', 'ReadKey.json')

    # def setUp(self):
        # nothing yet

    def test_read_card(self):
        card_expected = {"user": "user",
                         "name": "name",
                         "comment": "comment",
                         "ids": "template",
                         "mode": "mode",
                         "action": "action",
                         "data": "data"}

        card = self.bdd.get_card("template")

        self.assertEqual(card.parameters, card_expected)


if __name__ == '__main__':

    unittest.main()

