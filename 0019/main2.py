# 19. Remove Nth Node From End of List
# Single pass solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        while(n > 0):
            fast = fast.next
            n -= 1

        # first node will be removed and head will change
        if fast == None:
            temp = head
            head = head.next
            del temp
            return head
        
        # move until fast reaches the end
        while(fast.next != None):
            slow = slow.next
            fast = fast.next

        if slow.next != None:
            temp = slow.next
            slow.next = slow.next.next
            del temp

        return head