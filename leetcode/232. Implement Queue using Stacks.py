# queue, easy
from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q

class MyQueue:

    def __init__(self):
        self.s1 = MyStack()
        self.s2 = MyStack()
        

    def push(self, x: int) -> None:
        self.s1.push(x)
        

    def pop(self) -> int:
        if self.s2.empty():
            while not self.s1.empty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2.empty():
            while not self.s1.empty():
                self.s2.push(self.s1.pop())
        return self.s2.top()

    def empty(self) -> bool:
        return self.s1.empty() and self.s2.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()