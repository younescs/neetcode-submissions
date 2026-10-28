# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        # if not head or not head.next:
        #     return head
        slowp = head
        fastp = head

        for _ in range(n):
            fastp = fastp.next
        
        #[1,2,3,4,5,6]
        #n=2

        #nxt: 6
        #prev:4
        #slowp: 5
        #fastp: None
        prev = None
        nxt = None
        while fastp:
            prev = slowp
            slowp = slowp.next
            nxt = slowp.next
            fastp = fastp.next
        
        if slowp == head:
            dummy.next = slowp.next
        slowp.next = None
        if prev:
            prev.next = nxt

        return dummy.next

