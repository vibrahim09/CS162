from shape import Shape
from rectangle import Rectangle
from square import Square
from circle import Circle


def rectangles():
    """Construct a few instances of rectangle classes and check each class method for validity"""
    print("\nRECTANGLES:")
    a = Rectangle(1, 5, 7, 5)
    b = Rectangle(2, 7, 4, 3)
    c = Rectangle(2, 4, 4, 3)
    d = Rectangle(10, 2, 3, 3)
    e = Circle(2, 4, 2)
    f = Circle(5, 3, 1)
    g = Circle(5, 3, 3)
    print("\n")
    print("a:")
    print(a)
    print("\n")
    print("b:")
    print(b)
    print("\n")
    print("Intersection between a and b: ")
    a.intersection(b)
    print("\n")
    print("Union between a and b: ")
    a.union(b)
    print("\n")
    print("Contains a and b: ")
    a.contains(b)
    print("Contains a and c: ")
    a.contains(c)
    print("Contains a and e(Circle): ")
    a.contains(e)
    print("Contains a and f(Circle): ")
    a.contains(f)
    print("\n")
    print("Overlaps between a and b: ")
    a.overlaps(b)
    print("Overlaps between a and d: ")
    a.overlaps(d)
    print("Overlaps between a and g(Circle): ")
    a.overlaps(g)
    
    
def squares():
    """Construct a few instances of square classes"""
    print("\nSQUARES: ")
    a = Square(2, 2, 2)
    print(a)


def circles():
    """Construct a few instances of circles classes"""
    print("\nCIRCLES: ")
    a = Circle(2, 2, 2)
    print("\n")
    print(a)
    

    
def main():
    rectangles()
    squares()
    circles()

    
    
    
    
if __name__ == '__main__':
    main()
    
    