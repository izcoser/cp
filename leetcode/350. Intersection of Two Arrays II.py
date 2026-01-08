from typing import List
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counter = Counter(nums1)
        nums2_counter = Counter(nums2)

        ret = []
        for i in nums1_counter:
            if i in nums2_counter:
                ret.append += [i] * min(nums1_counter[i], nums2_counter[i])
        return ret