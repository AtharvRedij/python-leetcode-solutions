# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.traversal = [] 

    def traverse(self, root):
        if root:
            self.traverse(root.left)
            self.traverse(root.right)
            self.traversal.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.traversal
