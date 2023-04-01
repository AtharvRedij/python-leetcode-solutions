class Solution:
    def get_stack_repr(self, text):
        stack = []
        for char in text:
            if char == "#":
                if len(stack):
                    stack.pop(-1)
            else:
                stack.append(char)

        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = self.get_stack_repr(s)
        t_stack = self.get_stack_repr(t)

        while s_stack and t_stack:
            if s_stack.pop(-1) != t_stack.pop(-1):
                return False

        return not bool(s_stack or t_stack)
