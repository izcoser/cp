from typing import List
# medium, two pointers
# Couldn't figure a 2 pointers solution, but we are using a O(1) space and O(n) time as expected.
# Q: How can we prove that at least one duplicate number must exist in nums?
# A: The problem states `nums` has n + 1 integers in a [1, n] range, meaning there are more items than containers.

# The Two Pointer solution uses Floyd's Cycle Detection.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        appearances = [0] * (10 ** 5 + 1)
        for i in nums:
            appearances[i] += 1
            if appearances[i] > 1:
                return i
            
    def findDuplicateFloyd(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow