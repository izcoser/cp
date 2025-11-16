from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head

        l = list_len(head)
        if l in (0, 1):
            return head

        rotations = k % l
        if rotations == 0:
            return head

        slice_at_position = l - rotations
        return list_slice_and_append_at_start(head, slice_at_position)

def list_len(head: Optional[ListNode]) -> int:
    i = 0
    n = head
    while n:
        n = n.next
        i += 1
    return i

def list_slice_and_append_at_start(head: Optional[ListNode], position: int) -> Optional[ListNode]:
    # slice a list at `position`, append the sliced portion before the head.
    i = 1
    n = head
    while i != position:
        n = n.next
        i += 1
    
    sliced = n.next
    n.next = None

    n = sliced
    while n.next:
        n = n.next
    n.next = head
    return sliced
