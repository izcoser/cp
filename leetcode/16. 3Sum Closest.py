# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('-inf')
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # skip repeating i
                continue

            l = i + 1
            r = len(nums) - 1
            while(l < r):
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                elif s > target:
                    r -= 1
                elif s < target:
                    l += 1
                
                if abs(target - closest) > abs(target - s):
                    closest = s
        
        return closest