import time

class Time:

    def __init__(self,hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.check_bound()

    def check_bound(self):

        while( self.second >= 60 ):
            self.second -= 60
            self.minute += 1

        while( self.minute >= 60 ):
            self.minute -= 60
            self.hour += 1

        while( self.hour >= 24 ):
            self.hour -= 24

    def increament(self, second):
        try:
            if second < 0 :
                raise ValueError
            self.second += second
            self.check_bound()
        except ValueError:
            import sys
            line = sys._getframe(1).f_lineno
            print("ValueError detect : The second can't be negative"
                    "in the line: {0}".format(line))

        return self

    def __add__(self, t):

        if isinstance(t, Time):
            self.hour += t.hour
            self.minute += t.minute
            self.second += t.second
            self.check_bound()

        else:
            self.increament(t)

        return Time(self.hour, self.minute, self.second)



    def to_seconds(self):
        return 3600 * self.hour + 60 * self.minute + self.second


    def is_between(self, t1, t2):
        return t1.to_seconds() <= self.to_seconds() < t2.to_seconds()

    def __str__(self):
        return "{0} : {1} : {2}".format(self.hour, self.minute, self.second)

    def __gt__(self, t2):
        return self.to_seconds() > t2.to_seconds()

    def after(self, t2):
        return self > t2




if __name__ == "__main__":
    now = Time(10, 44, 0)
    t1 = Time(10, 20, 5)
    t2 = Time(12, 50, 3)

    print(now)
    print(t1)
    print(t2)

    print( t1 > t2 )
    print( t1.after(now))
    print( t2.after(now))

    print(now.is_between(t1, t2))
    print( t1 + t2 )
    t = t1
    print(t)
    t.increament(3600)
    print(t)
    t = t + 3600
    print(t)

    t.increament(-50)
