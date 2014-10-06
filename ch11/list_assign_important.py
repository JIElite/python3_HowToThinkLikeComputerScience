
# bind list [1, 2, 3, 4, 5, 6, 7, 8, 9] to a
a  = list(range(1,10))

# bind list [1, 2, 3, 4, 5, 6, 7, 8, 9] to b
# similar to copy in c-like , actually the same refernce
# modify b won't change the "a list value"
b = a[:]

# make a alias to "a list"
# if c is change , a is changed too .
c = a

