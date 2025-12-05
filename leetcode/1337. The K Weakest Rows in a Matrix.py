from heapq import heappush, heappop
from typing import List
# max heap, easy
class Solution:
    def kWeakestRows(self, mat, k):
        h = []
        for i, row in enumerate(mat):
            heappush(h, (-self.count_binary(row), -i))
            if len(h) > k:
                heappop(h)
        
        h = [(-count, -i) for count, i in h]
        return [i for _, i in sorted(h)]


    def count_binary(self, row: List[int]):
        lo, hi = 0, len(row)
        while lo < hi:
            mid = (lo + hi) // 2
            if row[mid] == 1:
                lo = mid + 1
            else:
                hi = mid
        
        return lo