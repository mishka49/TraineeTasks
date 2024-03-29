import math

from figure import Figure


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        super().area()
        p = self.__half_perimetr()
        return math.sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3))

    def __half_perimetr(self):
        return (self.side1 + self.side2 + self.side3) / 2


