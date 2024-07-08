#
# @lc app=leetcode.cn id=903 lang=python3
#
# [903] DI 序列的有效排列
#

# @lc code=start
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n = len(s)
        mod = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, n + 1):
            for j in range(i + 1):
                if s[i - 1] == "D":
                    for k in range(j, i):
                        dp[i][j] += dp[i - 1][k]
                        dp[i][j] %= mod
                else:
                    for k in range(j):
                        dp[i][j] += dp[i - 1][k]
                        dp[i][j] %= mod
        return sum(dp[n]) % mod


# @lc code=end
