#
#
# BIPBIP ZIZIK
# Unit test for CardList class
#
#

import unittest

from CardList import Card


class TestCard(unittest.TestCase):

    def test_create_normal_card(self):

        card_test = Card("1, 2,3 , 4 ")

        self.assertEqual(card_test.id, '1')
        self.assertEqual(card_test.cmd, '2')
        self.assertEqual(card_test.has_mode("3"), True)
        self.assertEqual(card_test.comment, '4')

    def test_create_multi_mode_card(self):
        card_test = Card("1,2, mode1;mode2 ; mode3 ,4")
        print(card_test.str_modes())
        self.assertEqual(card_test.has_mode("mode1"), True)
        self.assertEqual(card_test.has_mode("mode2"), True)
        self.assertEqual(card_test.has_mode("mode3"), True)
        self.assertEqual(card_test.has_mode("mode4"), False)


if __name__ == '__main__':

    #
    # coverage run CardListTest.py
    # coverage report
    # coverage html
    # coverage purge
    #
    # TODO see the use of  --omit CardListTest.py
    #

    unittest.main()

