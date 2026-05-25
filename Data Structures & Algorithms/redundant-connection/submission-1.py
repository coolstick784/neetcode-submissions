# an edge is necessary if 
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = [n for n in range(len(edges) + 1)]
        
        def trace(n):
            if union_find[n] == n:
                return n
            val = trace(union_find[n])
            union_find[n] = val
            return val
        def union(n1, n2):
            union_find[trace(n2)] = trace(n1)
        
        for start, end in edges:
            if trace(start) == trace(end):
                return [start, end]
            union(start, end)