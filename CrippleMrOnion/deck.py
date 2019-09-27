import random
from cards import Card


class Deck:
    """
    Represents a dek of cards
    Attributes:
        cards: a list of card objects
    """

    def __init__(self):
        self.cards = []
        for suit in Card.Suit:
            for rank in Card.Rank:
                card = Card(rank, suit)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return ', '.join(res)

    def add_card(self, card):
        """
        Adds a card to the deck
        :param card: card object
        :return: n/a
        """
        self.cards.append(card)

    def remove_card(self, card):
        """
        Removes a card from the deck
        :param card:
        :return:
        """
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """
        Removes and returns a card from the deck
        i = index of the card to pop by default it pops the last card
        :return: card object
        """
        return self.cards.pop(i)

    def shuffle(self):
        """
        shuffles the cards in the deck
        :return:
        """
        random.shuffle(self.cards)

    def sort(self):
        """
        Sorts cards in ascending order
        :return:
        """
        self.cards.sort()

    def move_cards(self, hand, num):
        """
        Moves the given number of cards from the deck into the hand
        :param hand: destination Hand object
        :param num: integer number of cards to move
        :return:
        """
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """
    Represents a hand of playing cards
    """

    def __init__(self, label=""):
        self.cards = []
        self.label = label
