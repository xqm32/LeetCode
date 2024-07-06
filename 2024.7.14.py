#
# @lc app=leetcode.cn id=1872 lang=python3
#
# [1872] 石子游戏 VIII
#

# @lc code=start
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        for i in range(1, n):
            stones[i] += stones[i - 1]
        dp = [0] * n
        dp[-1] = stones[-1]
        for i in range(n - 2, 0, -1):
            dp[i] = max(dp[i + 1], stones[i] - dp[i + 1])
        return dp[1]


# @lc code=end
