#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#

# @lc code=start
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(i, j, visited):
            visited.add((i, j))
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (
                    x < 0
                    or x >= m
                    or y < 0
                    or y >= n
                    or (x, y) in visited
                    or heights[x][y] < heights[i][j]
                ):
                    continue
                dfs(x, y, visited)

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m - 1, j, atlantic)

        return list(pacific & atlantic)


# @lc code=end
