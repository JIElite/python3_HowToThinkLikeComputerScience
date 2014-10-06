import sys

def test(did_work):
    line = sys._getframe(1).f_lineno
    if did_work:
        msg = "the line {0} pass.".format(line)
    else:
        msg = "the line {0} failed.".format(line)

    print (msg)


def test_suit():
    test(remove_all("an", "banana") == "ba")
    test(remove_all("cyc", "bicycle") == "bile")
    test(remove_all("iss", "Mississippi") == "Mippi")
    test(remove_all("eggs", "bicycle") == "bicycle")


def test_suit2():
    test(remove_all_2("an", "banana") == "ba")
    test(remove_all_2("cyc", "bicycle") == "bile")
    test(remove_all_2("iss", "Mississippi") == "Mippi")
    test(remove_all_2("eggs", "bicycle") == "bicycle")



def test_suit3 ():
    test(remove_all_3("an", "banana") == "ba")
    test(remove_all_3("cyc", "bicycle") == "bile")
    test(remove_all_3("iss", "Mississippi") == "Mippi")
    test(remove_all_3("eggs", "bicycle") == "bicycle")



def remove_all(substr, string):

    while(substr in string):
        for i in range(len(string) - len(substr) + 1):
            if (string[i:i+len(substr)] == substr):
                string = string[0:i] + string[i+len(substr):]

    return string



def remove_all_2(substr, string):
    return string.replace(substr,"")


def remove_all_3(substr, string):
    lst = string.split(substr)
    new_str = ""
    for i in lst:
        new_str += str(i)
    return new_str


test_suit()
print()
test_suit2()
print()
test_suit3()
