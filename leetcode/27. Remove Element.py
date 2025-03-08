from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr = []
        for i in nums:
            if i != val:
                arr.append(i)
        
        for idi, i in enumerate(arr):
            nums[idi] = i
        
        for i in range(len(arr), len(nums)):
            nums[i] = -1
        
        return len(arr)
