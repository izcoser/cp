# medium, tree, iterative dfs
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.node = root
        
    def next(self) -> int:
        while self.node or len(self.stack) > 0:
            while self.node:
                self.stack.append(self.node)
                self.node = self.node.left
            self.node = self.stack.pop()
            ret = self.node.val
            self.node = self.node.right
            return ret


    def hasNext(self) -> bool:
        return len(self.stack) > 0 or self.node != None

# Read the entire tree to an array in __init__.
# Does not conform with follow up: next() and hasNext() in O(h) memory, stack approach conforms with it. 
# def __init__(self, root: Optional[TreeNode]):
#     def traverse(root: Optional[TreeNode]):
#         if not root:
#             return
#         traverse(root.left)
#         self.values.append(root.val)
#         traverse(root.right)

#     self.values = []
#     traverse(root)
#     self.current = -1
    
# def next(self) -> int:
#     self.current += 1
#     return self.values[self.current]

# def hasNext(self) -> bool:
#     return self.current < len(self.values) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()