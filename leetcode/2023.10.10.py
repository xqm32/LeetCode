#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#


# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = i
            for j in range(1, i):
                if j * j <= i:
                    dp[i] = min(dp[i], dp[i - j * j] + 1)
                else:
                    break
        return dp[n]


# @lc code=end
