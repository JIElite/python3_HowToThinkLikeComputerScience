import sys


def test(did_work):
    line = sys._getframe(1).f_lineno
    if did_work:
        msg = "line {0} pass.".format(line)
    else:
        msg = "line {0} FAILED.".format(line)
    print(msg)



def test_suit(inventory):
    add_fruit(inventory, "strawberry", 10)
    test("strawberry" in inventory)
    test(inventory["strawberry"] == 10)
    add_fruit(inventory, "strawberry", 25)
    test(inventory["strawberry"] == 35)



def add_fruit(inventory, fruit, quantity = 0):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity
    return inventory


new_inventory = {}
test_suit(new_inventory)
