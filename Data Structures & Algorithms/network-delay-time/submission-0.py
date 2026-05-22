class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0, k)] #cost, cur nodes, node number
        edges = {}
        for start, end, time in times:
            edges.setdefault(start, []).append((end, time))
        best = [float('inf') for i in range(n+1)] # we want to know the best time to get to each node, then return the max
        best[k] = 0
        while heap:
            cur_time, node = heapq.heappop(heap)
            for end, time in edges.get(node, []):
                if cur_time + time < best[end]:
                    heapq.heappush(heap, (cur_time+time, end))
                    best[end] = cur_time + time

        res = max(best[1:])
        if res == float('inf'):
            return -1
        return res

