# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1:
            return 1
        if x == -1:
            return 1 if n % 2 == 0 else -1
        if x == 0:
            return 0

        if n < 0:
            op = lambda a, b: a / b
        else:
            op = lambda a, b: a * b

        res = 1
        prev = 0
        for _ in range(abs(n)):
            res = op(res, x)
            if res == prev:
                break
            prev = res

        return res
