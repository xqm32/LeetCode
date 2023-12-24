#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#

# @lc code=start
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in dislikes:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        color = [0] * n
        for i in range(n):
            if color[i] == 0:
                if not self.dfs(adj, color, i, 1):
                    return False
        return True

    def dfs(self, adj, color, i, c):
        color[i] = c
        for j in adj[i]:
            if color[j] == c:
                return False
            if color[j] == 0 and not self.dfs(adj, color, j, -c):
                return False
        return True


# @lc code=end
