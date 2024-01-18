#
# @lc app=leetcode.cn id=900 lang=python3
#
# [900] RLE 迭代器
#


# @lc code=start
class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.index = 0

    def next(self, n: int) -> int:
        while self.index < len(self.encoding):
            if self.encoding[self.index] >= n:
                self.encoding[self.index] -= n
                return self.encoding[self.index + 1]
            else:
                n -= self.encoding[self.index]
                self.index += 2
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
# @lc code=end
