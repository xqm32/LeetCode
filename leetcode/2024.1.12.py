#
# @lc app=leetcode.cn id=1034 lang=python3
#
# [1034] 边界着色
#

# @lc code=start
from typing import List


class Solution:
    def colorBorder(
        self, grid: List[List[int]], row: int, col: int, color: int
    ) -> List[List[int]]:
        def dfs(i, j):
            if not (
                0 <= i < m
                and 0 <= j < n
                and grid[i][j] == old_color
                and (i, j) not in visited
            ):
                return
            visited.add((i, j))
            if (
                i == 0
                or i == m - 1
                or j == 0
                or j == n - 1
                or any(
                    (i + di, j + dj) not in visited
                    and grid[i + di][j + dj] != old_color
                    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0))
                )
            ):
                grid[i][j] = color
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                dfs(i + di, j + dj)

        m, n = len(grid), len(grid[0])
        visited = set()
        old_color = grid[row][col]
        dfs(row, col)
        return grid


# @lc code=end
