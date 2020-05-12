class Hexagon:
    def __init__(self, p):
        self.perimeter = p

    def calcurete_perimeter(self):
        return self.perimeter * 6


hex = Hexagon(3)
print(hex.calcurete_perimeter())