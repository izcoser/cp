# medium, math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        acc = 0
        while n > 1:
            acc += n // 5
            n //= 5
        return acc