from figures import Figure, Circle, Triangle


def print_figures_area(figure: Figure):
    print(figure.area())


triangle = Triangle(1, 2, 2)
circle = Circle(1)

print_figures_area(triangle)
print_figures_area(circle)
