# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        new_head = ListNode()

        answer = ListNode()
        answer.next = new_head

        extra_num = 0

        while l1 is not None or l2 is not None or extra_num == 1:
            new_node = ListNode()

            if l1 is None:
                l1 = ListNode()

            if l2 is None:
                l2 = ListNode()

            crnt_num = l1.val + l2.val + extra_num

            if crnt_num >= 10:
                extra_num = 1
                crnt_num = crnt_num - 10
            else:
                extra_num = 0

            new_node.val = crnt_num

            new_head.next = new_node
            new_head = new_head.next

            l1 = l1.next
            l2 = l2.next

        return answer.next.next
