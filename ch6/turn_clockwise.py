import sys

def test(did_work):
    linum = sys._getframe(1).f_lineno
    if did_work:
        msg = "Test at line {0} ok.".format(linum)
    else:
        msg = "Test at line {0} FAILED".format(linum)
    print(msg)


def turn_clockwise(director):
    if director == "N":
        return "E"
    elif director == "E":
        return "S"
    elif director == "S":
        return "W"
    elif director == "W":
        return "N"



def test_suit():
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)

test_suit()
