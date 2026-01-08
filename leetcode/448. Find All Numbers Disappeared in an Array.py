from typing import List
# easy, hash table
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret = set([i + 1 for i in range(len(nums))])
        for i in nums:
            if i in ret:
                ret.remove(i)
        ret = list(ret)
        ret.sort()
        return ret