from typing import List
from heapq import heappop, heappush, heapify

# minheap, easy

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-1 * i for i in stones]
        heapify(h)

        while len(h) >= 2:
            s1 = heappop(h)
            s2 = heappop(h)

            if s1 == s2:
                continue

            else:
                heappush(h, -1 * abs(s1 - s2))

        return -1 * h[0] if len(h) == 1 else 0            

# [2,7,4,1,8,1] => 8, 7 -> [2,4,1,1,1] -> 4, 2 -> [2,1,1,1] -> 2, 1 -> [1,1,1] -> [1]