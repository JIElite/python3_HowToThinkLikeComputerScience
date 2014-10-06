import sys


def test(did_work):
    linum = sys._getframe(1).f_lineno
    if did_work:
        msg = "The line {0} work.".format(linum)

    else:
        msg = "The line {0} FAILED".format(linum)
    print (msg)


def test_suit():
    test(num_digits(0) == 1)
    test(num_digits(-12345) == 5)


def get_positive_digit(num):
    digit = 0
    while num:
        num = num // 10
        digit = digit + 1
    return digit


def num_digits(num):
    if num == 0:
        return 1
    else:
       return get_positive_digit(abs(num))


test_suit()
