from typing import List
# O(1) space, O(n) runtime, leveraging arithmetic progression formula
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_nums = len(nums)
        return (1 + len_nums) * len_nums // 2 - sum(nums) 
        