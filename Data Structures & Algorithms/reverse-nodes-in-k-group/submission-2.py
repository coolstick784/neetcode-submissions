# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        def rev(node):
            curCt = 1
            if not node or not node.next:
                return node
            prev = node
            cur = node.next
            while curCt < k and cur:
                new = cur.next
                cur.next = prev
                prev = cur
                cur = new
                curCt += 1
            node.next = cur
            return prev


        l = 0
        cur = head
        while cur:
            l += 1
            cur =cur.next
        ct = 0
        cur = head
        while cur:


            if (ct == 0 and k <= l) or ((ct+1) % k == 0 and ct < l - k):

                if ct != 0:
                    cur.next= rev(cur.next)
                else:
                    newHead = rev(cur)
                    cur = newHead
            
            
            
            ct += 1
            cur = cur.next

        return newHead

        