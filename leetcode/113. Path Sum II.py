from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.paths = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def pathSumRec(root: Optional[TreeNode], targetSum: int, path: List[int]):
            if not root:
                return
            if not root.left and not root.right and root.val == targetSum:
                path.append(root.val)
                self.paths.append(path)
                return
            
            targetSum -= root.val
            path.append(root.val)
            
            pathSumRec(root.left, targetSum, path.copy())
            pathSumRec(root.right, targetSum, path.copy())

        pathSumRec(root, targetSum, [])
        ret = self.paths
        self.paths = []
        return ret

# Alternate impl.    
# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#         if not root:
#             return []

#         stack = [(root, False, [root.val])]
#         res = []

#         while len(stack) != 0:
#             node, visited, path = stack.pop()

#             if node != None:
#                 if visited:
#                     if not node.left and not node.right and sum(path) == targetSum:
#                         res.append(path)

#                 else:
#                     stack.append((node, True, path))
                    
#                     if node.left:
#                         stack.append((node.left, False, path + [node.left.val]))
#                     if node.right:
#                         stack.append((node.right, False, path + [node.right.val]))
        
#         return res
