#
# @lc app=leetcode.cn id=667 lang=python3
#
# [667] 优美的排列 II
#

# @lc code=start
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        for i in range(1, n - k):
            res.append(i)
        for i in range(k + 1):
            res.append(n - k + i // 2 if i % 2 == 0 else n - i // 2)
        return res


# @lc code=end
