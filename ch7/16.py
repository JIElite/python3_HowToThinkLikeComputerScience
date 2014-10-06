import sys


def test(did_work):
    linum = sys._getframe(1).f_lineno
    if did_work:
        msg = "line {0} work.".format(linum)
    else:
        msg = "line {0} FAILED.".format(linum)
    print (msg)


def test_suit():
    test(sum_of_square( [ 2, 3, 4] ) == 29)
    test(sum_of_square( [ ] ) == 0)
    test(sum_of_square( [ 2, -3, 4] ) == 29)


def sum_of_square(lst):
    total = 0
    for i in lst:
        total = total + i**2
    return total


test_suit()
