from typing import List

# https://leetcode.com/problems/two-sum/
# Poor solution.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
            
        ns = [i for i in nums]
        ns.sort(reverse=True)

        # find the numbers, then their indices.
        for i in range(len(ns) - 1):
            for j in range(i + 1, len(ns)):
                if ns[i] + ns[j] == target:
                    idi, idj = indexes(nums, ns[i], ns[j])
                    return [idi, idj]

def indexes(nums: List[int], a: int, b: int) -> List[int]:
    ret = []
    for idx, i in enumerate(nums):
        if i in (a, b):
            ret.append(idx)
    return ret
