#!/usr/bin/env python3
"""Define the Deck class."""
import random

from card import Card


class Deck:
    """Model a deck of 52 playing cards.

    Implement the deck as a list of cards.  The last card in the list is
    defined to be at the top of the deck.
    """

    def __init__(self) -> None:
        """Initialize deck.

        Ace of clubs on bottom, King of spades on top.
        """
        self.__deck = [Card(r, s) for s in range(1, 5) for r in range(1, 14)]

    def __len__(self) -> int:
        """Return number of cards remaining in deck.

        Returns:
            int: The number of cards remaining in the deck.
        """
        return len(self.__deck)

    def __repr__(self) -> str:
        """Generate a string representation of the deck.

        The output of repr() is meant to aid debugging. Is should uniquely
        identify the object.

        Returns:
            str: A string from which the card could be instantiated.
        """
        return str(self)

    def __str__(self) -> str:
        """Generate a string representation of the deck.

        Returns:
            str: A string representation of the deck.
        """
        return ", ".join([str(card) for card in self.__deck])

    def shuffle(self) -> None:
        """Shuffle the deck in place."""
        random.shuffle(self.__deck)

    def deal(self) -> Card:
        """Deal a card from the deck.

        Return top card from deck; None, if the deck is empty.

        Returns:
            Card: An instance of the Card class.
        """
        return self.__deck.pop()

    def display(self, cols: int = 13) -> None:
        """Display the entire deck.

        Compute a column-oriented display of deck.

        Args:
            cols (int, optional): A string representing the cards in the deck in
                order. Defaults to 13 columns.
        """
        for index, card in enumerate(self.__deck):
            if not index % cols:
                print()
            print(f"{card!s:4}", end="")
        print("\n" * 2)

    def is_empty(self) -> bool:
        """Return True if the Deck is empty.

        Returns:
            Boolean: True if the Deck is empty; False, otherwise.
        """
        return len(self.__deck) <= 0
