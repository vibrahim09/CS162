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



if __name__ == '__main__':
    # Testing lines.
    # a= Square(1,5,3)
    # b = Square(3,3,5)
    
    # print(a.area())
    # print(b.area())
    # print(a)
    # print(b)
    
    # a.intersection(b)
    
    # c = a.union(b)
    
    # print(c)
    
    # print(a == b)
    pass