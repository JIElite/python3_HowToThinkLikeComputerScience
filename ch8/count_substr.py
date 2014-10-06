import sys

def test(did_work):
    line = sys._getframe(1).f_lineno
    if did_work:
        msg = "The line {0} pass.".format(line)
    else:
        msg = "The line {0} FAILED.".format(line)

    print (msg)


def test_suit():
    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2 )
    test(count("nana", "banana") == 1 )
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)

def count(substr, string):
    counter = 0
    for i in range(0, len(string)-len(substr) + 1):
        if string[i:i+len(substr)] == substr:
            counter = counter + 1

    return counter




test_suit()
