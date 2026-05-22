class StockSpanner:

    def __init__(self):
        
        self.arr = []

    def next(self, price: int) -> int:
        if not self.arr:
            self.arr.append((price, 1))

            return 1
        out = 1
        while self.arr and self.arr[-1][0] <= price:
            out += self.arr.pop()[1]
        self.arr.append((price, out))
        
        return out
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)