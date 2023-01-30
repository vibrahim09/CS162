#!/usr/bin/env python3
"""Define the Card class."""


class Card:
    """Model a playing card.

    Rank is an int (1-13), where aces are 1 and kings are 13.
    Suit is an int (1-4), where clubs are 1 and spades are 4.
    Value is an int (1-10), where aces are 1 and face cards are 10.
    """

    # List to map int rank to printable character (index 0 used for no rank)
    rank_list = ["x", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # List to map int suit to printable character (index 0 used for no suit)
    # 1 is clubs, 2 is diamonds, 3 is hearts, and 4 is spades
    suit_list = ["x", "\u2663", "\u2666", "\u2665", "\u2660"]

    def __init__(self, rank: int = 0, suit: int = 0) -> None:
        """Initialize card to specified rank (1-13) and suit (1-4).

        Args:
            rank (int, optional): The card's rank. Defaults to 0.
            suit (int, optional): The card's suit. Defaults to 0.
        """
        self.__rank = 0
        self.__suit = 0
        self.__face_up = None

        # Verify that rank and suit are integers and that they are within range
        # (1-13 and 1-4), then update instance variables if valid.
        if isinstance(rank, int) and isinstance(suit, int):
            # if type(rank) == int and type(suit) == int:
            if rank in range(1, 14) and suit in range(1, 5):
                self.__rank = rank
                self.__suit = suit
                self.__face_up = True

    def __eq__(self, other) -> bool:
        """Compare two cards.

        Args:
            other (Card): An instance of a Card.

        Returns:
            Boolean: True, if both Cards are of equal rank; False otherwise.
        """
        if not isinstance(other, Card):
            return False

        return self.rank() == other.rank()

    def __gt__(self, other) -> bool:
        """Compute if the rank of this card is greater than the rank of the other card.

        Args:
            other (Card): An instance of a Card.

        Returns:
            bool: True if the rank of this card is greater than other's rank.
        """
        if not isinstance(other, Card):
            return False

        return self.rank() > other.rank()

    def __hash__(self) -> int:
        """Compute the hash of the object.

        Returns:
            int: A unique value representing the card.
        """
        return hash(self.__key())

    def __key(self) -> tuple[int, int]:
        """Generate a unique key value for the card.

        Returns:
            tuple[int, int]: A value that represents the card.
        """
        return (self.__rank, self.__suit)

    def __lt__(self, other) -> bool:
        """Compute if the rank of this card is less than the rank of the other card.

        Args:
            other (Card): An instance of a Card.

        Returns:
            bool: True if the rank of this card is less than other's rank.
        """
        if not isinstance(other, Card):
            return False

        return self.rank() < other.rank()

    def __repr__(self) -> str:
        """Generate a string representation of the card.

        The output of repr() is meant to aid debugging. Is should uniquely
        identify the object and it should be possible to instantiate a new
        object using the returned value.

        Returns:
            str: A string from which the card could be instantiated.
        """
        return f"Card(rank = {self.__rank}, suit = {self.__suit})"

    def __str__(self) -> str:
        """Generate a string representation of the card.

        The output of str() is meant to be human-readable.

        Returns:
            str: A string representation of the card.
        """
        # Use rank to index into rank_list; use suit to index into suit_list.
        if self.__face_up:
            return f"{self.rank_list[self.__rank]}{(self.suit_list)[self.__suit]}"

        return "XX"

    def flip_card(self) -> None:
        """Flip card between face-up and face-down."""
        self.__face_up = not self.__face_up

    def is_face_up(self) -> bool | None:
        """Return True if card is facing up.

        Returns:
            Boolean: True if the card is face up; False, otherwise.
        """
        return self.__face_up

    def rank(self) -> int:
        """Get the rank of the card.

        The card's rank is an integer in the range 1 (Ace) to 13 (King).

        Returns:
            int: The card's rank.
        """
        return self.__rank

    def suit(self) -> int:
        """Get the suit of the card.

        The card's suit is an integer 1 (clubs), 2 (hearts), 3 (diamonds), or
        4 (spades).

        Returns:
            int: The card's suit.
        """
        return self.__suit

    def value(self) -> int:
        """Get the value of the card.

        The card's value (1 for aces, 2-9, 10 for face cards).

        Returns:
            int: The card's value.
        """
        return self.__rank if self.__rank < 10 else 10
