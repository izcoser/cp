# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # skip repeating i
                continue

            l = i + 1
            r = len(nums) - 1
            while(l < r):
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    solution.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]: # skip repeating left pointers
                        l += 1
                    while l < r and nums[r] == nums[r - 1]: # skip repeating right pointers
                        r -= 1
                    l += 1
                    r -= 1
        return solution