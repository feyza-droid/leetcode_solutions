# 19. Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_counter = 0
        ptr = head
        while(ptr != None):
            ptr = ptr.next
            total_counter += 1
        
        counter = 0
        temp = head
        prev = None
        
        if(temp != None and counter == (total_counter - n)): # if first node is to be removed
            head = temp.next
            del temp
            return head
        
        while(temp != None and counter != (total_counter - n)):
            prev = temp
            temp = temp.next
            counter += 1

        if temp == None: # if not found
            return head

        prev.next = temp.next # node to be removed is found (between prev and temp) and will be removed
        del temp

        return head
