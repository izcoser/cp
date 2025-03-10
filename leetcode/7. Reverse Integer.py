from math import log10

class Solution:
    def reverse(self, x: int) -> int:
        ds = digits(abs(x))
        
        multiplier = 1
        n = 0
        stack = []
        for i in reversed(range(ds)):
            stack.append(get_nth_digit(abs(x), i))
        while len(stack) > 0:
            i = stack.pop()
            n += i * 10 ** (len(stack))

        sign = 1
        if x < 0:
            sign = -1
        res = n * sign

        if res < (int)(-2 ** 31):
            res = 0
        if res > (int)((2 ** 31) -1):
            res = 0
        return res 

def get_nth_digit(x: int, n: int) -> int:
    return (x // (int)(10 ** (n))) % 10

def digits(x: int) -> int:
    if x == 0:
        return 1
    return (int)(log10(x)) + 1
