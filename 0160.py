# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_addresses = set()

        first_ptr = headA
        while first_ptr:
            node_addresses.add(first_ptr)
            first_ptr = first_ptr.next
            
        second_ptr = headB
        while second_ptr:
            if second_ptr in node_addresses:
                return second_ptr

            second_ptr = second_ptr.next

        return None
