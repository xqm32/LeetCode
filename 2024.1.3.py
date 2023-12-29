#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#

# @lc code=start
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)

        def dfs(node, c):
            if color[node] != 0:
                return color[node] == c
            color[node] = c
            for neighbor in graph[node]:
                if not dfs(neighbor, 3 - c):
                    return False
            return True

        for i in range(len(graph)):
            if color[i] == 0 and not dfs(i, 1):
                return False
        return True


# @lc code=end
