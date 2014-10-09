

def read_file(file_name):
    file_in = open(file_name, "r")
    lst = []
    lst = file_in.readlines()
    file_in.close()
    return lst

def fileter(substr, lst):
    for list_elem in lst:
        if substr in list_elem:
            print(list_elem, end = "")



if __name__ == "__main__":
    lst = read_file("test_file")
    find_word = "import"
    fileter(find_word, lst)
