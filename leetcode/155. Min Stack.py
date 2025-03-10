class MinStack:

    def __init__(self):
        self.s = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.min_stack) == 0 or self.min_stack[0] >= val:
            self.min_stack.insert(0, val)

    def pop(self) -> None:
        val = self.s.pop()
        if len(self.min_stack) > 0 and val == self.min_stack[0]:
            self.min_stack = self.min_stack[1:]
        return val

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.min_stack[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()