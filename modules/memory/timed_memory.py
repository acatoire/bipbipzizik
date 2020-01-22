

"""
BIPBIPZIZIK
cardMemory class
"""


from threading import Timer


class TimedMemory:
    """
    Class to manage an automatic memory for an element
    Anything can be saved in the memory
    The memory is automatically cleared to default value after a timeout
    """
    def __init__(self, timeout_value, reset_value=None):
        """
        Constructor for a memory
        :param timeout_value:
        :param reset_value: Optional reset value, default is None
        """

        self.timeout_value = timeout_value
        self.reset_value = reset_value

        # equivalent to init_timer
        self.memory = self.reset_value
        self.memory_timer = Timer(self.timeout_value, self.clear)

    def get(self):
        """
        Get the element saved in the memory
        :return: saved card or None if timeout occur
        """

        return self.memory

    def set(self, element_to_save):
        """
        Save a new element in the memory
        :param element_to_save:
        :return: None
        """

        self.memory = element_to_save

        if not self.memory_timer.is_alive():
            self.memory_timer.start()
        else:
            self.memory_timer.cancel()
            self.memory_timer = Timer(self.timeout_value, self.clear)
            self.memory_timer.start()

    def clear(self):
        """
        Clear the memory
        :return:
        """

        self.memory_timer.cancel()
        self._init_timer()

    def _init_timer(self):
        """
        Initialise the memory timer
        :return:
        """

        self.memory_timer = Timer(self.timeout_value, self.clear)
        self.memory = self.reset_value
