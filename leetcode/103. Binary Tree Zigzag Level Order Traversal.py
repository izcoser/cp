from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict

class Solution:
    def __init__(self):
        self.levels = defaultdict(list)
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node: Optional[TreeNode], level: int):
            if not node:
                return

            self.levels[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
                

        dfs(root, 0)
        for i in self.levels:
            if i %2 != 0:
                self.levels[i] = list(reversed(self.levels[i]))
        res = list(self.levels.values())

        self.levels = defaultdict(list)
        return res

## Other impl using queues:
# def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#     res = []
#     q = deque([root] if root else [])
#     while q:
#         level = []
#         for i in range(len(q)):
#             node = q.popleft()
#             level.append(node.val)
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
#         level = reversed(level) if len(res) % 2 else level
#         res.append(level)