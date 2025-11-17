# easy
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = nums[0]
        for i in nums:
            if res == i:
                count += 1
            else:
                count -= 1
                if count == -1:
                    count = 1
                    res = i
        return res

# Naive solution.
# def majorityElement(self, nums: List[int]) -> int:
#     count = defaultdict(int)
#     size = len(nums)
#     for i in nums:
#         count[i] += 1
#         if count[i] > size / 2:
#             return i