from typing import Optional, List
from heapq import heapify, heappop
# min heap, easy
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        h = [-1 * i for i in nums]
        heapify(h)

        a, b = heappop(h), heappop(h)

        return (-1 * a - 1) * (-1 * b - 1)