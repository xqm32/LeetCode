#
# @lc app=leetcode.cn id=920 lang=python3
#
# [920] 播放列表的数量
#

# @lc code=start
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                dp[i][j] = (
                    dp[i - 1][j - 1] * (n - j + 1) + dp[i - 1][j] * max(j - k, 0)
                ) % MOD
        return dp[goal][n]


# @lc code=end
