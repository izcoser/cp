import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        TOL = 0.0000000001
        if n <= 0:
            return False
        
        log = math.log(n, 2)
        return abs(int(log) - log) < TOL
        