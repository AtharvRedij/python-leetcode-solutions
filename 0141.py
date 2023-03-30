# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        slow_ptr = head
        fast_ptr = head.next

        while slow_ptr and fast_ptr:
            if slow_ptr == fast_ptr:
                return True
            
            slow_ptr = slow_ptr.next
            if fast_ptr.next is None or fast_ptr.next.next is None:
                break
                
            fast_ptr = fast_ptr.next.next

        return False
