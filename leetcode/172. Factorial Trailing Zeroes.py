# medium, math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        acc = 0
        while n > 1:
            acc += n // 5
            n //= 5
        return acc
    
# Explanation:
# All we care about is the number of factors of 10.
# These are actually 2 * 5, but factors of 2 will always outnumber
# factors of 5 in any factorial, so in fact we only care about factors of 5.
# E.g. 101 has 20 factors of 5, but also 4 factors of 5^2 which gives us an extra 4 factors.
# We count each 5^2 as only ONE extra factor of 5, because we already counted one of them in the previous iteration.
# The logic continues for higher powers, always giving more extra factors.