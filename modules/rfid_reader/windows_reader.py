

"""
MUSIC CARD
Card Reader
"""

import os.path
import sys

from select import select


class Reader:
    """
    Reader class to handle card read on linux
    """

    @staticmethod
    def read_card():
        """
        Function to read the cards.
        It concatenate all characters until finding 'KEY_ENTER'
        The final word is returned
        :return: card key as string
        """

        keys_input = input('Card id: ')

        if not keys_input:
            keys_input = "error"

        return keys_input
