class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        stack_size = 0

        for operation in operations:
            if operation == "+":
                if stack_size >= 2:
                    stack.append(stack[-1] + stack[-2])
                    stack_size += 1
            elif operation == "D":
                if stack_size >= 1:
                    stack.append(stack[-1] * 2)
                    stack_size += 1
            elif operation == "C":
                if stack_size >= 1:
                    stack.pop(-1)
                    stack_size -= 1
            else:
                stack.append(int(operation))
                stack_size += 1

        return sum(stack)
