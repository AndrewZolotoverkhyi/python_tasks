import math


class Polygon:
    def __init__(self, nbrsides):
        self.nbr_sides = nbrsides

    def whatType(self):
        if self.nbr_sides == 3:
            return "Triangle"
        elif self.nbr_sides == 4:
            return "Rectangle"
        else:
            return "Polygon"

    def howmanySides(self):
        return self.nbr_sides

    def area(self):
        return "No Area"

    def perimeter(self):
        return "No Perimeter"


class Triangle(Polygon):
    def __init__(self, a, b, c):
        Polygon.__init__(self, 3)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * ((s - self.a) * (s - self.b) * (s - self.c)))
        return area

    def perimeter(self):
        return self.a + self.b + self.c


class Rectangle(Polygon):
    def __init__(self, breadth, length):
        Polygon.__init__(self, 4)
        self.breadth = breadth
        self.length = length

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Trapezoid(Polygon):
    def __init__(self, a, b, c, d, h):
        Polygon.__init__(self, 3)
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h

    def area(self):
        h = (math.sqrt(self.c**2- (self.a - self.b)**2 + self.c**2 - self.d**2))/(2-(self.a-self.b))
        area = ((self.a+self.b)/2)*h
        return area

    def perimeter(self):
        return 2 * (self.length + self.breadth)


def main():
    tri1 = Triangle(2, 2, 2)
    rect = Rectangle(2, 3)
    tri2 = Triangle(3, 3, 3)
    figures = [tri1, rect, tri2]
    for fig in figures:
        print("Type of Polygon =>", fig.whatType())
        print("Sides =", fig.howmanySides())
        print("Area =", fig.area())
        print("Perimeter =", fig.perimeter())
