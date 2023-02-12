from dataclasses import dataclass



@dataclass
class Shape():
    
    def area(self):
        """Calculates the area of the shape.

        Returns:
            float: area of the shape
        """
        return (self.height * self.width)
    def create():
        pass
    def contains(self, other) -> bool:
        """Checks if shape contains another shape within its bounds.

        Args:
            other (Shape): an Instance of shape (Rectangle, square, or circle)

        Returns:
            bool: True if shape contains another shape within its bounds.
                False if shape is not in bunds of shape
        """
        if self.tl[0] < other.tl[0] and self.tl[1] < other.tl[1]:
            if other.br[0] < self.br[0] and other.br[1] < self.br[1]:
                print("Shape contains other shape.")
                return True
            else:
                print("Shape is not in bounds of shape")
                return False
        else:
            print("Shape is not in bounds of shape")
            return False
        
    def overlaps(self, other):
        """Checks if shape overlaps another shape
        Args:
            Other (Shape): an Instance of shape
            
        returns:
            bool: True is interception exist, flase otherwise
        """
        # Check if rectangle has area of zero.
        if self.area() == 0.0:
            return False
        x, y = 0, 1 #For simplicity and redability.
        # Check if rectangel is on left side of other.
        if self.tl[x] > other.br[y] or other.tl[x] < self.br[x]:
            return False
        
        # Check if rectangle is above the other.
        if self.br[1] > other.tl[1] or other.br[1] > self.tl[1]:
            return False
        
        else:
            print("It overlaps!")
            return True
        
    
    def __str__(self) -> str:
        return f"This Shapes initial coordinate is ({self.x},{self.y}) with width: {self.width}, and height: {self.height}"
    def __repr__(self) -> str:
        return f"x = {self.x}, y = {self.y}, width = {self.width}, height = {self.height}"


