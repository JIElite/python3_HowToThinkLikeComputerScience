import sys

def test(did_work):
    line = sys._getframe(1).f_lineno
    if did_work:
        msg = "The line {0} pass.".format(line)
    else:
        msg = "The line {0} FAILED.".format(line)

    print (msg)


def test_suit():
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome(""))

def reverse(str):
    reverse_str = ""
    for i in range(0, len(str)):
        reverse_str += str[-(i+1)]
    return reverse_str



def is_palindrome(str):
    if (reverse(str) == str):
        return True
    return False


test_suit()
