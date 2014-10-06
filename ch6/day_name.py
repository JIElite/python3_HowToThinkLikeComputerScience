import sys

def test(did_work):
    linum = sys._getframe(1).f_lineno
    if did_work:
        msg = "The line {0} is ok.".format(linum)
    else:
        msg = "The line {0} FAILED.".format(linum)
    print(msg)


def day_name(day):
    if day == 1:
        return "Monday"
    elif day == 2:
        return "Twesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    elif day == 0:
        return "Sunday"


def test_suit():
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)


test_suit()
