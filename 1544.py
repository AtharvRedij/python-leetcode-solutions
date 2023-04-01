class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            if not stack:
                stack.append(char)
                continue

            if stack[-1] == char:
                stack.append(char)

            elif stack[-1] == char.upper():
                stack.pop(-1)

            elif stack[-1] == char.lower():
                stack.pop(-1)

            else:
                stack.append(char)


        return "".join(stack)
