#!/usr/bin/env python3
"""[summary]

[extended_summary]
"""
from deck import Deck
import random

random.seed(100)
# Create the deck of cards and display it.
the_deck = Deck()
the_deck.shuffle()

the_deck.display()

player1_hand = []
player2_hand = []

# Deal out 26 cards to each player until deck is empty.
for i in range(26):
    if not the_deck.is_empty():
        player1_hand.append(the_deck.deal())
        player2_hand.append(the_deck.deal())


def display_hand(player_hand: list, player_number: int, cols: int = 13) -> None:
    """
        Display the player hand in a readable format.

        args:
            player_list (list): a List that includes the players cards.
            player_number (int): The number of the player.
            cols (int, optional): The amount of columns to display the players hand,
                defaults to 13.

        

    """
    print(f"Player {player_number} hand: ", end="")
    for index, card in enumerate(player_hand):
        if not index % cols:
            print()
        print(f"{card!s:4}", end="")
    print("\n" * 2)

display_hand(player1_hand, 1)

display_hand(player2_hand, 2)

print("\n" * 2)

card1 = player1_hand.pop(0)
card2 = player2_hand.pop(0)
print(card1)
print(card2)

print(len(player1_hand))