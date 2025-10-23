# polymorphism_demo.py
import math


class Shape:
    def area(self):
        """Base method to be overridden by subclasses"""
        raise NotImplementedError("Subclasses must implement area() method")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize rectangle with length and width"""
        self.length = length
        self.width = width

    def area(self):
        """Override area method for rectangle"""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize circle with radius"""
        self.radius = radius

    def area(self):
        """Override area method for circle"""
        return math.pi * self.radius ** 2