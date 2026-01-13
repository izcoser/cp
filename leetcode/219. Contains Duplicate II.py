from typing import List
# hashtable, easy
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index = {}
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i] in last_index:
                if i - last_index[nums[i]] <= k:
                    return True
                last_index[nums[i]] = i
            else:
                last_index[nums[i]] = i
        
        return False