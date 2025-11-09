from typing import List
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

MIN = -1 * 10 **8 
MAX = 1 * 10 ** 8

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # smaller
        a, b = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        
        lo = 0
        hi = len(a)
        total_elements = len(nums1) + len(nums2)
        
        while (lo <= hi):
            part_a = (lo + hi) // 2
            part_b = (total_elements + 1) // 2 - part_a

            left_a = get_max(a, part_a)
            right_a = get_min(a, part_a)

            left_b = get_max(b, part_b)
            right_b = get_min(b, part_b)

            if left_a <= right_b and left_b <= right_a:
                if total_elements % 2 == 0:
                    return (max(left_a, left_b) + min(right_a, right_b)) / 2.0
                return max(left_a, left_b)
            
            if left_a > left_b:
                hi = part_a - 1
            else:
                lo = part_a + 1
        
        return -1

def get_max(nums: List[int], partition: int):
    if partition == 0:
        return MIN
    return nums[partition - 1]


def get_min(nums: List[int], partition: int):
    if partition == len(nums):
        return MAX
    return nums[partition]