# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            left_side_same = self.isSameTree(p.left, q.left)
            right_side_same = self.isSameTree(p.right, q.right)
            return left_side_same and right_side_same
        else:
            return False
