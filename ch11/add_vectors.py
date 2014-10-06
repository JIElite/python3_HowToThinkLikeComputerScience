import sys

def test(did_work):
    line = sys._getframe(1).f_lineno
    if did_work:
        msg = "The line {0} pass.".format(line)
    else:
        msg = "The line {0} FAILED.".format(line)

    print (msg)


def test_suit():
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

def add_vectors(lst1, lst2):
    new_list = []

    if len(lst1):
        if len(lst1) == len(lst2):
            for i in range(len(lst1)):
                value = lst1[i] + lst2[i]
                new_list.append(value)
        else:
            raise IndexError

    return new_list


test_suit()
