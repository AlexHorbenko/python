import math
import numbers

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() > other.get_square()
        return NotImplemented

    def __lt__(self, other):
        return not self > other

    def __ge__(self, other):
        return any((self > other, self == other))

    def __ne__(self, other):
        return not self == other

    def __iadd__(self, other):
        return Rectangle.__add__(self, other)

    def __add__(self, other):
        r3_square = self.get_square() + other.get_square()
        r3_width = self.width
        r3_height = r3_square / r3_width
        return Rectangle(r3_width, r3_height)

    def __mul__(self, n):
        if isinstance(n, numbers.Real):
            r4_square = self.get_square() * n
            r4_width = self.width
            r4_height = r4_square / r4_width
            return Rectangle(r4_width, r4_height)
        return NotImplemented

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print(type(r3.__dict__['width']))
print(type(r3.__dict__['height']))