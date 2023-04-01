class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_mapping = {
            ")": "(",
            "}": "{",
            "]": "[",
        }


        for char in s:
            if char in parentheses_mapping.values():
                stack.append(char)
            else:
                if len(stack) > 0 and stack[-1] == parentheses_mapping[char]:
                    stack.pop(-1)
                else:
                    return False

        return not len(stack)
