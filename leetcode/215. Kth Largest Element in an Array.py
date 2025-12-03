from typing import List
from heapq import heappush, heappop, heapify
# minheap, medium
class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #         h = [-i for i in nums]
    #         heapify(h)

    #         for _ in range(k):
    #             a = heappop(h)

    #         return -a
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for i in nums:
            heappush(h, i)
            if len(h) > k:
                heappop(h)
        return h[0]