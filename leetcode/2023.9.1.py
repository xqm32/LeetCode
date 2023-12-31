#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
#

# @lc code=start
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        m, n = len(mat), len(mat[0])
        res = []
        for i in range(m + n - 1):
            if i % 2 != 0:
                for j in range(i + 1):
                    if j < m and i - j < n:
                        res.append(mat[j][i - j])
            else:
                for j in range(i, -1, -1):
                    if j < m and i - j < n:
                        res.append(mat[j][i - j])
        return res


# @lc code=end
