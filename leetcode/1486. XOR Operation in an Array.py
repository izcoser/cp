# math, easy
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        x = start
        for i in range(1, n):
            x ^= (start + 2 * i)
        return x