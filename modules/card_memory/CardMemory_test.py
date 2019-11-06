#
# BIPBIP ZIZIK
# cardMemory class
#
#

import unittest

from time import sleep

from modules.card_memory.CardMemory import CardMemory


class CardMemoryTest(unittest.TestCase):

    def setUp(self):
        self.empty = "empty"
        self.fill = "fill"
        self.time_value = 2.0
        self.memo = CardMemory(self.time_value, self.empty)

    def test_memory(self):

        self.assertEqual(self.memo.get(), self.empty)

        self.memo.set(self.fill)
        sleep(self.time_value - 0.5)
        self.assertEqual(self.memo.get(), self.fill)

        sleep(0.5)
        self.assertEqual(self.memo.get(), self.empty)

    def test_memory_reset(self):

        fill2 = "fill2"

        # Fill first value
        self.memo.set(self.fill)

        # Wait 1s to fill second value
        sleep(1.0)
        self.memo.set(fill2)
        self.assertEqual(self.memo.get(), fill2)

        # Wait 1.5s to have elapsed the initial timer
        # Value should be the second one
        sleep(1.5)
        self.assertEqual(self.memo.get(), fill2)

        # Wait 1s to have elapsed the second timer
        sleep(1.0)
        self.assertEqual(self.memo.get(), self.empty)

    def test_memory_double_use(self):

        # Fill first value
        self.memo.set(self.fill)
        # Wait 1s the end of the memory
        sleep(1.0)
        self.assertEqual(self.memo.get(), self.fill)
        # Wait 3s the end of the memory
        sleep(2.0)
        self.assertEqual(self.memo.get(), self.empty)

        # Try another use
        self.memo.set(self.fill)
        # Wait 1s the end of the memory
        sleep(1.0)
        self.assertEqual(self.memo.get(), self.fill)
        # Wait 3s the end of the memory
        sleep(2.0)
        self.assertEqual(self.memo.get(), self.empty)


if __name__ == '__main__':

    unittest.main()
