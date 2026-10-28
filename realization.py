"""Realization: A class implements an abstract interface."""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

if __name__ == '__main__':
    rectangle = Rectangle(5, 3)
    print(f'Rectangle area: {rectangle.area()}')
