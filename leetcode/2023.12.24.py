#
# @lc app=leetcode.cn id=688 lang=python3
#
# [688] 骑士在棋盘上的概率
#


# @lc code=start
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1
        for _ in range(k):
            dp2 = [[0] * n for _ in range(n)]
            for x in range(n):
                for y in range(n):
                    for dx, dy in (
                        (2, 1),
                        (2, -1),
                        (-2, 1),
                        (-2, -1),
                        (1, 2),
                        (1, -2),
                        (-1, 2),
                        (-1, -2),
                    ):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            dp2[nx][ny] += dp[x][y] / 8.0
            dp = dp2
        return sum(map(sum, dp))


# @lc code=end
