class MyStack:

    def __init__(self):
        self.primary = []
        self.secondary = []
        
    def push(self, x: int) -> None:
        self.primary.append(x)
        
    def rearrange(self, append=True) -> int:
        while len(self.primary) > 1:
            self.secondary.append(self.primary.pop(0))

        top = self.primary.pop(-1)

        while len(self.secondary) > 0:
            self.primary.append(self.secondary.pop(0))

        if append:
            self.primary.append(top)

        return top

    def pop(self) -> int:
        return self.rearrange(False)
        
    def top(self) -> int:
        return self.rearrange()
        
    def empty(self) -> bool:
        return not bool(self.primary)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
