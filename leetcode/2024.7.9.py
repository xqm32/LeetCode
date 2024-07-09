#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        memo = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if memo[i][j] != 0:
                return memo[i][j]
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    memo[i][j] = max(memo[i][j], dfs(x, y))
            memo[i][j] += 1
            return memo[i][j]

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res


# @lc code=end
