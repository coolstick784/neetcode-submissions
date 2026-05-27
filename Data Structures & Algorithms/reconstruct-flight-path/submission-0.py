class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for start, end in sorted(tickets)[::-1]:
            adj.setdefault(start, []).append(end)
        
        stack = ['JFK']
        res = []
        while stack:
            if not adj.get(stack[-1]):
                res.append(stack.pop())
            else:
                stack.append(adj[stack[-1]].pop())
        return res[::-1]