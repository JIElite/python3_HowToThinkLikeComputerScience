
class Node:

    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return ("The value of Node is : {0}".format(self.value))


#This is self-define linked list
#it's done by lst , maybe it's not good
class Linked_list:

    def __init__(self):
        self.lst = []

    def add_node(self, node):
        self.rear_pos = len(self.lst) - 1
        self.lst.append(node)
        self.lst[self.rear_pos].next = node
        return self

    def pop(self):
        self.lst.pop()
        last_index = len(self.lst) - 1
        self.lst[last_index].next = None

    def print_self(self):
        for node in self.lst:
            print(node.value, end = " ")
        print()



def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    linked_list = Linked_list()
    linked_list.add_node(n1).add_node(n2).add_node(n3)
    print(n1.next.next)
    print(n1.next.next.next)
    linked_list.print_self()
    linked_list.pop()
    linked_list.print_self()



if __name__ == "__main__":
    main()
