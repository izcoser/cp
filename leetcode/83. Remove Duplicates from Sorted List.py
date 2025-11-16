from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = head
        previous = n

        if not n:
            return None

        while n:
            previous = n
            n = n.next

            if not n:
                break

            while previous.val == n.val:
                previous.next = n.next
                n = n.next
                if not n:
                    break

        return head