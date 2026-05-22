class FreqStack:

    def __init__(self):
        self.ctr = 0
        self.time = 0
        self.heap = [] # -ctr, -time, num
        self.ctr = {}

    def push(self, val: int) -> None:
        self.time += 1
        self.ctr[val] = self.ctr.get(val, 0) + 1
        heapq.heappush(self.heap, (-self.ctr[val], -self.time, val))

    def pop(self) -> int:
        self.time += 1
        while -self.heap[0][0] != self.ctr[self.heap[0][2]]:
            heapq.heappop(self.heap)
        ctr, t, val = heapq.heappop(self.heap)
        ctr = -ctr
        self.ctr[val] -= 1
        t = -t
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()