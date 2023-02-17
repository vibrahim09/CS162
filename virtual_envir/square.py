from rectangle import Rectangle
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
    
    x: float
    y: float
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
        
    def __str__(self) -> str:
        """Returns a string representation  of the square.
        This is meant to be human readable.
        
        returns: 
            str: a string representation of the square.
        """

        return f"This square is initialized at point ({self.x}, {self.y}), with width {self.width}, and height {self.height}."
    
    def __repr__(self) -> str:
        """Generate a string representation of the shape.
        
        The output of repr() is meant to aid debugging. Is should uniquely
        identify the object and it should be possible to instantiate a new
        object using the returned value.
        
        Returns:
            str: A string from which the shape could be instantiated.
        """
        return f"Square (x = {self.x}, y = {self.y}, width = {self.width}, height = {self.height})"
    
    # def __eq__(self, other) -> bool:
    """Used dataclasses built in __eq__ method to compare if both shape are of equal x, y, width and height"""