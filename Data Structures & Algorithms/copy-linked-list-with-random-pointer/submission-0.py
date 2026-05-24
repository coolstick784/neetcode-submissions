"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ids = set()
        newNodes = {}
        

        def dfs(node):
            if not node:
                return node
            if id(node) in ids:
                return newNodes[id(node)]

            ids.add(id(node))
            
            new = Node(node.val)
            newNodes[id(node)] = new

            new.next = dfs(node.next)
            new.random = dfs(node.random)
            
            return new
        return dfs(head)