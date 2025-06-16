class Rectangle:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __str__(self):
        return f"(x = {self._x}, y = {self._y}, w = {self._width}, h = {self._height}), 면적 : {self.area()}"

    def set_x(self, x): self._x = x
    def set_y(self, y): self._y = y
    def set_width(self, width): self._width = width
    def set_height(self, height): self._height = height
    def get_x(self): return self._x
    def get_y(self): return self._y
    def get_width(self): return self._width
    def get_height(self): return self._height
    def area(self): return self._width * self._height

    def contains(self, r):
        return (self._x <= r._x and
                self._y >= r._y and
                self._x + self._width >= r._x + r._width and
                self._y - self._height <= r._y - r._height)

    def overlaps(self, r):
      return (self._x < r.get_x() + r.get_width() or
              self._x + self._width > r.get_x() or
              self._y > r.get_y() - r.get_height() or
              self._y - self._height < r.get_y())
    
    


r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(0, -10, 10, 10)
r3 = Rectangle(-100, 0, 120, 100)

print("r1 =", r1)
print("r2 =", r2)
print("r3 =", r3)

print("r1 contains r2 :", r1.contains(r2))
print("r1 contains r3 :", r1.contains(r3))
print("r1 overlaps r2 :", r1.overlaps(r2))
print("r1 overlaps r3 :", r1.overlaps(r3))
