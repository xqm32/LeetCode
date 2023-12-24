#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#

# @lc code=start
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if not 0 <= i < n or not 0 <= j < m or grid[i][j] == 0:
                return
            grid[i][j] = 0
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        for j in range(m):
            dfs(0, j)
            dfs(n - 1, j)
        return sum(sum(row) for row in grid)


# @lc code=end
