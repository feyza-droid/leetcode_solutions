class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    # O(1)
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.size += 1
    
    # O(1)
    def pop(self):
        if self.isEmpty(): 
            print("No data in the stack to pop()!") 
            return None
        
        temp = self.top
        data = self.top.data
        self.top = self.top.next
        del temp
        self.size -= 1
        return data

    # O(1)
    def peek(self):
        if self.top == None:
            return None
        else:
            return self.top.data

    # O(1)
    def isEmpty(self):
        return self.size == 0

    # O(1)
    def getSize(self):
        return self.size

    # O(n)
    def print(self):
        if self.isEmpty():
            print("Stack is empty\n")
        else:
            node = self.top
            print("top", end="->")
            while(node):
                print(node.data, end="->")
                node = node.next
            print("None", end="\n")


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(f"size {stack.size}")
stack.print()
print(f"{stack.pop()} is popped from the stack!")
stack.print()
print(f"{stack.pop()} is popped from the stack!")
stack.print()
stack.push(5)
stack.print()
print(f"{stack.pop()} is popped from the stack!")
stack.print()
print(f"{stack.pop()} is popped from the stack!")
stack.print()
print(f"{stack.pop()} is popped from the stack!")
stack.print()
print(f"{stack.pop()} is popped from the stack!")
stack.print()
stack.push(6)
stack.print()
print(f"peek {stack.peek()}")
stack.print()