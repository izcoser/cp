from collections import Counter
from heapq import heappush, heappop
from typing import List

# min heap, medium (or just sort the array in descending order and iterate)
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        len_arr = len(arr)
        count = Counter(arr)
        h = []
        for k, v in count.items():
            heappush(h, -v)
        
        removed = len_arr
        i = 0
        while removed > len_arr // 2:
            removed += heappop(h)
            i += 1

        return i