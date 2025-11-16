class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for _ in range(n - 1):
            val = one + two
            two = one
            one = val
        return one
    

    def climbStairsDfs(self, n: int) -> int:
        pass