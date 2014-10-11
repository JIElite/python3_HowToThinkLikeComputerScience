import sys

def test(did_work):
    line = sys._getframe(1).f_lineno
    if did_work:
        msg = "line {0} pass.".format(line)
    else:
        mst = "line {0} FAILED.".format(line)
    print(msg)
