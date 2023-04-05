"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.traversal = [] 

    def traverse(self, root):
        if root:
            self.traversal.append(root.val)
            for child in root.children:
                self.traverse(child)

    def preorder(self, root: 'Node') -> List[int]:
        self.traverse(root)
        return self.traversal
