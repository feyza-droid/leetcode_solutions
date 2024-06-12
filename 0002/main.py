#2. Add Two Numbers
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = None
        p3 = None
        rem = 0
        while(True):
            if l1 == None and l2 == None:
                break
            
            if l1 == None:
                val1 = 0
            else:
                val1 = l1.val
                l1 = l1.next
                
            if l2 == None:
                val2 = 0
            else:
                val2 = l2.val
                l2 = l2.next
                
            val3 = val1 + val2 + rem
            rem = int (val3 / 10)
            val3 = int(val3 % 10)
            
            if l3 == None:
                l3 = ListNode(val3) # assign head to new node
                p3 = l3
            else:
                p3.next = ListNode(val3)
                p3 = p3.next
                
        if rem > 0:
            p3.next = ListNode(rem)
            p3 = p3.next
            
        return l3
