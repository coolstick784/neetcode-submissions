class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        best = {}
        heap = [(grid[0][0], 0, 0)]
        best[(0, 0)] = grid[0][0]
        n = len(grid)
        def explore(cur_cost, cr, cc):
            if cr < 0 or cc < 0 or cr >= n or cc >= n:
                return 
            new_cost = max(cur_cost, grid[cr][cc])
            if new_cost < best.get((cr, cc), float('inf')):
                best[(cr, cc)] = new_cost
                heapq.heappush(heap, (new_cost, cr, cc))
        while heap:
            
            cost, r, c = heapq.heappop(heap)

            if cost > best[(r, c)]:
                continue
            if r == n-1 and c == n-1:
                return cost
            explore(cost, r+1, c)
            explore(cost, r-1, c)
            explore(cost, r, c+1)
            explore(cost, r, c-1)
