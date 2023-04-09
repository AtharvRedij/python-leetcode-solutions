# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None

        if root.val in [p.val, q.val]:
            return root

        left_val = self.lowestCommonAncestor(root.left, p, q)
        right_val = self.lowestCommonAncestor(root.right, p, q)
        
        if left_val and right_val:
            return root
        else:
            return left_val or right_val
            
