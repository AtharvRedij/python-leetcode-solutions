"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import defaultdict

class Solution:
    def __init__(self):
        self.level_nodes = defaultdict(list) 

    def traverse(self, root, index):
        if root:
            self.level_nodes[index].append(root.val)

            for child in root.children:
                self.traverse(child, index+1)

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.traverse(root, 0)

        results = []
        
        for i in range(len(self.level_nodes)):
            results.append(self.level_nodes[i])

        return results
