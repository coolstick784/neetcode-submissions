class MedianFinder:

    def __init__(self):
        self.low = [] # descending
        self.high = [] # ascending

    def addNum(self, num: int) -> None:
        if not self.low and not self.high:
            heapq.heappush(self.low, -num)
            return
        if not self.high or len(self.low) > len(self.high): # add to high
            heapq.heappush(self.low, -num)
            pop = -heapq.heappop(self.low)
            heapq.heappush(self.high, pop)
            return 
        if len(self.low) <= len(self.high): # add to low
            heapq.heappush(self.high, num)
            pop = heapq.heappop(self.high)
            heapq.heappush(self.low, -pop)
            return 
            


    def findMedian(self) -> float:
 
        if self.low and self.high and len(self.low) == len(self.high):
            return (-self.low[0] + self.high[0]) /2
        return -self.low[0] 
        