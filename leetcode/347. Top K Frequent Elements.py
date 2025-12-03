from typing import List
from collections import Counter
from heapq import heappush, heappop, nlargest

# heap, medium

class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     c = Counter(nums)
    #     h = []
    #     for key, value in c.items():
    #         heappush(h, (-value, key))

    #     return [heappop(h)[1] for _ in range(k)]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        h = []
        for key, value in c.items():
            heappush(h, (value, key))
            if len(h) > k:
                heappop(h)


        return [item[1] for item in h]


    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     return [x for x, _ in nlargest(k, Counter(nums).items(), key=lambda x: x[1])] # CPython impl.