class Stack:
    def __init__(self, source):
        self.stack = [source]

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        value = self.stack[-1] # last element
        self.stack = self.stack[:-1]  # remove last element
        return value

    def is_non_empty(self):
        return len(self.stack) != 0