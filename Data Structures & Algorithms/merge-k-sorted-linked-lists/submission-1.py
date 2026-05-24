# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = None
        head = None
        ctr = 0
        while True:

            mn = float('inf')
            cur_mn = None
            cur_idx = None
            for idx, l in enumerate(lists):
                if l and l.val < mn:
                    mn = l.val
                    cur_mn = l
                    cur_idx = idx

            if cur_idx is not None:
                print("cur idx", cur_idx)
                lists[cur_idx] = lists[cur_idx].next
          
            if not cur_mn:
                if head:
                    return head
                return None
            if cur:
                cur.next = cur_mn
                cur = cur_mn
                cur.next = None
            else:
                head = cur_mn
                cur = head
                cur.next = None

            


