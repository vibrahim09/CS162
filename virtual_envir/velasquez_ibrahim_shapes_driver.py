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
    d = Rectangle(1, 5, 7, 5)
    e = Rectangle(2, 4, 2, 2)
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
    
def squares():
    """Construct a few instances of square classes"""
    print("\nSQUARES: ")


def circles():
    """Construct a few instances of circles classes"""
    print("\nCIRCLES: ")
        
    

    
def main():
    rectangles()
    squares()
    circles()

    
    
    
    
if __name__ == '__main__':
    main()
    
    