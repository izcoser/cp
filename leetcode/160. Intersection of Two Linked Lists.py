from typing import Optional
# LL, easy.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        size_a = get_size(headA)
        size_b = get_size(headB)

        larger, smaller = (headA, headB) if size_a > size_b else (headB, headA)
        i = 0
        while i < abs(size_a - size_b):
            larger = larger.next
            i +=1

        while larger and smaller:
            if larger == smaller:
                return larger
            larger = larger.next
            smaller = smaller.next 

def get_size(head: ListNode) -> int:
    i = 0
    a = head
    while a:
        a = a.next
        i += 1
    return i