import time

def read_data(file_name):
    file_in = open(file_name, "r")
    lst = []
    while True:
        text = file_in.readline()
        if text == "":
            break
        else:
            lst.append(text)
    file_in.close()
    return lst



def write_reverse_data(file_name, lst):
    file_out = open(file_name, "w")

    for i in range(len(lst) - 1, -1, -1):
        file_out.write(lst[i])  #include newline char.

    file_out.close()


def show_data(list_name, line):
    for i in range(line):
        print(list_name[i], end = "")


#start_test
start_time = time.clock()


lst = read_data("test_file")
write_reverse_data("test_out", lst)


finish_time = time.clock()
total_time = finish_time - start_time

#linear time Algorithm
print("The Elapsed time : ", total_time)
