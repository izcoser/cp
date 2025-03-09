from typing import List

# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        # backtracking problem again... can do this without backtracking but anyway.

        results = []

        def backtrack(ns: List[int]):
            if len(nums) == len(ns):
                results.append(ns[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    ns.append(nums[i])
                    used[i] = True

                    backtrack(ns)

                    ns.pop()
                    used[i] = False
        
        backtrack([])
        return results
        