class MyQueue:

    def __init__(self):
        self.primary = []
        self.secondary = []

    def push(self, x: int) -> None:
        self.primary.append(x)

    def pop(self) -> int:
        self.peek()
        return self.secondary.pop()

    def peek(self) -> int:
        if not self.secondary:
            while len(self.primary):
                self.secondary.append(self.primary.pop()) 

        return self.secondary[-1]
            
    def empty(self) -> bool:
        return not self.primary and not self.secondary
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
