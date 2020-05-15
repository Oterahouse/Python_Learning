class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")


class Square(Shape):
    def __init__(self, a1, a2, a3, a4):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4

    def calculate_perimeter(self):
        return self.a1 + self.a2 + self.a3 + self.a4

    def change_size(self, change):
        self.a1 = self.a1 + change
        self.a2 = self.a2 + change
        self.a3 = self.a3 + change
        self.a4 = self.a4 + change

class Rectangle(Shape):
    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2

    def calculate_perimeter(self):
        return self.b1 * 2 + self.b2 * 2


r = Rectangle(1, 2)
print(r.calculate_perimeter())
s = Square(3, 4, 5, 6)
print(s.calculate_perimeter())
s.change_size(3)
print(s.calculate_perimeter())
s.change_size(-2)
print(s.calculate_perimeter())

r.what_am_i()
s.what_am_i()