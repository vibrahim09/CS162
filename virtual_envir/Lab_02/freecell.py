"""Write a program to create a game of FreeCell

"""
from deck import Deck
from card import Card


class FreeCell():
    """Create a game of FreeCell"""
    deck = Deck()
    deck.shuffle()
    tableau = [[], [], [], [], [], [], [], []]
    foundation = [[], [], [], []]
    cells= [[], [], [], []]
    column = 0
    while not deck.is_empty():
        tableau[column].append(deck.deal())
        column += 1
        if column % 8 == 0:
            column = 0
    def __init__(self, tableau = tableau, foundation = foundation, cells = cells):
        """Create a game of FreeCell"""
        self.tableau = tableau
        self.foundation = foundation
        self.cells = cells
    def print_game(self):
        """Print a game of FreeCell"""
        print()
        print("Cells:                           Foundation:")
        #cell and foundation
        for i in range(4):
            print(f"{i + 1:>8}", end='')
        print('    ', end='')
        for i in range(4):
            print(f"{i + 1:>8}", end='')
        print()
        for _ in self.cells:
            try:
                print("%8s" % (_[0]), end='')
            except IndexError:
                print("%8s" % (''), end='')

        print('    ', end='')
        for stack in self.foundation:
            try:
                print("%8s" % (stack[-1]), end='')
            except IndexError:
                print("%8s" % (''), end='')

        print()
        print('------------------------------------------------------------------------')
        print("  Tableau")
        for i in range(len(self.tableau)):
            print(f"{i + 1:>8}", end="")
        print()
        print('------------------------------------------------------------------------')
        max_length = max([len(stack) for stack in self.tableau])

        for i in range(max_length):
            print(' ', end='')
            for stack in self.tableau:

                try:
                    print("%8s" % (stack[i]), end='')
                except IndexError:
                    print("%8s" % (''), end='')
            print()
        print('------------------------------------------------------------------------')
    def tableau_to_foundation(self, col_t, col_f):
        """Move a card to the foundation.
        args: col_t (int): the column of the card to be moved
            col_f (int): the column of the foundation in which the card is to be moved.
        
        Returns:
            bool: True if the move was successful, false otherwise.
        """
        tableau = self.tableau[col_t - 1]
        foundation = self.foundation[col_f - 1]
        if tableau == []:
            return False
        if foundation == []:
            return tableau[-1].rank == 1
        return foundation[-1].suit == tableau[-1].suit and foundation[-1].rank < tableau[-1].rank
    def cell_to_foundation(self, col_c, col_f):
        """Move a cell card to the foundation.
        args: col_c (int): the column of the card to be moved from the cell.
            col_f (int): the column of the foundation in which the card is to be moved.
        
        Returns:
            bool: True if the move was successful, false otherwise.
        """
        cell = self.cells[col_c - 1]
        foundation = self.foundation[col_f - 1]
        if cell == []:
            return False
        if foundation == []:
            return cell[-1] == 1
        return foundation[-1].suit == cell[-1].suit and foundation[-1].rank < cell[-1].rank
    def tableau_to_cell(self, col_c):
        """Move a tableau card to the cell pile.
        args:
            col_c (int): the column of the cell in which the card is to be moved.
        
        Returns:
            bool: True if the move was successful, false otherwise.
        """
        cell = self.cells[col_c - 1]
        return cell == []
    def cell_to_tableau(self, col_c, col_t):
        """Move a cell card to the tableau.
        args: col_c (int): the column of the card to be moved from the cell.
            col_t (int): the column of the tableau in which the card is to be moved.
        
        Returns:
            bool: True if the move was successful, false otherwise.
        """
        cell = self.cells[col_c - 1]
        tableau = self.tableau[col_t - 1]
        if cell == []:
            return False
        if tableau == []:
            return True
        cell_card = self.cells[col_c - 1][-1]
        tableau_card = self.tableau[col_t - 1][-1]
        return cell_card.rank < tableau_card.rank and cell.suit != tableau_card.suit
    def tableau_to_tableau(self, col_t1, col_t2):
        """Move a tableau card to the another column in tableau.
        args: col_t1 (int): the column of the card to be moved from the tableau.
            col_t2 (int): the column of the tableau in which the card is to be moved.
        
        Returns:
            bool: True if the move was successful, false otherwise.
        """
        initial = self.tableau[col_t1 - 1]
        final = self.tableau[col_t2 - 1]
        if initial == []:
            return False
        if final == []:
            return True
        initial_card = initial[-1]
        final_card = final[-1]
        return initial_card.rank < final_card.rank and final_card.suit != final_card.suit
    def t2f(self, col_t, col_f):
        """Move a card to the foundation.
        args: col_t (int): the column of the card to be moved
            col_f (int): the column of the foundation in which the card is to be moved.
        """
        if self.tableau_to_foundation(col_t, col_f):
            card = self.tableau[col_t - 1].pop()
            self.foundation[col_f].append(card)
        else:
            print("Invalid move!")
    def t2c(self, col_t, col_c):
        """Move a tableau card to the cell pile.
        args:
            col_t (int): the column of the card to be moved from the tableau.
            col_c (int): the column of the cell in which the card is to be moved.
        """
        if self.tableau_to_cell(col_c):
            card = self.tableau[col_t - 1].pop()
            self.cells[col_c - 1].append(card)
        else:
            print("Invalid move!")
    def t2t(self, col_t1, col_t2):
        """Move a tableau card to the another column in tableau.
        args: col_t1 (int): the column of the card to be moved from the tableau.
            col_t2 (int): the column of the tableau in which the card is to be moved.
        
        """
        if self.tableau_to_tableau(col_t1, col_t2):
            card = self.tableau[col_t1 - 1].pop()
            self.tableau[col_t2 -1].append(card)
        else:
            print("Invalid move!")
    def c2t(self, col_c, col_t):
        """Move a cell card to the tableau.
        args: col_c (int): the column of the card to be moved from the cell.
            col_t (int): the column of the tableau in which the card is to be moved.
        """
        if self.cell_to_tableau(col_c, col_t):
            card = self.cells[col_c - 1].pop()
            self.tableau[col_t -1].append(card)
        else:
            print("Invalid move!")
    def c2f(self, col_c, col_f):
        """Move a cell card to the foundation.
        args: col_c (int): the column of the card to be moved from the cell.
            col_f (int): the column of the foundation in which the card is to be moved.
        """
        if self.cell_to_foundation(col_c, col_f):
            card = self.cells[col_c - 1].pop()
            self.foundation[col_f -1].append(card)
        else:
            print("Invalid move!")
    def help(self):
        """Display the help menu for the player."""        
        print("""\tt2f T  F   -- move from Tableau T to Foundation F
        t2c T  C   -- move from Tableau T to Cell C
        t2t T1 T2  -- move from Tableau T1 to Tableau T2
        c2t C  T   -- move from Cell C to Tableau T
        c2f C  F   -- move from Cell C to Foundation F
        h          -- help (displays the menu of options)
        q          –- quit
        """)
    def win(self):
        """Checks whether the player has won the game.
        This is accomplished by moving all cards from Tableau to the foundation.
        """
        for column in self.foundation:
            if len(column) == 13:
                print("You have won the game!!")
                return True
            return False
    def instructions(self):
        """Display the instructions"""
        print("""\tTo win the game of Freecell, you must move all the cards
            from the Tableau to the foundation in order from Ace to king and they must match their suits.
        Only one card can be moved at a time.
        Once a card is in the foundation it cannot be moved.
        """)
a = FreeCell()

def main():
    """Main function to run the a new game of free cell."""
    game = FreeCell()
    print("Starting a new game of free cell....\n")
    print("Here is the help menu to help you play the game:\n")
    game.help()
    game.instructions()
    
    
    
    
    
if __name__=='__main__':
    main()
    