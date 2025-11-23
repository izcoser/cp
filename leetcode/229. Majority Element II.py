from typing import Optional, List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # there can only be two elements that appear more than n/3 times in the array of n elements.
        count = {}
        max_elements_in_count = 2

        for i in nums:
            if i in count:
                count[i] += 1
            
            else:
                count[i] = 1

            
            if len(count) > max_elements_in_count:
                for k in count.copy():
                    if count[k] == 1:
                        del count[k]
                    elif count[k] > 1:
                        count[k] -= 1
        print(count)
        return [k for k in count if count[k] > len(nums) / 3]
