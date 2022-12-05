class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, data):
        node = Node(data)

        if not self.head:  # first time adding a node to doubly linked list
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node

    def delete_node(self, data):
        node = self.head

        # deleting first element and changing the head
        if node.data == data:
            temp = node
            self.head = node.next
            
            if not self.head: # last node deleted, tail changed (linked list had only 1 node so head and tail will become None)
                self.tail = None
            else: # when there are more nodes after head and the head is deleted set new head's prev to None
                self.head.prev = None
            del temp
            return

        while(node.next):
            if node.next.data == data:
                temp = node.next
                node.next = node.next.next
                
                if not node.next: # last node deleted, tail changed
                    self.tail = node
                else: # deleted one is not last node, so change the next's prev, if we would try to set the node.next.prev when the last node is deleted, it would give exception since node.next is None 
                    node.next.prev = node
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
