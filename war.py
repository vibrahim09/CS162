#!/usr/bin/env python3
"""[summary]

[extended_summary]
"""
from deck import Deck

# Create the deck of cards
the_deck = Deck()
the_deck.shuffle()

the_deck.display()
player1_hand = []
player2_hand = []

for i in range(1, len(the_deck) + 1):
    if not the_deck.is_empty():
        player1_hand.append(the_deck.deal())
        player2_hand.append(the_deck.deal())


print(len(player1_hand))
print(len(player2_hand))
for i in player1_hand:
    print(i, end=" ")

print()

card1 = player1_hand.pop()
card2 = player2_hand.pop()
print(card1)
print(card2)