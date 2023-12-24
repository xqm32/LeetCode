#
# @lc app=leetcode.cn id=885 lang=python3
#
# [885] 螺旋矩阵 III
#

# @lc code=start
from typing import List


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        ans = [[rStart, cStart]]
        r, c = rStart, cStart
        step = 1
        while len(ans) < rows * cols:
            for _ in range(step):
                c += 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
            for _ in range(step):
                r += 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
            step += 1
            for _ in range(step):
                c -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
            for _ in range(step):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
            step += 1
        return ans


# @lc code=end
