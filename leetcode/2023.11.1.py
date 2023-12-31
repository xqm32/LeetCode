#
# @lc app=leetcode.cn id=861 lang=python3
#
# [861] 翻转矩阵后的得分
#

# @lc code=start
from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1

        for j in range(1, n):
            cnt = sum(grid[i][j] for i in range(m))
            if cnt < m - cnt:
                for i in range(m):
                    grid[i][j] ^= 1

        res = 0
        for i in range(m):
            res += int("".join(map(str, grid[i])), 2)
        return res


# @lc code=end
