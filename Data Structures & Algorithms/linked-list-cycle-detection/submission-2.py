# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False

        
        curr = head
        nxt = curr.next

        while nxt and nxt.next:
            if curr == nxt:
                return True
            curr = curr.next
            nxt = nxt.next.next

        
        return False
        