from dataclasses import dataclass



@dataclass
class Shape():
    """Model a circular shape. Initialized with dataclasses."""
    
    x: float
    y: float
    
    def area(self):
        """Calculates the area of the shape.

        Returns:
            float: area of the shape
        """
        return NotImplementedError
    def create():
        """Creates a instance of the shape"""
        raise NotImplementedError
    def contains(self, other) -> bool:
        """Checks if shape contains another shape within its bounds.

        Args:
            other (Shape): an Instance of shape (Rectangle, square, or circle)

        Returns:
            bool: True if shape contains another shape within its bounds.
                False if shape is not in bunds of shape
        """
        return NotImplementedError

    def overlaps(self, other):
        """Checks if shape overlaps another shape
        Args:
            Other (Shape): an Instance of shape
            
        returns:
            bool: True is interception exist, false otherwise
        """
        # Check if rectangle has area of zero.
        # if self.area() == 0.0:
        #     return False
        
        x, y = 0, 1 #For simplicity and readability.
        # Check if rectangle is on left side of other.
        if self.tl[x] > other.br[x] or other.tl[x] > self.br[x]:
            return False
        
        # Check if rectangle is above the other.
        if self.br[y] > other.tl[y] or other.br[y] > self.tl[y]:
            return False
        
        else:
            print("It overlaps!")
            return True
        
    
    def __str__(self) -> str:
        """"""
        return NotImplementedError
    def __repr__(self) -> str: 
        return NotImplementedError


