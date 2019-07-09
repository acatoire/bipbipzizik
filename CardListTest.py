#
#
# BIPBIP ZIZIK
# Unit test for CardList class
#
#

import unittest

from CardList import Card
from CardList import CardList


class TestCard(unittest.TestCase):

    def test_create_normal_card(self):

        card_test = Card("1, 2,3 , 4 ")

        self.assertEqual(card_test.id, '1')
        self.assertEqual(card_test.cmd, '2')
        self.assertEqual(card_test.has_mode("3"), True)
        self.assertEqual(card_test.comment, '4')

    def test_create_multi_mode_card(self):

        card_test = Card("1,2, mode1;mode2 ; mode3 ,4")

        self.assertEqual(card_test.has_mode("mode1"), True)
        self.assertEqual(card_test.has_mode("mode2"), True)
        self.assertEqual(card_test.has_mode("mode3"), True)
        self.assertEqual(card_test.has_mode("mode4"), False)

    def test_create_default_card(self):

        card_test = Card(",,,")

        self.assertEqual(card_test.id, 'error')
        self.assertEqual(card_test.cmd, 'error')
        self.assertEqual(card_test.has_mode("Normal"), True)
        self.assertEqual(card_test.comment, 'no')

        card_test = Card("")

        self.assertEqual(card_test.id, 'error')
        self.assertEqual(card_test.cmd, 'error')
        self.assertEqual(card_test.has_mode("Normal"), True)
        self.assertEqual(card_test.comment, 'no')

    def test_search_card_in_cardList(self):

        card_list = CardList()

        self.assertGreater(card_list.size(), 0)

        card = card_list.get_card("0013200813")

        self.assertNotEqual(card, None)

        card = card_list.get_card("0-0")

        self.assertEqual(card, None)


if __name__ == '__main__':

    #
    # coverage run CardListTest.py
    # coverage report --omit CardListTest.py
    # coverage html --omit CardListTest.py
    # coverage erase
    #

    unittest.main()

