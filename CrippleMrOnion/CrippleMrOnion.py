import deck
import player


# Initialize the game variables
cmo_deck = deck.Deck()
discards = deck.Hand()
cmo_deck.shuffle()
players = []
current_player = ""
pot = 0


def setup_game():
    num_players = 0
    # Ask for the number of players
    while num_players < 2 or num_players > 7:
        num_players = int(input("How many players? (enter a number between 2 and 7) "))

    # initialize players
    for i in range(num_players):
        player_name = input(f"Player {i + 1}, What is your name? ")

        # Create a player instance for each
        new_player = player.Player()

        # set name to player[i]
        new_player.player_name = player_name

        # assign starting bank
        new_player.bank = 100

        # initialize hand
        new_player.hand = deck.Hand()
        players.append(new_player)


def deal_cards(num_cards, num_players):
    for i in range(num_cards):
        for j in range(num_players):
            # deal one card to each player until there are num_cards in each player's hand
            cmo_deck.move_cards(players[j].hand, 1)


def main():
    setup_game()
    deal_cards(5, len(players))  # face up cards
    print(str(players))
    # bet
    deal_cards(5, len(players))  # face down cards
    # bet
    # score hands
    # declare winner and award the pot
    # play another hand?


main()
