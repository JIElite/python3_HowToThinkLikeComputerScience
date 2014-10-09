

def read_file(file_in_name):
    file_in = open(file_in_name, "r")
    lst = []
    lst = file_in.readlines()
    file_in.close()
    return lst


def retrieve_numberline(file_in_name, file_out_name):
    lst = []
    lst = read_file(file_in_name)
    file_out = open(file_out_name, "w")

    for list_elem in lst:
        text = list_elem[5:]
        file_out.write(text)
    file_out.close()

if __name__ == "__main__":
    retrieve_numberline("test_file_addline", "test_without_numline")



