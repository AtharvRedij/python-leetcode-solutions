# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root.left and not root.right:
            return [str(root.val)]

        results = []

        if root.left:
            results.extend([f"{root.val}->{item}" for item in self.binaryTreePaths(root.left)])

        if root.right:
            results.extend([f"{root.val}->{item}" for item in self.binaryTreePaths(root.right)])

        return results
