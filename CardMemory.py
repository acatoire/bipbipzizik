#
# BIPBIP ZIZIK
# cardMemory class
#
#


from threading import Timer
from time import sleep


class CardMemory:
    def __init__(self, timer, reset_value=""):

        self.timer_value = timer
        self.clear_value = reset_value
        self.memory = reset_value
        self.memory_timer = Timer(self.timer_value, self.clear)

    def get(self):

        return self.memory

    def set(self, value):

        self.memory = value
        if not self.memory_timer.is_alive():
            self.memory_timer.start()
        else:
            self.memory_timer.cancel()
            self.memory_timer = Timer(self.timer_value, self.clear)
            self.memory_timer.start()

    def clear(self):

        self.memory = self.clear_value


# For test purpose
def main():

    # Test the card list creation
    memo = CardMemory()
    print(memo.get())
    memo.set("full")
    print(memo.get())
    sleep(10)
    print(memo.get())


if __name__ == "__main__":
    main()
