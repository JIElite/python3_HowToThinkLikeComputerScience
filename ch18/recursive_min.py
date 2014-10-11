from test import *


def recursive_min(lst):
    min = None
    first_time = True

    for i in lst:
        if type(i) == type([]):
            val = recursive_min(i)
        else:
            val = i

        if first_time or val < min:
            min = val
            first_time = False
    return min



def test_suit():
    test(recursive_min([2, 9, [1, 13], 8, 16]) == 1)
    test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
    test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
    test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)




if __name__ == "__main__":
    test_suit()
