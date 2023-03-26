# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bits = []

        current = head
        while current:
            bits.append(current.val)
            current = current.next

        power = 0
        decimal_repr = 0

        for i in range(len(bits)-1, -1, -1):
            decimal_repr += (bits[i] * (2 ** power))
            power += 1

        return decimal_repr
