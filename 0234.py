# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        current = head
        
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        size = 0

        current = head
        while current:
            size += 1
            current = current.next

        if size == 1:
            return True

        middle = (size // 2) + 1
        if size % 2 == 1:
            middle += 1


        prev = None
        current = head
        index = 0
        while current:
            index += 1
            if index == middle:
                prev.next = None
                new_head = self.reverse(current)
                break
            else:
                prev = current
                current = current.next

        while head and new_head:
            if head.val != new_head.val:
                return False

            head = head.next
            new_head = new_head.next

        return True
