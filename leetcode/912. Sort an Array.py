from typing import List
# heap from scratch, medium
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heapify(nums)
        len_nums = len(nums)
        return [self.pop(nums) for i in range(len_nums)]

    def heapify(self, nums: List[int]):
        n = len(nums)
        for i in range(n//2 - 1, -1, -1):
            self.sift_down(nums, i, n)

    def sift_down(self, nums: List[int], i: int, n: int):
        while True:
            left = 2*i + 1
            right = 2*i + 2
            smallest = i

            if left < n and nums[left] < nums[smallest]:
                smallest = left
            if right < n and nums[right] < nums[smallest]:
                smallest = right
            
            if i == smallest: # i didn't change.
                break

            nums[i], nums[smallest] = nums[smallest], nums[i]
            i = smallest

    def pop(self, nums: List[int]):
        nums[0], nums[-1] = nums[-1], nums[0]
        val = nums.pop()

        self.sift_down(nums, 0, len(nums))

        return val