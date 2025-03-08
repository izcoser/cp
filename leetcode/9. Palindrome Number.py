from math import log10

# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative numbers can't be palindrome.
        if x < 0:
            return False
        
        d = digits(x)
        if d == 1:
            return True
        
        for i in range((d // 2) + 1):
            rightmost = get_nth_digit(x, i)
            leftmost = get_nth_digit(x, d - i - 1)

            if rightmost != leftmost:
                return False
            
        return True
        
def get_nth_digit(x: int, n: int) -> int:
    return (x // (int)(10 ** (n))) % 10

def digits(x: int) -> int:
    if x == 0:
        return 1
    return (int)(log10(x)) + 1

