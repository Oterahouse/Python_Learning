class Rectangle:
    def __init__(self, a1, a2, a3, a4):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4

    def calculate_perimeter(self):
        return self.a1 + self.a2 + self.a3 + self.a4


class Square:
    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2

    def calculate_perimeter(self):
        return self.b1 * 2 + self.b2 * 2

r = Rectangle(1, 2, 3, 4)
print(r.calculate_perimeter())
s = Square(1, 2)
print(s.calculate_perimeter())