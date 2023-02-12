from dataclasses import dataclass

@dataclass
class Shape():
    
    def area(self):
        return (self.height * self.width)
    def create(cls):
        pass
    def contains(self, other):
        pass
    def overlaps(self, other):
        pass
    def __str__(self) -> str:
        return f"This Shape top left coordinate is ({self.x},{self.y}) with width: {self.width}, and height: {self.height}"
    def __repr__(self) -> str:
        return f"x = {self.x}, y = {self.y}, width = {self.width}, height = {self.height}"
