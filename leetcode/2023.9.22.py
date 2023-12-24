#
# @lc app=leetcode.cn id=799 lang=python3
#
# [799] 香槟塔
#


# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (i + 1) for i in range(101)]
        dp[0][0] = poured
        for i in range(1, 101):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = max((dp[i - 1][j] - 1) / 2, 0)
                elif j == i:
                    dp[i][j] = max((dp[i - 1][j - 1] - 1) / 2, 0)
                else:
                    dp[i][j] = max((dp[i - 1][j] - 1) / 2, 0) + max(
                        (dp[i - 1][j - 1] - 1) / 2, 0
                    )
        return min(dp[query_row][query_glass], 1)


# @lc code=end
