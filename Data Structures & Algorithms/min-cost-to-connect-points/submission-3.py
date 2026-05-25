class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        # start with a point, then ask: what's the closest point to any of our current points that isn't a current point?

        cur_points = set()
        heap = []
        self.res = 0
        
        def add_point(x, y):
            print((x, y))
            cur_points.add((x, y))
            
            for cx, cy in points:
                if (cx, cy) in cur_points:
                    continue 
                heapq.heappush(heap, (abs(x-cx) + abs(y-cy), cx, cy))

            while heap:
                dist, cx, cy = heapq.heappop(heap)

                if (cx, cy) not in cur_points:
                    add_point(cx, cy)
                    self.res += dist
                    break
            
            
            if (cx, cy) not in cur_points:

                add_point(cx, cy)
                self.res += dist

        x, y = points[0]
        add_point(x, y)
        return self.res