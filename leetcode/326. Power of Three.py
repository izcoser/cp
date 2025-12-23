# math, easy
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        largest = 3**20
        return largest % n == 0