class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        parentheses_sets = []
        current_set_size = 0
        start = None

        for i in range(len(s)):
            if s[i] == "(":
                if current_set_size == 0:
                    start = i
                current_set_size += 1

            elif s[i] == ")":
                current_set_size -= 1
                if current_set_size == 0:
                    parentheses_sets.append(s[start+1:i])

        return "".join(parentheses_sets)
