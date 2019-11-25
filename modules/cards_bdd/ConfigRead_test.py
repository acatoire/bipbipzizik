#
# BIPBIPZIZIK
# Unit test for Card and FirebaseBdd classes
# It test the read of cards on production database with a public key
#

import unittest

from modules.cards_bdd.Card import Card
from modules.cards_bdd.DbManager import DbManager


class ConfigRead(unittest.TestCase):

    @classmethod
    #def setUpClass(cls):

        #cls.bdd = DbManager('https://bipbipzizik.firebaseio.com/', 'prod', 'ReadKey.json')

    # def setUp(self):
        # nothing yet

    def test_read_config(self):
        card_expected = {"app_name": "For test purpose",
                         "app_owner": "axel",
                         "app_id": "template",
                         "sonos_server_ip": "HHH.UUU.GGG.OOO",
                         "sonos_server_port": "2017",
                         "room_name": "Ginette",
                         "multi_read_mode": "none",
                         "card_timeout": "42"}
        self.database = DbManager('https://bipbipzizik.firebaseio.com/', 'prod', 'ReadKey.json')
        config = self.database.get_config("template")
        config.print()
        self.assertEqual(config.cfg_sonos_server_port, "2017")
        self.assertEqual(config.cfg_app_name, "For test purpose")


if __name__ == '__main__':

    unittest.main()

