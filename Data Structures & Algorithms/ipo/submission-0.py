# always choose the one with the most profit with the given capital


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        zipped = deque(sorted(list(zip(capital, profits))))
        heap = []
        left = k
        res = w
        while left > 0 and (heap or (zipped and zipped[0][0] <= res)):
            while zipped and zipped[0][0] <= res:
                c, p = zipped.popleft()
                heapq.heappush(heap, -p)
            res += -heapq.heappop(heap)
            left -= 1
            

        return res
        
        