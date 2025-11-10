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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return self.branch(root, 1)

    def branch(self, node: Optional[TreeNode], depth: int):
        if node == None:
            return sys.maxsize
        if node.left == None and node.right == None:
            return depth

        return min(self.branch(node.left, depth + 1), self.branch(node.right, depth + 1))