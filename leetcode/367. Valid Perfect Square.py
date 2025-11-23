class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        lower_bound = 1
        upper_bound = num // 2

        while lower_bound <= upper_bound:
            val = (upper_bound + lower_bound) // 2
            square = val * val
            if square == num:
                return True

            if square < num:
                lower_bound = val + 1
            else:
                upper_bound = val - 1

        return False