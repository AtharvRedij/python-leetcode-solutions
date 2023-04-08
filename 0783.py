# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.traversal = []

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.traversal.append(root.val)
            self.inorder(root.right)

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)
        min_diff = None

        for i in range(len(self.traversal) - 1):
            diff = self.traversal[i+1] - self.traversal[i]

            if min_diff is None:
                min_diff = diff
            else:
                min_diff = min(min_diff, diff)

        return min_diff
