import sys

def test(did_work_func):
    linum = sys._getframe(1).f_lineno
    if did_work_func:
        msg = "The line {0} is work.".format(linum)
    else:
        msg = "The line {0} FAILED.".format(linum)
    print (msg)








