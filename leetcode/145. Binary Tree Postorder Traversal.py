from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.nodes = []
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root: Optional[TreeNode]):
            if not root:
                return

            postorder(root.left)
            postorder(root.right)
            self.nodes.append(root.val)

        postorder(root)
        ret = self.nodes
        self.nodes = []
        return ret
