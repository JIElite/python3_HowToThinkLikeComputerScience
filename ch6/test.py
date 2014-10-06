import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED".format(linenum)
    print(msg)


def absolute_val(value):
    if value < 0:
        return -value
    return value


test(absolute_val(-5) == 5)

