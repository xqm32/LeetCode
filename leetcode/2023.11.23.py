#
# @lc app=leetcode.cn id=790 lang=python3
#
# [790] 多米诺和托米诺平铺
#


# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0, 0] for _ in range(n + 1)]
        dp[0][0] = 1
        dp[1][0] = 1
        for i in range(2, n + 1):
            dp[i][0] = (dp[i - 1][0] + dp[i - 2][0] + dp[i - 1][1] * 2) % MOD
            dp[i][1] = (dp[i - 2][0] + dp[i - 1][1]) % MOD
        return dp[n][0]


# @lc code=end
