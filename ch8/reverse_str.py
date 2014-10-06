import sys

def test(did_work):
    line = sys._getframe(1).f_lineno
    if did_work:
        msg = "The line {0} pass.".format(line)
    else:
        msg = "The line {0} FAILED.".format(line)

    print (msg)


def test_suit():
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")



def reverse(str):
    reverse_str = ""
    for i in range(0, len(str)):
        reverse_str += str[-(i+1)]
    return reverse_str



test_suit()
