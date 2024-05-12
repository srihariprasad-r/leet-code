class StockSpanner:

    def __init__(self):
        self.stck = []

    def next(self, price: int) -> int:
        cnt = 1
        while self.stck and self.stck[-1][0] <= price:
            cnt += self.stck.pop()[1]

        self.stck.append([price, cnt])
        return cnt
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)    