import math

class Circle:
    PI = 3.14

    def __init__(self, x, y, radius):
        self._x = x
        self._y = y
        self._radius = radius

    def __str__(self):
        area = self.area()
        return f"Circle : (x = {self._x}, y = {self._y}, r = {self._radius}), 면적 : {area:.1f}"

    def get_x(self): return self._x
    def get_y(self): return self._y
    def get_radius(self): return self._radius

    def set_x(self, x): self._x = x
    def set_y(self, y): self._y = y
    def set_radius(self, r): self._radius = r

    def area(self):
        return Circle.PI * self._radius ** 2

    def contains(self, c):
        dist = math.sqrt((self._x - c._x)**2 + (self._y - c._y)**2)
        return dist + c._radius <= self._radius

    def overlaps(self, c):
        dist = math.sqrt((self._x - c._x)**2 + (self._y - c._y)**2)
        return dist < self._radius + c._radius


c1 = Circle(0, 0, 100)
c2 = Circle(0, -10, 10)
c3 = Circle(-100, 0, 120)

print("c1 =", c1)
print("c2 =", c2)
print("c3 =", c3)
print("c1 contains c2 :", c1.contains(c2))
print("c1 contains c3 :", c1.contains(c3))
print("c1 overlaps c2 :", c1.overlaps(c2))
print("c1 overlaps c3 :", c1.overlaps(c3))
