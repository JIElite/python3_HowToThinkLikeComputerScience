string = "The is a new string"

# convert string to list #
str_lst = list(string)
print(str_lst)

# because we can't use built-in function str()
# to convert list to string type
# so we do the following code
# convert lst back to string

new_str = "".join(str_lst)
print(new_str)


# another method for convert list to string:
new_str2 = ""
for i in str_lst:
    new_str2 += str(i)
print(new_str2)


