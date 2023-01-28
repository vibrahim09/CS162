#!/usr/bin/env python3
"""[summary]

[extended_summary]
"""
from deck import Deck
import random

random.seed(90)
# Create the deck of cards and display it.
the_deck = Deck()
the_deck.shuffle()

the_deck.display()

player1_hand = []
player2_hand = []

# Deal out 26 cards to each player until deck is empty.
for i in range(5):
    if not the_deck.is_empty():
        player1_hand.append(the_deck.deal())
        player2_hand.append(the_deck.deal())


def display_hand(player_hand: list, player_number: int, cols: int = 13) -> None:
    """Display the player hand in a readable format in columns.

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
    print("\n")

def hand_empty(player_hand: list) -> bool:
    """Checks if a players hand is empty and returns True.
    
        args:
            player_hand (list): a List of cards in each players hand
            
        Returns: 
            bool: True if player_hand is empty.
    """
    return len(player_hand) <= 0


# Starting hands
print("Starting hands")
display_hand(player1_hand, 1)
display_hand(player2_hand, 2)

#Set user variable for iteration.
user = ""

while user != "n":
    """Loops through a battle until either player runs out of
        cards or user input is n.
    """
    #Players deal one card to compare against each other
    card1 = player1_hand.pop(0)
    card2 = player2_hand.pop(0)

    #Compare cards to check who won the battle
    if card1 == card2:
        print(f"Battle was 1: {card1}, 2: {card2}. Battle was a tie!\n")
        player1_hand.append(card1)
        player2_hand.append(card2)
        display_hand(player1_hand, 1)
        display_hand(player2_hand, 2)
    elif card1.rank() is 1:
        print(f"Battle was 1: {card1}, 2: {card2}. Player 1 wins battle!\n")
        player1_hand.extend((card2, card1))
        display_hand(player1_hand, 1)
        display_hand(player2_hand, 2)
    elif card2.rank() is 1:
        print(f"Battle was 1: {card1}, 2: {card2}. Player 2 wins battle!\n")
        player2_hand.extend((card1, card2))
        display_hand(player1_hand, 1)
        display_hand(player2_hand, 2)
    elif card1 > card2:
        print(f"Battle was 1: {card2}, 2: {card1}. Player 1 wins battle!\n")
        player1_hand.extend((card1, card2))
        display_hand(player1_hand, 1)
        display_hand(player2_hand, 2)
    elif card1 < card2:
        print(f"Battle was 1: {card1}, 2: {card2}. Player 2 wins battle!\n")
        player2_hand.extend((card1, card2))
        display_hand(player1_hand, 1)
        display_hand(player2_hand, 2)

    #Check if player hand is empty.
    if hand_empty(player1_hand):
        print("Player 2 wins!")
        break
    elif hand_empty(player2_hand):
        print("Player 1 wins!")
        break
    

    #Check user input
    user = input("Continue... (Nn) to stop the game: ")
    print("\n")

    #If user terminates the game, check who has the longer list to decide the winner
    if user == "n":
        if len(player1_hand) > len(player2_hand):
            print("Player 1 wins!")
        elif len(player1_hand) == len(player2_hand):
            print("It's a tie!")
        else:
            print("Player 2 wins!")
