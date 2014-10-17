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


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = node
        self.length += 1

    def remove(self):
        if self.length:
            value = self.head.value
            self.head = self.head.next
            self.length -= 1
            return value
        else:
            print("there is no any node in the queue")

    def is_empty(self):
        return self.length == 0






