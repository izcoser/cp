# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # linear runtime complexity so we can iterate through the array to count occurrences
        # and then constant extra space means whatever we use to count must be independent of input.
        
        # because nums[i] is between -30k and 30k, we'll create an array where
        # index 0 is -30k and index (60k + 1) is 30k.
        count = [0] * 60001

        for n in nums:
            i = n + 30000
            count[i] += 1

        for i, c in enumerate(count):
            if c == 1:
                return i - 30000