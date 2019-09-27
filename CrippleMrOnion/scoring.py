from enum import Enum


class SuitPairs(Enum):
    Clubs = 1
    Swords = 1
    Spades = 2
    Wands = 2
    Hearts = 3
    Cups = 3
    Diamonds = 4
    Coins = 4


def bagel(player_name.hand):
"""
checks to see if the value of any two cards in the player's hand = 21
player_name = current player
"""

    for card in player_name.hand:
        