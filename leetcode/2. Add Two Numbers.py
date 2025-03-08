from typing import Optional, List

# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        multiplier = 1
        node = l1
        while node != None:
            n1 += (node.val * multiplier)
            multiplier *= 10
            node = node.next

        n2 = 0
        multiplier = 1
        node = l2

        while node != None:
            n2 += (node.val * multiplier)
            multiplier *= 10
            node = node.next

        s = n1 + n2
        return_list = [int(i) for i in reversed(list(str(s)))]
        a = ListNode(val=return_list[0])
        it = a
        for i in return_list[1:]:
            it.next = ListNode(val=i)
            it = it.next
        
        return a



        

        