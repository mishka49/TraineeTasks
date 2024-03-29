import math
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        super().area()
        return math.pi * self.radius ** 2


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        if Triangle.__is_can_be_exist(side1,side2,side3):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3

    def area(self):
        super().area()
        p = self.__half_perimetr()
        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

    @staticmethod
    def __is_can_be_exist(side1, side2, side3):
        return side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2

    def is_right_triangle(self):
        sides = [self.side1, self.side2, self.side3]
        sides.sort(reverse=True)
        return sides[0] ** 2 == sides[1] ** 2 + sides[2] ** 2

    def __half_perimetr(self):
        return (self.side1 + self.side2 + self.side3) / 2
