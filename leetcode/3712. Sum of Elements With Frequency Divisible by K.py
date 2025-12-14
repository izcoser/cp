from collections import Counter
from typing import List

# easy, counting
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        return sum([num * freq for num, freq in count.items() if freq % k == 0])