#!/usr/bin/env python3
# coding=utf-8
"""Demonstrate some of the operations of the Deck and Card classes."""
import random

from card import Card
from deck import Deck

# Seed the random number generator to a specific value so every execution
# of the program uses the same sequence of random numbers (for testing).
random.seed(100)

# Create a deck of cards
my_deck = Deck()


# Shuffle the deck, then display it in 13 columns
my_deck.shuffle()
print("===== shuffled deck =====")
my_deck.display()


# Deal five cards to each player (alternating)
print("Dealt five cards to each player (alternating)")
print()

player1_list: list[Card] = []
player2_list: list[Card] = []
for i in range(5):
    if not my_deck.is_empty():
        player1_list.append(my_deck.deal())
    if not my_deck.is_empty():
        player2_list.append(my_deck.deal())


# Display each player's cards and the cards still in the deck
print("===== player #1 =====")
print()
print(player1_list)
print()
print("===== player #2 =====")
print()
print(player2_list)
print()
print("===== remaining cards in deck =====")
my_deck.display()


# First card dealt to Player #1
player1_card = player1_list.pop(0)
print(f"First card dealt to player #1: {player1_card}")


# First card dealt to Player #2
player2_card = player2_list.pop(0)
print(f"First card dealt to player #2: {player2_card}")


# Compare the ranks of the two cards
print()
if player1_card == player2_card:
    print(f"Tie: {player1_card} and {player2_card} of equal rank")
elif player1_card > player2_card:
    print(f"Player #1 wins: {player1_card} of higher rank than {player2_card}")
elif player1_card < player2_card:
    print(f"Player #2 wins: {player2_card} of higher rank than {player1_card}")
