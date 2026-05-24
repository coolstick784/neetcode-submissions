# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = 1
        n1 = 0
        cur = l1
        while cur:
            n1 += p * cur.val
            cur = cur.next
            p *= 10
        n2 = 0
        cur = l2
        p = 1
        while cur:
            n2 += p * cur.val
            cur = cur.next
            p *= 10
        total = n1 + n2
        new = ListNode()
        cur = new

        while total:
            cur.val = total % 10
            total = total // 10
            if total:
                cur.next = ListNode()
                cur = cur.next

        return new
