class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        nested_size = 0

        for char in s:
            if char == "(":
                nested_size += 1
                max_depth = max(max_depth, nested_size)
            elif char == ")":
                nested_size -= 1

        return max_depth
