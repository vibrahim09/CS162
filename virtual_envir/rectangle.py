from shape import Shape
from dataclasses import dataclass, field

@dataclass
class Rectangle(Shape):
    """Model a Rectangle shape. Initialized with dataclasses.
    
    Args:
        x: (float) top left corner of the shape in the cardinal plane. x value.
        y: (float) top left corner of the shape in the cardinal plane. y value.
        width: (float) width of the rectangle. 
        height: (float) height of the rectangle.
    """
    
    x: float
    y: float
    width: float
    height: float
    tl: tuple = field(init=False, repr=False)
    br: tuple = field(init=False, repr=False)
    
    def __post_init__(self) -> None:
        """Initializes the Rectangles plot points for the top left(tl) and bottom right(br).
        We do this post init to grab the x, y, width and height to use them for calculations.
    
        Returns: None
        """
        self.tl: tuple = (self.x, self.y)
        self.br: tuple = (self.x + self.width, self.y - self.height)

    def perimeter(self) -> float:
        """Returns the perimeter of the rectangle
        by multiplying the heigh and width of the rectangle.
        
        Returns: 
            float: the perimeter of the rectangle
        """
        return float((self.height + self.width) * 2)
    
    def intersection(self, other):
        """Finds if the rectangles intersect in the 2d plane and returns true is an intersection exits
        If the intersection exits, it will return a new rectangle with x, y, width and height attributes.
        
        Args:
            other (Rectangle): an instance of a rectangle.
        
        Returns:
            new_rectangle (Rectangle): an instance of a rectangle
            None: if rectangles don't intersect.
        """
        
        if not isinstance(other, Rectangle):
            print("Other is not a Rectangle")
            return None
        
        # check for min x variable and max x variable to find width and height of intersection.
        # Do the same for y variables to find the height.
        # If area is negative then then intersection does not exist.
        # If positive area, then intersection exists and creates a new rectangle.
        x, y = 0, 1
        width = min(self.br[x], other.br[x]) - max(self.tl[x], other.tl[x])
        height = min(self.tl[y], other.tl[y]) - max(self.br[y], other.br[y])
        if min(width, height) > 0:
            new_shape = Rectangle(0, 0, width, height)
            print(f"New shape created by intersection has width: {width} and height: {height}")
            return new_shape
        else:
            print("Rectangles do not intercept.")
            return None               
    
    def union(self, other):
        """Finds the rectangles union in the 2d plane and returns a new rectangle with width and height of both rectangles.
        
        Args:
            Other (Rectangle): An instance of a rectangle.
        
        Returns:
            Class (rectangle): An instance of a rectangle with union height and width. 
        """
        if not isinstance(other, Rectangle):
            print("Other is not a Rectangle")
            return None
        # Checks for lowest x and y values to define its starting point. this should be the left most point.
        # Using the max width and height of both rectangles, and subtracting the new x and y values
        # it will give us the new width and height of the union without the adding the intersection if there is one.
        x, y = 0, 1
        new_x = min(self.tl[x], other.tl[x])
        new_y = min(self.tl[y], other.tl[y])
        new_width = (max(self.x + self.width, other.x + other.width) -  new_x)
        new_height = (max(self.y + self.height, other.y + other.height) - new_y)
        print(f"New shape created by union has width: {new_width} and height: {new_height}")
        return Rectangle(new_x, new_y, new_width, new_height)
    
    # def __eq__(self, other) -> bool:
    """Used dataclasses built in __eq__ method to compare if both rectangles are of equal x, y, width and height"""
    

if __name__ == "__main__":
    # Testing lines.
    a = Rectangle(1, 5, 3, 5)
    b = Rectangle(3, 7, 4, 4)
    
    print(a.area())
    print(b.area())
    
    a.intersection(b)

    print(a == b)

    c = a.union(b)

    print(c)

    print(b.__repr__())