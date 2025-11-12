from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
class Solution:
    def __init__(self):
        self.levels = defaultdict(list)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node: Optional[TreeNode], level: int):
            if not node:
                return

            self.levels[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        res = list(self.levels.values())

        self.levels = defaultdict(list)
        return res
