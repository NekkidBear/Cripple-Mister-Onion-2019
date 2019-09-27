
from enum import Enum


class Card(tuple):
    """
    Represents a standard playing card.

    Attributes:
        self.Suit: Hearts, Clubs, Spades, Diamonds, Cups, Swords, Coins, and Wands
        self.Rank: Ace, 2-10, Jack, Queen, King
    """
    class Rank(Enum):
        Ace = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5
        Six = 6
        Seven = 7
        Eight = 8
        Nine = 9
        Ten = 10
        Jack = 11
        Queen = 12
        King = 13

    class Suit(Enum):
        Hearts = 1
        Clubs = 2
        Spades = 3
        Diamonds = 4
        Cups = 5
        Swords = 6
        Coins = 7
        Wands = 8

    def __new__(cls, rank, suit):
        assert isinstance(rank, cls.Rank)
        assert isinstance(suit, cls.Suit)
        return tuple.__new__(cls, (rank, suit))

    @property
    def rank(self):
        return self[0]

    @property
    def suit(self):
        return self[1]

    def __str__(self):
        """
        Returns a human readable string representing the card.
        """
        return f"{self.rank.name} of {self.suit.name}"

    def __lt__(self, other):
        """
        Compares and returns a boolean if this card is less than the other card
        :param other:
        :return: boolean
        """
        return self.rank.value < other[0].value

    def __gt__(self, other):
        """
        Compares and returns a boolean if this card is greater than the other card
        :param other: tuple representing another card
        :return: boolean
        """
        return self.rank > other[0]

    def __eq__(self, other):
        """
        Compares and returns a boolean if this card is equal to the other card
        :param other: tuple representing another card
        :return: boolean
        """

        return self.rank == other[0] and self.suit == other[1]

    def __setattr__(self, *ignored):
        raise NotImplementedError

    def __delattr__(self, *ignored):
        raise NotImplementedError
