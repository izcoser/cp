from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        min_diff = float('inf')
        out = []
        for i in range(len(arr) - 1):
            a, b = arr[i], arr[i + 1]
            diff = abs(a - b)
            if diff < min_diff:
                min_diff = diff
        
        for i in range(len(arr) - 1):
            a, b = arr[i], arr[i + 1]
            diff = abs(a - b)
            if diff == min_diff:
                out.append([a, b])
        
        return out