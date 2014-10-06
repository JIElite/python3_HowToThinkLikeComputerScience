import sys

def test(did_work):
    linum = sys._getframe(1).f_lineno
    if did_work:
        msg = "line {0} work.".format(linum)
    else:
        msg = "line {0} FAILED.".format(linum)
    print (msg)


def test_suit():
    test(num_even_digits(123456) == 3)
    test(num_even_digits(2468) == 4)
    test(num_even_digits(1357) == 0)
    test(num_even_digits(0) == 1)

def num_even_digits(num):
    even_digit = 0
    num_list = list(str(abs(num)))
    for i in num_list:
        if int(i) % 2 == 0:
            even_digit = even_digit + 1
    return even_digit

test_suit()
