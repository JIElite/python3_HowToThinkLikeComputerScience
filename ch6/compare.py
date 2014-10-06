import sys


def test(did_work):
    linum = sys._getframe(1).f_lineno
    if did_work:
        msg = "The line {0} ok.".format(linum)
    else:
        msg = "The line {0} FAILED.".format(linum)
    print(msg)


def compare(number1, number2):
    if number1 > number2 :
        return 1
    elif number1 == number2 :
        return 0
    else :
        return -1


def test_suit():
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)



def main():
    test_suit()


main()


