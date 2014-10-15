
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __mul__(self, other):
        if type(other) == type(3):
            return Point(self.x * other, self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return Point(self.x * other, self.y * other)


    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


    def __str__(self):
        return "{0}, {1}".format(self.x, self.y)




if __name__ == "__main__":
    p1 = Point(3, 4)
    p2 = Point(5, 5)
    print(p1 * 3)
    print(3 * p1)







