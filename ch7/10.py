import math
import sys


sqrt = math.sqrt

def test(did_work):
    linum = sys._getframe(1).f_lineno
    if did_work:
        msg = "The line {0} work.".format(linum)
    else:
        msg = "The line {0} FAILED.".format(linum)

    print(msg)


def test_suit():
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))


def is_prime(num):
    terminate = int(sqrt(num))

    for i in range(2, terminate + 1):
        if num % i == 0:
            return False
    return True

test_suit()
