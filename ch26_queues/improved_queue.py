

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


class ImprovedQueue:

    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        if self.length == 0:
            print("There is no any elements in the queue")
            return False

        head = self.head
        self.head = self.head.next
        self.length -= 1
        return head
