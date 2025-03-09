from typing import List

# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # there are 2^len(nums) subsets.
        # subset 0 -> [] (000)
        # subset 1 -> [1] (001)
        # subset 2 -> [2] (010)
        # subset 3 -> [1, 2] (011)

        results = []
        for i in range((int)(2**(len(nums)))):
            subset = []
            i_as_list = [int(d) for d in str(bin(i))[2:].zfill(len(nums))]
            for idj, j in enumerate(i_as_list):
                if j == 1:
                    subset.append(nums[idj])
            
            results.append(subset)
        
        return results
