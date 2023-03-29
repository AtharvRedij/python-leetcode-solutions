# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def add_to_ll(self, head, tail, new_node):
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

        return head, tail

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        last_node = None
        first_ll_current = list1
        second_ll_current = list2

        while first_ll_current and second_ll_current:
            if first_ll_current.val < second_ll_current.val:
                new_node = ListNode(first_ll_current.val)
                first_ll_current = first_ll_current.next

            else:
                new_node = ListNode(second_ll_current.val)
                second_ll_current = second_ll_current.next

            new_head, last_node = self.add_to_ll(new_head, last_node, new_node)

        while first_ll_current:
            new_node = ListNode(first_ll_current.val)
            first_ll_current = first_ll_current.next
            new_head, last_node = self.add_to_ll(new_head, last_node, new_node)

        while second_ll_current:
            new_node = ListNode(second_ll_current.val)
            second_ll_current = second_ll_current.next
            new_head, last_node = self.add_to_ll(new_head, last_node, new_node)

        return new_head
