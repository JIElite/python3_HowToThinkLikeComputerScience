import sys

def test(did_work):
    linum = sys._getframe(1).f_lineno
    if did_work:
        msg = "line {0} ok.".format(linum)
    else:
        msg = "line {0} FAILED.".format(linum)
    print(msg)



def f2c(f_degree):
    c_degree  = round ( ( f_degree - 32.0 ) * 5 / 9 )
    return c_degree

def c2f(c_degree):
    f_degree = round(c_degree * 9 / 5 ) + 32
    return f_degree



def test_suit_f2c():
    test(f2c(212) == 100)
    test(f2c(32) == 0)
    test(f2c(-40) == -40)
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)



def test_suit_c2f():
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)

def main():
    test_suit_f2c()
    test_suit_c2f()


main()
