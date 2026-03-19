from circle import circle_class

for ii in range(1,4):
    test_circle = circle_class(ii)
    try:
        assert test_circle.area() == str(round(3.1416 * (ii ** 2), 4))
        assert test_circle.perimeter() == str(round(3.1416 * 2 * ii, 4))
        print(f'Radius = {ii}: test passed.')
    except AssertionError:
        print(f'Radius = {ii}: test failed.')