# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        tail = ListNode()
        tail.next = head

        if not head or not head.next:
            return

        # first we get to the half point:
        slowp = head
        fastp = head.next

        while fastp and fastp.next:
            slowp = slowp.next
            fastp = fastp.next.next
        
        #now slowp is at the half point, we want to reverse the second half so we reverse linked list on the second half

        prev = None
        curr = slowp.next
        #this is gonna be the new end of our linkedlist
        slowp.next = None

        #reverse linked list:
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        l1 = head
        l2 = prev

        #now we simply combine both:
        while l1 and l2:
            tail.next = l1
            l1 = l1.next
            tail = tail.next
            tail.next = l2
            
            tail = tail.next
            l2 = l2.next
        
        if not l1:
            tail.next = l2
        elif not l2:
            tail.next = l1


