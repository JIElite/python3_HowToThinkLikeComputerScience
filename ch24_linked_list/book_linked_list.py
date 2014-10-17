class Node:

    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


     def print_backward():
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.value, end = " ")


class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None

    def print_backward(self):
        print("[", end = " ")
        if self.head is not None:
            self.head.print_backward()

    #use as a private method
    def add_first(self, value):
        node = Node(value)
        node.next = None
        self.head = node
        self.length += 1

    def add_node(self, value):
        node = self.head
        if node is None:
            self.add_first(value)
        #when the head is not None
        while node.next is not None:
            node = node.next
        new_node = Node(value)
        new_node.next = None
        node.next = new_node
        self.length += 1


def print_list(start_node):
    node = start_node
    while node is not None:
        print(node, end = " ")
        node = node.next
    print()

def print_backward(lst):
    if lst is None:
        return
    head = lst
    tail = lst.next
    print_backward(tail)
    print(head, end = " ")

def add_node(start_node, node):
    traverse_node = start_node
    while traverse_node.next is not None:
        traverse_node = traverse_node.next
    traverse_node.next = node


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    add_node(n1, n2)
    print_list(n1)
    print_backward(n1)

