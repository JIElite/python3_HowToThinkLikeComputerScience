

def str_cmp(str1, str2):
    if str1 < str2:
        print(str1, " is smaller than ", str2)
    elif str1 > str2:
        print(str1, " is bigger than ", str2)
    else:
        print("two string is equal")


str_cmp("hello", "hello")
str_cmp("hello", "Hello")
str_cmp("string", "hello")

