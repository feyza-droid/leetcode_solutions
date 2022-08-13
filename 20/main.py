# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        p_dict = {}
        p_dict[')'] = '('
        p_dict[']'] = '['
        p_dict['}'] = '{'
        
        open_c = p_dict.values()
        
        for c in s:
            if c in open_c:
                stack.push(c)
            else:
                if stack.get_size() == 0:
                    return False
                
                top_c = stack.pop()
                if top_c != p_dict[c]:
                    return False
                
        if stack.get_size() != 0: # some of the openings have not been closed
            return False
        
        return True
    
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
        
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
        
    def pop(self):
        if self.get_size() == 0:
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        value = remove.value
        del remove
        
        self.head.next = self.head.next.next
        self.size -= 1
        return value
    
    def get_size(self):
        return self.size
