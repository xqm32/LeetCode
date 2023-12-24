#
# @lc app=leetcode.cn id=840 lang=python3
#
# [840] 矩阵中的幻方
#

# @lc code=start
from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def magic(
            a: int, b: int, c: int, d: int, e: int, f: int, g: int, h: int, i: int
        ) -> bool:
            return sorted([a, b, c, d, e, f, g, h, i]) == list(range(1, 10)) and (
                a + b + c
                == d + e + f
                == g + h + i
                == a + d + g
                == b + e + h
                == c + f + i
                == a + e + i
                == c + e + g
                == 15
            )

        ans = 0
        for r in range(R - 2):
            for c in range(C - 2):
                if grid[r + 1][c + 1] != 5:
                    continue
                if magic(
                    grid[r][c],
                    grid[r][c + 1],
                    grid[r][c + 2],
                    grid[r + 1][c],
                    grid[r + 1][c + 1],
                    grid[r + 1][c + 2],
                    grid[r + 2][c],
                    grid[r + 2][c + 1],
                    grid[r + 2][c + 2],
                ):
                    ans += 1
        return ans


# @lc code=end
