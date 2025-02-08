class Stack():
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self, size):
        return len(self.items) == size

    def push(self, value):
        if self.is_full(self.size):
            print("Stack is full.")
        else:
            print(f"{value} is pushed at the bottom of the items list.")
            self.items.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Nothing to pop from items.")
        else:
            print(f"Element {self.items[-1]} would be removed.")
            self.items.remove(self.items[-1])

    def peek(self):
        return self.items[-1]


def main():
    stack = Stack(5)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    stack.push(6)
    print("Current items in the stack: " + str(stack.items))

    stack.pop()
    print("Current items in the stack: " + str(stack.items))

    stack.pop()
    print("Current items in the stack: " + str(stack.items))


if __name__ == "__main__":
    main()