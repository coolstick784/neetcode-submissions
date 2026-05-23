class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def trace(e):
            if e == key[e]:
                return e
            val = trace(key[e])
            key[e] = val
            return val
        
        

        def union_find(e1, e2):
            key[trace(key[e2])] = trace(key[e1])
            
            
        

        conns = {}
        for start, end in edges:
            conns.setdefault(start, set()).add(end)
            conns.setdefault(end, set()).add(start)
        key = [idx for idx in range(n)]
        for start in conns:
            for end in conns.get(start, []):
                union_find(start, end)
                conns[end].remove(start)

        return len([e for e in range(n) if key[e] == e])