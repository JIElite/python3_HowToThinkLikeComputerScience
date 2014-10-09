

def read_file(file_in_name):
    file_in = open(file_in_name, "r")
    lst = []
    lst = file_in.readlines()
    file_in.close()
    return lst


def add_linenum(file_in_name, file_out_name):
    lst = read_file(file_in_name)
    file_out = open(file_out_name, "w")
    for i,list_elem in enumerate(lst):
        file_out.write("{0:<5}".format(i) + list_elem)
    file_out.close()


if __name__ == "__main__":
    add_linenum("test_file", "test_file_addline")

