#
# @lc app=leetcode.cn id=901 lang=python3
#
# [901] 股票价格跨度
#


# @lc code=start
class StockSpanner:
    def __init__(self):
        self.stack = []
        self.index = 0

    def next(self, price: int) -> int:
        self.index += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        if not self.stack:
            self.stack.append((price, self.index))
            return self.index
        else:
            res = self.index - self.stack[-1][1]
            self.stack.append((price, self.index))
            return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end
