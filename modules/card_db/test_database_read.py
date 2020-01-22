

"""
BIPBIPZIZIK
Unit test for Card and FirebaseBdd classes
It test the read of cards on production database without credential
"""

import unittest

from modules.card_db.db_reader import DbReader


class DatabaseReadTest(unittest.TestCase):
    """
    Set of unit test of firebase read for cards and config
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup for all unit test
        :return: None
        """

        # Create the database handler
        cls.database = DbReader('https://bipbipzizik.firebaseio.com/', 'prod')

    # def setUp(self):
        # nothing yet

    def test_read_card(self):
        """
        Test card read on production database
        :return
        """

        card_expected = {"user": "user",
                         "name": "name",
                         "comment": "comment",
                         "ids": "template",
                         "mode": "mode",
                         "action": "action",
                         "data": "data"}

        card = self.database.get_card("template")

        self.assertEqual(card.parameters, card_expected)

    def test_read_config(self):
        """
        Test config read on production database
        :return
        """

        card_expected = {"app_name": "For test purpose",
                         "app_owner": "axel",
                         "app_id": "template",
                         "sonos_server_ip": "HHH.UUU.GGG.OOO",
                         "sonos_server_port": "2017",
                         "room_name": "Ginette",
                         "multi_read_mode": "none",
                         "card_timeout": "42"}

        config = self.database.get_config("template")

        self.assertEqual(config.cfg_app_name, card_expected.get("app_name"))
        self.assertEqual(config.cfg_app_owner, card_expected.get("app_owner"))
        self.assertEqual(config.cfg_application_id, card_expected.get("app_id"))
        self.assertEqual(config.cfg_sonos_server_ip, card_expected.get("sonos_server_ip"))
        self.assertEqual(config.cfg_sonos_server_port, card_expected.get("sonos_server_port"))
        self.assertEqual(config.cfg_room_name, card_expected.get("room_name"))
        self.assertEqual(config.cfg_multi_read_mode, card_expected.get("multi_read_mode"))
        self.assertEqual(config.cfg_card_timeout, int(card_expected.get("card_timeout")))


if __name__ == '__main__':

    unittest.main()
