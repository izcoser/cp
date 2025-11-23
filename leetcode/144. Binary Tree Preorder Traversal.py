from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.nodes = []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root: Optional[TreeNode]):
            if not root:
                return

            self.nodes.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        ret = self.nodes
        self.nodes = []
        return ret
        