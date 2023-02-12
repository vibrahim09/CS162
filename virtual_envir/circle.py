from math import pi
from dataclasses import dataclass, field
from shape import Shape

@dataclass
class Circle(Shape):
    """Model a circular shape. Initialized with dataclasses.
    
    Args:
        x: (float) center of the shape in the cardinal plane. x value.
        y: (float) center of the shape in the cardinal plane. y value.
        radius: (float) radius of the circle. 
    """
    
    x: float
    y: float
    radius: float
    
    tl: tuple = field(init=False, repr=False)
    br: tuple = field(init=False, repr=False)
    
    def __post_init__(self) -> None:
        """Initializes the Rectangles plot points for the top left(tl) and bottom right(br).
        We do this post init to grab the x, y, width and height to use them for calculations.
    
        Returns: None
        """
        self.tl: tuple = (self.x, self.y)
        self.br: tuple = (self.x + self.width, self.y - self.height)
    
    def area(self) -> float:
        """Gives the area of the circle.
        
        Returns:
            Area: (float) the area of the circle.
        """
        
        return round(pi * self.radius ** 2, 2)
    
    def diameter(self) -> float:
        """Returns the diameter of the circle.
            
        returns:
            diameter: (float) diameter of the circle.
        """
        return self.radius * 2
    
    def circumference(self) -> float:
        """Returns the circumference of the circle.
        
        returns:
            circumference: (float) circumference of the circle rounded by 4 significant figures.
        """
        
        return round(2 * pi * self.radius, 2)
    
    def __str__(self) -> str:
        """Returns a string representation of the circle.
            This is meant to be human readable.

        """
        
        return f"This shapes initial coordinate is ({self.x}, {self.y}) with radius: {self.radius}."
    def __repr__(self) -> str:
        """Generate a string representation of the card.
        
        The output of repr() is meant to aid debugging. Is should uniquely
        identify the object and it should be possible to instantiate a new
        object using the returned value.
        
        Returns:
            str: A string from which the card could be instantiated.
        """
        return f"x = {self.x}, y = {self.y}, radius = {self.radius}"
    
    
    
    
    
if __name__ == "__main__":
    # Test lines
    c = Circle(2, 3, 2)
    d = Circle(2, 3, 5)
    print(c)
    print(d)
    print(c == d)
    print(c.diameter())
    print(c.area())
    print(d.diameter())
    
    print(c.circumference())
    
    print(d.circumference())