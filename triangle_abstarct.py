import math
from abc import abstractmethod

class GeometryFigure:
    def __init__(self, sides):
        self.sides = sides

    def check_figure(self):
        if isinstance(self, EquilateralTriangle):
            return 'Triangle is Equilateral.'
        elif isinstance(self, IsoscelesTriangle):
            return 'Triangle is Isosceles.'
        elif isinstance(self, RectangularTriangle):
            return 'Triangle is Rectangular'
        elif isinstance(self, IsoscelesTriangle):
            return 'Triangle is Isosceles'
        else:
            return "Can't find type of figure"


class Triangle(GeometryFigure):
    def __init__(self, a, b, c, h, p):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        self.p = p

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.p = self.get_p_2()
        self.h = self.get_h()

    @abstractmethod
    def triangle_type(self):
        print()

    def square_rectangular(self):
        return 0.5 * (self.a * self.b)

    def get_p_2(self):
        return (self.a + self.b + self.c) / 2

    def get_p(self):
        p = self.a + self.b + self.c
        return p

    def get_h(self):
        h = 2 * math.sqrt(
            2 * (self.get_p_2() - self.a) * (self.get_p_2() - self.b) * (self.get_p_2() - self.c)) / self.a
        return h

    def square_h(self):
        return 0.5 * self.a * self.h


class RectangularTriangle(Triangle):
    def __init__(self, a, b, c):
        a = a.getsize();
        self.b = b
        self.c = c


class IsoscelesTriangle(Triangle):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class EquilateralTriangle(Triangle):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class Quadrilateral(GeometryFigure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

print(IsoscelesTriangle(3, 5, 7).check_figure())
# tr = Triangle(3, 5, 7)
# print(tr.square_rectangular())
