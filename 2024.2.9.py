#
# @lc app=leetcode.cn id=1260 lang=python3
#
# [1260] 二维网格迁移
#

# @lc code=start
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
        if k == 0:
            return grid
        grid = sum(grid, [])
        grid = grid[-k:] + grid[:-k]
        return [grid[i * n : (i + 1) * n] for i in range(m)]


# @lc code=end
