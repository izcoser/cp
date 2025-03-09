from typing import List

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = []
        prev = -200
        for i in nums:
            if i != prev:
                arr.append(i)
            prev = i
        
        for idi, i in enumerate(arr):
            nums[idi] = i
        
        for i in range(len(arr), len(nums)):
            nums[i] = -1
        
        return len(arr)
