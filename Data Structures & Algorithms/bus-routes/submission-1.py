from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        explored = set()
        stops_explored = set()
        routes = [set(r) for r in routes]
        stations = {}
        for idx, r in enumerate(routes):
            for stop in r:
                stations.setdefault(stop, set()).add(idx)
        
        
        q = deque()    
        res = float('inf')
        for r in stations.get(source, set()):
            q.append((r, 1))
        while q:
            r, ct = q.popleft()
            explored.add(r)
            if target in routes[r]:
                return ct
            for stop in routes[r]:
                if stop in stops_explored:
                    continue
                stops_explored.add(stop)
                for route in stations.get(stop, set()):
                    if route in explored:
                        continue
                    q.append((route, ct+1))

        return -1
        




        