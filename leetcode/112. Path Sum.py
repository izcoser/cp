# https://leetcode.com/problems/minimum-depth-of-binary-tree/
from typing import Optional
import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        return self.branch(root, 0, targetSum)

    def branch(self, node: Optional[TreeNode], sum: int, target: int):
        if node == None:
            return False

        sum += node.val
        
        if not node.left and not node.right:
            return sum == target

        return self.branch(node.left, sum, target) or self.branch(node.right, sum, target)