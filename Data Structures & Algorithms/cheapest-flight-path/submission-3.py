class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dest = {}
        for start, end, price in flights:
            dest.setdefault(start, []).append((end, price))
        

        heap = [(0, -1, src)]
        while heap:
    
            price, val, cur = heapq.heappop(heap)
            if cur == dst:
                return price
            if val >= k:
                continue
            for new, add in dest.get(cur, []):
                
                heapq.heappush(heap, (price+add, val+1, new))
     

 

        return -1