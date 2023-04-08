# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original:
            if original.val == target.val:
                return cloned
            else:
                ref_in_left = self.getTargetCopy(original.left, cloned.left, target)
                ref_in_right = self.getTargetCopy(original.right, cloned.right, target)
                return ref_in_left or ref_in_right
        else:
            return None
