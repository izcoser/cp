class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search with integers from 1 to x // 2
        if x < 1:
            return 0
        
        if x == 1:
            return 1
        
        lower_bound = 1
        upper_bound = x // 2

        while lower_bound <= upper_bound:
            val = (upper_bound + lower_bound) // 2
            square = val * val
            if square == x:
                return val

            if square < x:
                lower_bound = val + 1
            else:
                upper_bound = val - 1

        return upper_bound