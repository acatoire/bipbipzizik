#
# BIPBIP ZIZIK
# cardMemory class
#
#


from threading import Timer
from time import sleep


class CardMemory:
    def __init__(self, csv_line):

        self.memory = ""
        self.memory_timer = Timer(1.0, self.clear)

    def get(self):

        return self.memory

    def set(self, value):

        self.memory = value
        self.memory_timer.cancel()
        self.memory_timer.start()

    def clear(self):

        self.memory = ""


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
