class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""
enqueue(data): add node to the rear
deque(): remove node from the front

front-> node -> node > node -> ... -> rear
"""
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    # O(1)
    def enqueue(self, data):
        node = Node(data)
        if self.rear == None: # first time adding a node
            self.front = node
        else:
            self.rear.next = node
        self.rear = node

    # O(1)
    def deque(self):
        if self.front == None:
            return None

        temp = self.front
        data = self.front.data

        self.front = self.front.next
        if self.front == None: # no node left
            self.rear = None

        del temp
        return data

    # O(1)
    def peek(self):
        if self.front == None:
            return None
        else:
            return self.front.data

    # O(1)
    def isEmpty(self):
        return self.front == None

    # O(n)
    def print(self):
        if self.isEmpty():
            print("Queue is empty\n")
        else:
            node = self.front
            print("front", end="->")
            while(node):
                print(node.data, end="->")
                node = node.next
            print("None", end="\n")

queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
queue.print()
queue.enqueue("D")
queue.print()
print(f"peek {queue.peek()}")
print(f"{queue.deque()} is deleted.")
queue.print()
print(f"{queue.deque()} is deleted.")
queue.print()
queue.enqueue("E")
print(f"peek {queue.peek()}")
print(f"{queue.deque()} is deleted.")
queue.print()
print(f"{queue.deque()} is deleted.")
queue.print()
print(f"{queue.deque()} is deleted.")
queue.print()