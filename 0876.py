# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0

        current = head
        while current:
            size += 1
            current = current.next

        middle_index = math.ceil(size / 2)
        if size % 2 == 0:
            middle_index += 1

        current = head
        for i in range(middle_index-1):
            current = current.next

        return current
