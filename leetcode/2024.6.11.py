#
# @lc app=leetcode.cn id=576 lang=python3
#
# [576] 出界的路径数
#

# @lc code=start
class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        dp = [[[0] * (maxMove + 1) for _ in range(n)] for _ in range(m)]
        MOD = 10**9 + 7
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for k in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if ni < 0 or ni >= m or nj < 0 or nj >= n:
                            dp[i][j][k] += 1
                        else:
                            dp[i][j][k] = (dp[i][j][k] + dp[ni][nj][k - 1]) % MOD
        return dp[startRow][startColumn][maxMove]


# @lc code=end
