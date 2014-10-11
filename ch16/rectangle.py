from point import *
from test import *


class Rectangle:

    def __init__(self, point, width, height):
        self.start_point = point
        self.width = width
        self.height = height

    def __str__(self):
        return ("{0}, {1}, {2}"
                .format(self.start_point, self.width, self.height))

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        self.start_point.x += dx
        self.start_point.y += dy

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * ( self.width + self.height )

    def flip(self):
        self.width, self.height = self.height, self.width

    def contains(self, point):
        start_x = self.start_point.x
        start_y = self.start_point.y

        if ((start_x <= point.x < start_x + self.width)
                and (start_y <= point.y < start_y + self.height)):
            return True
        return False
    def collision(self, rectangle):
        my_start = self.start_point
        my_width = self.width
        my_height = self.height

        r_start = rectangle.start_point
        r_width = rectangle.width
        r_height = rectangle.height

        if my_start.x == r_start.x and my_start.y == r_start.y:
            return True

        if my_start.x > r_start.x:
            if my_start.y >= r_start.y:
                return rectangle.contains(my_start)
            else:
                return rectangle.contains(Point(my_start.x,
                                                my_start.y + my_height))
        elif my_start.x == r_start.x:
            if my_start.y < r_start.y:
                return self.contains(r_start)
            elif my_start.y > r_start.y:
                return rectangle.contains(my_start)
        else:#my_start.x < r_start.x
            if my_start.y > r_start.y:
                return self.contains(Point(r_start.x,
                                           r_start.y + rectangle.height))
            else:
                return self.contains(r_start)






def test_suit(r):
    test(r.contains(Point(0, 0)))
    test(r.contains(Point(3, 3)))
    test(not r.contains(Point(3, 7)))
    test(not r.contains(Point(3, 5)))
    test(r.contains(Point(3, 4.9999999)))
    test(not r.contains(Point(-3, -3)))


if __name__ == "__main__":
    r = Rectangle(Point(0, 0), 10, 5)
    print(r)
    print(r.area() == 50)
    print(r.perimeter() == 30)
    r.flip()
    print("After flip: ",r)
    test_suit(Rectangle(Point(0, 0), 10, 5))

    print(r.collision(Rectangle(Point(-1,-2), 10, 5)))


