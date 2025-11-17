# easy
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n) memory, O(n) time
        a = set()
        for i in nums:
            if i in a:
                return True
            a.add(i)
        return False
    
    def containsDuplicateSort(self, nums: List[int]) -> bool:
        # O(1) memory, O(n log n) time
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False