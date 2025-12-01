from typing import List
from heapq import heappush, heappop, heapify

# min heap, medium

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        heapify(self.h)
        self.k = k

        for _ in range(len(nums) - k):
            heappop(self.h)

    def add(self, val: int) -> int:
        heappush(self.h, val)

        if len(self.h) > self.k:
            heappop(self.h)
        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)