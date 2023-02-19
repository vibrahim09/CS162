from rectangle import Rectangle
from circle import Circle
from dataclasses import dataclass, field

@dataclass
class Square(Rectangle):
    """Model a Square shape. Initialized with dataclasses and inheriting from Rectangle class.
    
    Args:
        x: (float) top left corner of the shape in the cardinal plane. x value.
        y: (float) top left corner of the shape in the cardinal plane. y value.
        width: (float) width of the Square. 
        height: (float) height of the Square.
    """

    width: float
    height: float = field(init=False)
    tl: tuple = field(init=False, repr=False)
    br: tuple = field(init=False, repr=False)
    
    def __post_init__(self) -> None:
        """Initializes the Squares plot points for the top left(tl) and bottom right(br) and its height.
        We do this post init to grab the x, y, width and height to use them for calculations.
    
        Returns: None
        """
        self.height = self.width
        self.tl: tuple = (self.x, self.y)
        self.br: tuple = (self.x + self.width, self.y - self.height)
        
    def contains(self, other) -> bool:
        """Checks if shape contains another shape within its bounds.
        Args:   
            other (Shape): an Instance of shape (Rectangle, square, or circle)
            
        Returns:    
            bool: True if shape contains another shape within its bounds.
                False if shape is not in bunds of shape
        """
        if isinstance(other, (Rectangle, Square)):
            if self.tl[0] < other.tl[0] and other.tl[1] < self.tl[1]:
                if other.br[0] < self.br[0] and self.br[1] < other.br[1]:
                    print("Shape contains other shape.")
                    return True
                else:
                    print("Shape is not in bounds of shape")
                    return False
            else:
                print("Shape is not in bounds of shape")
                return False
        elif isinstance(other, Circle):
            if other.x + other.radius > self.br[0]:
                print("it is outside of the rectangle")
                return False
            elif other.x - other.radius < self.tl[0]:
                print("it is outside of the rectangle")
                return False
            elif other.y - other.radius < self.br[1]:
                print("it is outside of the rectangle")
                return False
            elif other.y + other.radius > self.tl[1]:
                print("it is outside of the rectangle")
                return False
            else:
                print("it is inside of the rectangle")
                return True 
        
    def __str__(self) -> str:
        """Returns a string representation  of the square.
        This is meant to be human readable.
        
        returns: 
            str: a string representation of the square.
        """

        return f"""This square is initialized at point ({self.x}, {self.y}), with width = {self.width}, height = {self.height},
    area = {self.area()}, and perimeter = {self.perimeter()}"""
    
    def __repr__(self) -> str:
        """Generate a string representation of the shape.
        
        The output of repr() is meant to aid debugging. Is should uniquely
        identify the object and it should be possible to instantiate a new
        object using the returned value.
        
        Returns:
            str: A string from which the shape could be instantiated.
        """
        return f"Square (x = {self.x}, y = {self.y}, width = {self.width}, height = {self.height})"
    
    @classmethod
    def create(cls):
        """Creates a instance of the shape"""
        return Square(0, 0, 1)
    
    # def __eq__(self, other) -> bool:
    """Used dataclasses built in __eq__ method to compare if both shape are of equal x, y, width and height"""