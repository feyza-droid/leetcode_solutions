# 234. Palindrome Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        node = ListNode(val, next=None)
        node.next = self.top
        self.top = node

    def pop(self):
        temp = self.top
        val = self.top.val
        self.top = self.top.next
        del temp
        return val

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = Stack()
        
        count = 0
        node = head
        while(node):
            count += 1
            node = node.next
        
        length = count
        half = int(length/2)

        count = 0
        node = head
        while(node):
            if count < half:
                stack.push(node.val)   
            elif count == half:
                if length % 2 == 0:
                    val = stack.pop()
                    if val != node.val:
                        return False    
            else:
                val = stack.pop()
                if val != node.val:
                    return False
            count += 1
            node = node.next

        return True