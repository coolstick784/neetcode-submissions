# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        def rev(curHead):
    
            ctr = 0
  

            curNode = curHead
            
            prev = None
            new = None
        
            while ctr < k:
                new = curNode.next
       
                curNode.next = prev
  
             
                prev = curNode
                curNode = new
                ctr += 1
            curHead.next = new
            
            return prev

        def solve(node):
            if not node:
                return node

            ctr = 1
            cur = node
            while cur and ctr < k:
                ctr += 1
                cur = cur.next
            
            if ctr < k or not cur:
                return node

            cur.next = solve(cur.next)

            return rev(node)
        return solve(head)