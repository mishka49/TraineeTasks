from figures import Triangle


def test_triangle_area():
    triangle1 = Triangle(1, 2, 2)
    triangle2 = Triangle(2, 2, 2)
    triangle3 = Triangle(5, 10, 6)

    assert 0.97 == round(triangle1.area(), 2)
    assert 1.73 == round(triangle2.area(), 2)
    assert 11.40 == round(triangle3.area(), 2)


def test_is_right_triangle():
    triangle1 = Triangle(6, 8, 10)
    triangle2 = Triangle(9, 12, 15)
    triangle3 = Triangle(2, 2, 2)

    assert triangle1.is_right_triangle()
    assert triangle2.is_right_triangle()
    assert not triangle3.is_right_triangle()


def test_is_can_be_exist():
    assert not Triangle._Triangle__is_can_be_exist(1, 2, 3)
    assert Triangle._Triangle__is_can_be_exist(2,2,2)
