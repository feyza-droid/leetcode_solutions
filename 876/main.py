# 876. Middle of the Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        counter = 0
        
        while(ptr != None):
            ptr = ptr.next
            counter += 1
            
        mid = int(counter / 2)
        i = 0
        new_ptr = head
        
        while(i != mid):
            new_ptr = new_ptr.next
            i += 1
        
        return new_ptr
