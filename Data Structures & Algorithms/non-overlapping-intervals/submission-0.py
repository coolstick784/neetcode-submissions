import heapq
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        maxEnd = -1
        intervals.sort()
        heap = []
        for start, end in intervals:
            
            if heap and start < -heap[0]:
                heapq.heappush(heap, -end)
                heapq.heappop(heap)
                res += 1
            else:
                heapq.heappush(heap, -end)
            
        return res