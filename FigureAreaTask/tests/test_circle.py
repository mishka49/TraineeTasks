import math
from figures import Circle


def test_calculate_area():
    circle1 = Circle(1)
    circle2 = Circle(2)
    circle10 = Circle(10)

    assert math.pi == circle1.area()
    assert 12.57 == round(circle2.area(), 2)
    assert 314.16 == round(circle10.area(), 2)
