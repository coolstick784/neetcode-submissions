# if x is connected to node y and node y is connected to node z, then node x cannot be connected to node z
# each node must be connected to another node

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            if n == 1:
                return True
            else:
                return False
        explored = set()
        conns = {}
        for start, end in edges:
            conns.setdefault(start, set()).add(end)
            conns.setdefault(end, set()).add(start)
        
        def explore(node):
            if node not in conns:
                return False
            explored.add(node)
            for end in conns[node]:
                conns[end].remove(node)
                if end in explored:
                    return False
                if not explore(end):
                    return False
            return True

        if not explore(0):
            return False

        if len(explored) == n:
            return True
        return False