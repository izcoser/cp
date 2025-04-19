# https://leetcode.com/problems/4sum/description/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        len_nums = len(nums)

        if len_nums < 4:
            return []
        
        nums.sort()
        res = []
        
        for i in range(len_nums - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, len_nums - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                r = len_nums - 1
                l = j + 1
                
                while l < r and l < len_nums:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])

                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1

                        r -= 1
                        l += 1

        return res