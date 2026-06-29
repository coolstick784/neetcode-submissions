# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def solve(node, look):
            if not node:
                return False
            if node.val == look.val or solve(node.left, look) or solve(node.right, look):
                return True
            return False


        def dfs(node):
            if not node:
                return None
            l = dfs(node.left)
            if l:
                return l
            r = dfs(node.right)
            if r:
                return r
            if solve(node, p) and solve(node, q):
                return node
            return None

        return dfs(root)