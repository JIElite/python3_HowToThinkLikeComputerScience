

def recursion_depth(number):
    print("recursion_depth is ",number)
    try:
        recursion_depth(number + 1)
    except:
        print("I can't go any deeper into this wormhole. ",number)


if __name__ == "__main__":
    recursion_depth(0)
