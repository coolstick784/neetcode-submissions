# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        
        node = head
        while node:
            l += 1
            node = node.next
        if l == n:
            return head.next
        cur_l = 0
        node = head

        while node:
            if l - n == cur_l+1:
                node.next = node.next.next
            cur_l += 1
            node = node.next
        return head