# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a, b = list1, list2
        
        out = ListNode(0)
        tail = out

        while a != None or b != None:
            if a and b:
                if a.val < b.val:
                    tail.next = a
                    a = a.next
                else:
                    tail.next = b
                    b = b.next
            
            elif a:
                tail.next = a
                break
            
            elif b:
                tail.next = b
                break

            tail = tail.next
        
        return out.next