from shape import Shape
from rectangle import Rectangle
from square import Square
from circle import Circle


def rectangles():
    """Construct a few instances of rectangle classes"""
    print("\n")
    a = Rectangle(1, 5, 7, 5)
    b = Rectangle(2, 7, 4, 3)
    c = Rectangle(6, 8, 4, 3)
    d = Rectangle(1, 5, 7, 5)
    e = Rectangle(2, 4, 2, 2)
    print(a.area())
    print(b.area())
    print()
    print("Interceptions True: ")
    #Should intercept/overlap.
    a.intersection(b)
    b.intersection(a)
    print()
    print("Overlaps:")
    a.overlaps(b)
    b.overlaps(a)
    #Should not intercept/overlap.
    print()
    print("Interceptions False: ")
    a.intersection(c)
    c.intersection(a)
    print()
    print("Unions: ")
    #Union will create a new rectangle regardless of interception.
    a.union(b)
    b.union(a)
    a.union(c)
    print()
    #Uses dataclasses to sinmplify functionality 
    print("Equalities: ")
    print(a == b)
    print(a == d)
    print()
    #Contains a triangle within it self. 
    print("Contains: ")
    a.contains(e)
    a.contains(d)
    



def squares():
    """Construct a few instances of square classes"""
    print("\nSQUARES: ")
    a = Square(1, 5, 7)
    b = Square(2, 7, 4)
    c = Square(6, 8, 4)
    d = Square(1, 5, 7)
    e = Square(2, 4, 2)
    print(a.area())
    print(b.area())
    print()
    print("Interceptions True: ")
    #Should intercept/overlap.
    a.intersection(b)
    b.intersection(a)
    print()
    print("Square Overlaps:")
    a.overlaps(b)
    b.overlaps(a)
    #Should not intercept/overlap.
    print()
    print("Interceptions False: ")
    a.intersection(c)
    c.intersection(a)
    print()
    print("Unions: ")
    #Union will create a new square regardless of interception.
    a.union(b)
    b.union(a)
    a.union(c)
    print()
    #Uses dataclasses to sinmplify functionality 
    print("Equalities: ")
    print(a == b)
    print(a == d)
    print()
    #Contains a square within it self. 
    print("Contains: ")
    a.contains(e)
    a.contains(d)

def circles():
    """Construct a few instances of circles classes"""
    print("\nSQUARES: ")
    a = Square(1, 5, 7)
    b = Square(2, 7, 4)
    c = Square(6, 8, 4)
    d = Square(1, 5, 7)
    e = Square(2, 4, 2)

    
def main():
    rectangles()
    squares()
    circles()

    
    
    
    
if __name__ == '__main__':
    main()
    
    