class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        i = len(digits) - 1
        while carry and i >= 0:
            carry = False
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                carry = True

            i -= 1
        
        if carry:
            return [1] + digits
        
        return digits