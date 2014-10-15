
class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return ( self.items == [] )


def eval_posfix(expr):
    import re
    token_list = re.split("([^0-9])", expr)
    stack = Stack()
    for token in token_list:
        if token == "" or token == " ":
            continue
        if token == "+":
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == "*":
            product = stack.pop() * stack.pop()
            stack.push(product)
        elif token == "/":
            down = stack.pop()
            up = stack.pop()
            try:
                divide = up / down
                stack.push(divide)
            except ZeroDivisionError:
                print("ZeroDivisionError detected")
                continue
        else:
            stack.push(int(token))
    return stack.pop()


def main():
    print(eval_posfix("56 0 / 51 22 + 34 *"))


if __name__ == "__main__":
    main()

