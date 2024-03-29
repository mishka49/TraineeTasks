import math

from figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        super().area()
        return math.pi * self.radius**2


if __name__=="__main__":
    figure = Circle(1)
    print(figure.area())