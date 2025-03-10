from typing import List

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        s = 0
        for idx, x in enumerate(nums):
            a_exists = idx - k >= 0
            b_exists = idx + k < len(nums)

            if not a_exists and not b_exists:
                s += x
            
            elif a_exists and b_exists:
                if x > nums[idx - k] and x > nums[idx + k]:
                    s +=x
                
            elif a_exists and x > nums[idx - k]:
                s +=x
                
            elif b_exists and x > nums[idx + k]:
                s +=x
        return s
        