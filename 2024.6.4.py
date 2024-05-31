#
# @lc app=leetcode.cn id=519 lang=python3
#
# [519] 随机翻转矩阵
#

# @lc code=start
class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.dic = {}

    def flip(self) -> List[int]:
        idx = random.randint(0, self.total - 1)
        x = self.dic.get(idx, idx)
        self.total -= 1
        self.dic[idx] = self.dic.get(self.total, self.total)
        return [x // self.n, x % self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.dic.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
# @lc code=end
