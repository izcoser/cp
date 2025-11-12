from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        len_list = get_linked_list_length(head)

        if len_list == 0:
            return None

        if len_list == 1:
            return TreeNode(head.val)
        
        # pop middle element
        left, middle, right = pop_element_at_index_n(head, len_list // 2)
        
        node = TreeNode(val=middle.val)
        node.left = self.sortedListToBST(left)
        node.right = self.sortedListToBST(right)
        return node


def get_linked_list_length(head: Optional[ListNode]) -> int:
    n = 0
    node = head
    while node:
        node = node.next
        n += 1
    return n


def pop_element_at_index_n(head: Optional[ListNode], n: int) -> tuple[Optional[ListNode], Optional[ListNode], Optional[ListNode]]:
    if not head:
        return None, None, None

    if n == 0:
        popped = head
        right = head.next
        popped.next = None
        return None, popped, right

    list_len = get_linked_list_length(head)
    if n >= list_len:
        return head, None, None

    if n == list_len - 1:  # removing last element
        node = head
        for _ in range(list_len - 2):
            node = node.next
        popped = node.next
        node.next = None
        popped.next = None
        return head, popped, None

    node = head
    for _ in range(n - 1):
        node = node.next

    popped = node.next
    right = popped.next
    node.next = None
    popped.next = None
    return head, popped, right

# Improved pop:

# def pop_element_at_index_n(head: Optional[ListNode], n: int) -> tuple[Optional[ListNode], Optional[ListNode], Optional[ListNode]]:
#     """
#     Correctly splits the list at index 'n' into three parts:
#     1. Left list (head)
#     2. Middle node (popped)
#     3. Right list (right)
#     """
#     if not head:
#         return None, None, None

#     # Case 1: Popping the head element (n=0)
#     if n == 0:
#         popped = head
#         right = head.next
#         popped.next = None  # Isolate the popped node
#         return None, popped, right  # Left list is None

#     # Case 2: Popping any other element (n > 0)
    
#     # Find the node *just before* the one we want to pop
#     node_before_mid = head
#     for _ in range(n - 1):
#         # This loop is safe because the main function checks for
#         # len_list == 1, so 'n' will never be > 0 for a single-node list.
#         node_before_mid = node_before_mid.next

#     # Identify the three parts
#     popped = node_before_mid.next
#     right = popped.next

#     # Sever the links to create three distinct lists
#     node_before_mid.next = None  # Terminates the left list
#     popped.next = None           # Isolates the middle node

#     return head, popped, right