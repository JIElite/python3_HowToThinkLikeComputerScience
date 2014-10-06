
list = [1, 2, 3, 4, 5]

tuple = (1, 2, 3, 4, 5)


def change_list(lst):
    for (i,val) in enumerate(lst):
        lst[i] = val ** 2


def pass_tuple(tup):
    for (i, val) in enumerate(tup):
        print ( "The index : {0} , value is : {1}".format(i, val))
    print()
        #tup[i] = val ** 2



#this function still change the origin list
def test_change(lst):
    new_list = []
    new_list = list
    for (i, val) in enumerate(new_list):
        new_list[i] = val ** 3
    return new_list


def not_change(lst):
    new_list = []
    for i in lst:
        new_list.append(i)
    return new_list

#pass_tuple(tuple)  #raise type error didn't support item assign.
#change_list(list)
#test_change(list)

not_change(list)
print(list)

