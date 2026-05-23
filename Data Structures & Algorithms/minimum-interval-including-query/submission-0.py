class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = [(n, idx) for idx, n in enumerate(queries)]
        queries.sort()
        intervals.sort()
        res = [None for _ in queries]
        heap = [] # dist, start, end
        query_idx = 0
        idx = 0

        while query_idx < len(queries):
            if idx < len(intervals):
                start, end = intervals[idx]
            cur_n, cur_idx = queries[query_idx]
            if idx == len(intervals) or start > cur_n:
                while heap and (heap[0][1] > cur_n or heap[0][2] < cur_n):
                    heapq.heappop(heap)
                if heap:
                    res[cur_idx] = heap[0][0]
                else:
                    res[cur_idx] = -1
                query_idx += 1
            else:
                heapq.heappush(heap, (end-start+1, start, end))
                idx += 1
        
        return res
