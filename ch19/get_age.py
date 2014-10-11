

def get_age():
    age = int(input("please enter your age: "))
    if age < 0:
        my_err = ValueError("{0} is not a valid age".format(age))
        raise my_err
    return age


if __name__ == "__main__":
    get_age()
