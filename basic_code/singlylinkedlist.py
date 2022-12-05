class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, data):
        node = Node(data)

        if not self.head: # first time adding a node to singly linked list
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def delete_node(self, data):
        node = self.head

        # deleting first element and changing the head
        if node.data == data:
            temp = node
            self.head = node.next

            if not self.head: # last node deleted, tail changed (linked list had only 1 node so head and tail will become None)
                self.tail = None
            del temp
            return

        while(node.next):
            if node.next.data == data:
                temp = node.next
                node.next = node.next.next

                if not node.next: # last node deleted, tail changed
                    self.tail = node
                del temp
                return
            node = node.next

    def print(self):
        node = self.head
        if not node:
            print("LinkedList is empty\n")
        else:
            print("head", end="->")
            while(node):
                print(node.data, end="->")
                node = node.next
            print("None", end="\n")

linkedlist = LinkedList()
linkedlist.insert_node(8)
linkedlist.insert_node(3)
linkedlist.insert_node(7)
linkedlist.print()
linkedlist.delete_node(8)
linkedlist.print()
linkedlist.delete_node(3)
linkedlist.print()
linkedlist.delete_node(7)
linkedlist.print()