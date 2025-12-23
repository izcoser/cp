from typing import List
# medium, matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_column = [row[0] for row in matrix]

        # binary search on first column to find out the row where the element may be.
        l = 0
        r = len(first_column) - 1

        while r - l > 1:
            mid = (l + r) // 2
            if target > first_column[mid]:
                l = mid
            elif target < first_column[mid]:
                r = mid - 1
            else:
                return True

        arr = matrix[l] + matrix[r]
        # binary search on the final array.
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid)
            if target > arr[mid]:
                l = mid + 1
            elif target < arr[mid]:
                r = mid - 1
            else:
                return True

        return False
