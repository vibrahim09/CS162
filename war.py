#!/usr/bin/env python3
"""[summary]

[extended_summary]
"""
from deck import Deck

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


print(len(player1_hand))
print(len(player2_hand))

def display_hand(player_hand: list, cols: int = 13) -> None:
    """
        Display the player hand in a readable format.
        args:
        player_list: a List that includes the players cards

    """

    for index, card in enumerate(player_hand):
        if not index % cols:
            print()
        print(f"{card!s:4}", end="")
    print("\n" * 2)

for index, card in enumerate(player2_hand):
    if not index % 13:
        print()
    print(f"{card!s:4}", end="")

print("\n" * 2)

card1 = player1_hand.pop()
card2 = player2_hand.pop()
print(card1)
print(card2)

print(len(player1_hand))