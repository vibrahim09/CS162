import math
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
    
    radius: float
    
    def contains(self, other):
        """Check if a circle is inside another circle.
        
        Args:
            other: (Circle): Instance of Circle
            
        Returns:
            True if the circle is inside the other circle. False otherwise.
        """
        d = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        if d <= self.radius - other.radius:
            print("Shape contains other shape.")
            return True
        elif d <= other.radius - self.radius:
            print("Shape contains other shape.")
            return True
        else:
            print("Shapes do not contain each other.")
        
    def overlaps(self, other):
        """ Checks if circle overlaps with other circle."""
        d = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        if d <= self.radius + other.radius:
            print("Shapes overlap!")
            return True
        else:
            print("Shapes do not overlap!")
        

    def area(self) -> float:
        """Gives the area of the circle.
        
        Returns:
            Area: (float) the area of the circle.
        """
        
        return round(math.pi * self.radius ** 2, 2)
    
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
        
        return round(2 * math.pi * self.radius, 2)
    
    def __str__(self) -> str:
        """Returns a string representation of the circle.
            This is meant to be human readable.

        returns: 
            str: a string representation of the circle.
        """
        
        return f"""This circle is initialized at point ({self.x}, {self.y}), with radius = {self.radius},
    area = {self.area()}, and circumference = {self.circumference()}"""
    def __repr__(self) -> str:
        """Generate a string representation of the shape.
        
        The output of repr() is meant to aid debugging. Is should uniquely
        identify the object and it should be possible to instantiate a new
        object using the returned value.
        
        Returns:
            str: A string from which the shape could be instantiated.
        """
        return f"Circle (x = {self.x}, y = {self.y}, radius = {self.radius})"
    
    @classmethod
    def create(cls):
        """Creates a instance of the shape"""
        return Circle(0,0,1)
    
    # def __eq__(self, other) -> bool:
    """Used dataclasses built in __eq__ method to compare if both shape are of equal x, y, width and height"""