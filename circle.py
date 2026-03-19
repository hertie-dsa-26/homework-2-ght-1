class circle_class:

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        area = round(3.1416 * (self.radius ** 2), 4)
        return str(area)
    
    def perimeter(self):
        perimeter = round(3.1416 * 2 * self.radius, 4)
        return str(perimeter)