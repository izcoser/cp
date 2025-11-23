class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            s = 0
            while num > 0:
                s += num % 10
                num = num // 10
            num = s
        return num
    
    
        # digital root solution:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9