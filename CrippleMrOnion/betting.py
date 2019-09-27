def bet(bettor, pot):
    """
    Prompts the current player for an amount to bet and subtracts it from their bank
    :param pot: Current pot for the round
    :param bettor: a player object
    :return:
    """
    my_bet = int(input("How much do you want to bet? "))
    bettor.subtract_money(my_bet)
    pot += my_bet


def call(bettor, pot):
    """
    Calls the bet and matches the current pot
    :param bettor:
    :param pot:
    :return:
    """


def fold(player):
    """
    Player folds on this hand
    :param player: player object
    :return:
    """
    player.hand.move_cards(discards, len(player.hand))