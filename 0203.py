# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        while head and head.val == val:
            prev = head
            head = head.next

        current = head
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
                
            current = current.next

        return head
