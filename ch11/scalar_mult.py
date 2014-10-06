import sys

def test(did_work):
    line = sys._getframe(1).f_lineno
    if did_work:
        msg = "The line {0} pass.".format(line)
    else:
        msg = "The line {0} FAILED.".format(line)

    print (msg)



def test_suit():
    test(scalar_mult(5, [1, 2]) == [5, 10] )
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3] )
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14] )



def scalar_mult(scalar, lst):
    new_lst = []
    for i in lst:
        new_lst.append(scalar * i)
    return new_lst



test_suit()
