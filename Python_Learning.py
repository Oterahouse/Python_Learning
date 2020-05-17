class Square:
    square_list = []

    def __init__(self, number):
        self.number = number
        self.square_list.append(self.number)

s1 = Square(1)
s2 = Square(2)
s3 = Square(3)

print(Square.square_list)