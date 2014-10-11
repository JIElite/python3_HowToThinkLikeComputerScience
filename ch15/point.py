class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{0}, {1}".format(self.x, self.y)

    def get_distance(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return ( dx**2 + dy**2 )**0.5

    def reflect_x(self):
        self.y = - self.y
        return (self.x, self.y)

    def reflect_y(self):
        self.x = - self.x

    def slope_from_origin(self):
        if self.x:
            return self.y / self.x
        else:
            return 0


    def slope_from_point(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        if dx:
            return dy / dx
        return None

    def get_line_to(self, point):
        ''' y = ax + b , get (a, b) tuple'''
        a = self.slope_from_point(point)
        if a:
            b = self.y - a*self.x
            return (a, b)
        return "x = {0}".format(self.x)


if __name__ == "__main__":
    print(Point(4, 10).slope_from_origin())
    print(Point(4, 10).reflect_x())
    print(Point(4, 11).get_line_to(Point(4, 15)))
