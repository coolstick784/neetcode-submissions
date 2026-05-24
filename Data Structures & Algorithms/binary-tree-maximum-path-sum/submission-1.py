# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -float('inf')
        def explore(node):
            if node is None:
                return 0
            l = max(explore(node.left), 0)
            r = max(explore(node.right), 0)
            val = node.val + l + r
            self.res = max(self.res, val)
            to_return = node.val + max(l, r)
            return to_return
            

        explore(root)
        return self.res