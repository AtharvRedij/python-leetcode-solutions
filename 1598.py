class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0

        for operation in logs:
            if operation == "./":
                continue
            elif operation == "../":
                if depth > 0:
                    depth -= 1
            else:
                depth += 1

        return depth
