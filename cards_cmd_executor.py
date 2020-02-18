

"""
BIPBIPZIZIK
Fake Unit test for card command execution
It run some known cards directly as unit test to test in on any computers.
"""

import unittest

from card_launcher import CardLauncher


class CardsWrite(unittest.TestCase):
    """
    Set of unit test of firebase cards database
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup for all unit test
        :return: None
        """

        cls.launcher = CardLauncher('https://bipbipzizik.firebaseio.com/', 'prod')
        cls.launcher.config_update('000000008e3c2b91')

    # def setUp(self):
        # nothing yet

    def test_playpause(self):
        """
        Test card read on production database
        :return
        """
        self.launcher.execute_card('0013397903')

    def test_mathieu_shedid(self):
        """
        Test card read on production database
        :return
        """
        self.launcher.execute_card('0013365376')

    def test_gorillaz(self):
        """
        Test card read on production database
        :return
        """
        self.launcher.execute_card('0005585628')


if __name__ == '__main__':

    unittest.main()
