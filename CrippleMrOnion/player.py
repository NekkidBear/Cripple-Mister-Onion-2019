import deck


class Player:
    """
    Represents a player with a hand of cards and a bank for betting
    """
    def __init__(self, hand=None, bank=0, player_name='player'):
        if hand is None:
            hand = deck.Hand()
        self.hand = hand
        self.bank = bank
        self.player_name = player_name

    def add_money(self, amt):
        self.bank += amt

    def subtract_money(self, amt):
        self.bank -= amt

    def __repr__(self):
        return f"""\n\nName:\t{self.player_name}\nMoney:\t{self.bank}\nCards:\t{self.hand}"""
