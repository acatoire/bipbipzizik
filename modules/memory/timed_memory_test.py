"""
BIPBIPZIZIK
Unit test for timed memory classe

"""

import unittest

from time import sleep

from modules.memory.timed_memory import TimedMemory


class TimedMemoryTest(unittest.TestCase):
    """
    Set of unit test of firebase cards database
    """

    def setUp(self):
        """
        Setup for each unit test
        :return:
        """

        self.empty = "empty"
        self.fill = "filled"
        self.timeout_value = 2.0
        self.memory = TimedMemory(self.timeout_value, self.empty)

    def test_memory(self):
        """
        Basic check of the auto reset
        :return:
        """

        self.assertEqual(self.memory.get(), self.empty)

        self.memory.set(self.fill)
        sleep(self.timeout_value - 0.5)
        self.assertEqual(self.memory.get(), self.fill)

        sleep(0.5)
        self.assertEqual(self.memory.get(), self.empty)

    def test_memory_reset(self):
        """
        Check the re-use of a running timer
        :return:
        """

        fill2 = "fill2"

        # Fill first value
        self.memory.set(self.fill)

        # Wait 1s to fill second value
        sleep(1.0)
        self.memory.set(fill2)
        self.assertEqual(self.memory.get(), fill2)

        # Wait 1.5s to have elapsed the initial timer
        # Value should be the second one
        sleep(1.5)
        self.assertEqual(self.memory.get(), fill2)

        # Wait 1s to have elapsed the second timer
        sleep(1.0)
        self.assertEqual(self.memory.get(), self.empty)

    def test_memory_double_use(self):
        """
        Check the re-use of a ended timer
        :return:
        """

        # Fill first value
        self.memory.set(self.fill)
        # Wait 1s the end of the memory
        sleep(1.0)
        self.assertEqual(self.memory.get(), self.fill)
        # Wait 3s the end of the memory
        sleep(2.0)
        self.assertEqual(self.memory.get(), self.empty)

        # Try another use
        self.memory.set(self.fill)
        # Wait 1s the end of the memory
        sleep(1.0)
        self.assertEqual(self.memory.get(), self.fill)
        # Wait 3s the end of the memory
        sleep(2.0)
        self.assertEqual(self.memory.get(), self.empty)


if __name__ == '__main__':

    unittest.main()
