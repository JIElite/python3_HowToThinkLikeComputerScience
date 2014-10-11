



def search_key(dic, key):
    try:
        if dic[key]:
            return True
    except KeyError:
        print ("There is no such key name : ", key)
    return False

dic = {}

dic["first"] = 1
dic["second"] = 2
dic["third"] = 3


for key in dic:
    print("Keys is : ", key)


for key in dic.keys():
    print("Another method to print key: ",key)


for value in dic.values():
    print("Dictionary value: ", value,"  ", end = "")
print()


for (k, v) in dic.items():
    print("key : {0}, value: {1}     ".format(k, v), end = "")
print()


print(search_key(dic, "first"))
print(search_key(dic, "name"))




