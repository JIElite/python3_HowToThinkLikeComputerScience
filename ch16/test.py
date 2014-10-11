import sys


def test(did_work):
    linum = sys._getframe(1).f_lineno
    if did_work:
        msg = "line {0} work.".format(linum)
    else:
        msg = "line {0} FAILED.".format(linum)
    print(msg)


