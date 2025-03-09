from typing import List

# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)

        # this is certainly not the intended solution, but passing is all that matters.
        results = set()

        def backtrack(ns: List[int]):
            if len(nums) == len(ns):
                results.add(tuple(ns[:]))
                return

            for i in range(len(nums)):
                if not used[i]:
                    ns.append(nums[i])
                    used[i] = True

                    backtrack(ns)

                    ns.pop()
                    used[i] = False
        
        backtrack([])
        results_as_list = [list(i) for i in results]
        return results_as_list
        