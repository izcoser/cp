from typing import List
# medium, two pointers
# Couldn't figure a 2 pointers solution, but we are using a O(1) space and O(n) time as expected.
# Q: How can we prove that at least one duplicate number must exist in nums?
# A: The problem states `nums` has n + 1 integers in a [1, n] range, meaning there are more items than containers.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        appearances = [0] * (10 ** 5 + 1)
        for i in nums:
            appearances[i] += 1
            if appearances[i] > 1:
                return i