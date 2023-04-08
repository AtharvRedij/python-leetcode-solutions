# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], current_depth = 1) -> int:
        if root:
            if root.left and root.right:
                left_depth = self.maxDepth(root.left, current_depth + 1)
                right_depth = self.maxDepth(root.right, current_depth + 1)
                return max(left_depth, right_depth)

            elif root.left:
                return self.maxDepth(root.left, current_depth + 1)

            elif root.right:
                return self.maxDepth(root.right, current_depth + 1)

            else:
                return current_depth
        else:
            return current_depth - 1
