import sys

def test(did_work):
    line = sys._getframe(1).f_lineno
    if did_work:
        msg = "The line {0} pass.".format(line)
    else:
        msg = "The line {0} FAILED.".format(line)

    print (msg)



def swap(x, y):
    (x, y) = (y, x)
    return x, y


a = ["This", "is", "fun"]
b = [2,3,4]

print("before swap function call: a:", a, "b:", b)
a, b = swap(a, b)
print("after swap function call: a:", a, "b:", b)
