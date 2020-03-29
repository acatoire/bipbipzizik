

"""
BIPBIPZIZIK
cardMemory class
"""

from time import time


class TimedMemory:
    """
    Class to manage an automatic memory for a value
    Anything can be saved in the memory
    The memory is automatically cleared to default value after a given timeout
    """

    def __init__(self, timeout_value: float, default_value=None):
        """
        Memory creation and init
        @param timeout_value: Time value in second
        @param default_value: (Optional) Default value returned if the timeout is elapsed, default is None
        @return None
        """

        self.timeout_value = timeout_value
        self.default_value = default_value
        self.saved_value = default_value

        self.start_time = time()

    def clear(self):
        """
        Clear the memory
        After a memory clear, it will only return the default value given at init
        @return: None
        """

        self.start_time = time() + self.timeout_value

    @property
    def value(self):
        """
        Value saved in the memory
        @return: saved value ot default if the timeout occurs
        """
        elapsed_time = time() - self.start_time

        if elapsed_time < self.timeout_value:
            value = self.saved_value
        else:
            value = self.default_value

        return value

    @value.setter
    def value(self, element_to_save):
        """
        Save a new element in the memory
        @return element_to_save:
        @return: None
        """

        self.start_time = time()
        self.saved_value = element_to_save
