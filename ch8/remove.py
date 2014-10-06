import sys

def test(did_work):
    line = sys._getframe(1).f_lineno
    if did_work:
        msg = "The line {0} pass.".format(line)
    else:
        msg = "The line {0} FAILED.".format(line)

    print (msg)



def test_suit():
    test(remove("an", "banana") == "bana")
    test(remove("cyc", "bicycle") == "bile")
    test(remove("iss", "Mississippi") == "Missippi")
    test(remove("eggs", "bicycle") == "bicycle")





def remove(substr, string):
    if substr in string:
        for i in range(len(string) - len(substr) + 1):
            if string[i:i + len(substr)] == substr:
                new_str = string[0:i] + string[i+len(substr) : ]
                return new_str

    else:
        return string

remove("na","banana")
test_suit()
