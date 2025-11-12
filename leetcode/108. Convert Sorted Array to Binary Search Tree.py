from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        nums_length = len(nums)
        if nums_length == 1:
            return TreeNode(val=nums[0])

        middle_index = nums_length // 2
        middle_value = nums[middle_index]

        node = TreeNode(val=middle_value)

        left_arr = [i for i in nums[:middle_index] if i != middle_value]
        right_arr = [i for i in nums[middle_index:] if i != middle_value]

        if len(right_arr) > 0 and len(left_arr) == 0:
            left_arr, right_arr = right_arr, left_arr
        
        node.left = self.sortedArrayToBST(left_arr) if len(left_arr) else None
        node.right = self.sortedArrayToBST(right_arr) if len(right_arr) else None
        
        return node