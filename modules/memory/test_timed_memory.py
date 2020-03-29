"""
BIPBIPZIZIK
Unit test for timed memory classe

"""

import unittest

from time import sleep, time

from modules.memory.timed_memory import TimedMemory


class TimedMemoryTest(unittest.TestCase):
    """
    Set of unit test of firebase cards database
    """

    def setUp(self):
        """
        Setup for each unit test
        """

        self.empty = "empty"
        self.fill = "filled"
        self.timeout_value = 0.1
        self.memory = TimedMemory(self.timeout_value, self.empty)

    def test_memory(self):
        """
        Basic check of the memory system
        """

        # Check initial value
        self.assertEqual(self.memory.value, self.empty)

        # Save a value in the memory
        self.memory.value = self.fill
        start = time()

        while time() < (start + self.timeout_value - 0.01):
            sleep(0.001)

        # Check saved value before timeout
        self.assertEqual(self.memory.value, self.fill)

        while time() < (start + self.timeout_value + 0.01):
            sleep(0.001)

        # Check saved value after timeout
        self.assertEqual(self.memory.value, self.empty)

    def test_memory_reuse(self):
        """
        Check the re-use of a running memory before timeout
        """

        fill2 = "fill2"

        # Check initial value
        self.assertEqual(self.memory.value, self.empty)

        # Save first value in the memory
        self.memory.value = self.fill
        start = time()

        while time() < (start + self.timeout_value - 0.01):
            sleep(0.001)

        # Check saved value before timeout
        self.assertEqual(self.memory.value, self.fill)

        # Save second value in the memory
        self.memory.value = fill2
        start2 = time()

        while time() < (start + self.timeout_value + 0.01):
            sleep(0.001)

        # Check saved value after first timeout
        self.assertEqual(self.memory.value, fill2)

        while time() < (start2 + self.timeout_value + 0.01):
            sleep(0.001)

        # Check saved value after second timeout
        self.assertEqual(self.memory.value, self.empty)

    def test_memory_double_use(self):
        """
        Check the re-use of a ended timer
        """

        fill2 = "fill2"

        # Check initial value
        self.assertEqual(self.memory.value, self.empty)

        # Save a value in the memory
        self.memory.value = self.fill
        start = time()

        while time() < (start + self.timeout_value - 0.01):
            sleep(0.001)

        # Check saved value before timeout
        self.assertEqual(self.memory.value, self.fill)

        while time() < (start + self.timeout_value + 0.01):
            sleep(0.001)

        # Check saved value after timeout
        self.assertEqual(self.memory.value, self.empty)

        # Check initial value
        self.assertEqual(self.memory.value, self.empty)

        # Save a value in the memory
        self.memory.value = fill2
        start = time()

        while time() < (start + self.timeout_value - 0.01):
            sleep(0.001)

        # Check saved value before timeout
        self.assertEqual(self.memory.value, fill2)

        while time() < (start + self.timeout_value + 0.01):
            sleep(0.001)

        # Check saved value after timeout
        self.assertEqual(self.memory.value, self.empty)


if __name__ == '__main__':

    unittest.main()
