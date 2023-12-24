#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#

# @lc code=start
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = {}
        for i in range(len(equations)):
            a, b = equations[i]
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]

        def dfs(a, b, visited):
            if a not in graph or b not in graph:
                return -1
            if b in graph[a]:
                return graph[a][b]
            for c in graph[a]:
                if c not in visited:
                    visited.add(c)
                    res = dfs(c, b, visited)
                    if res != -1:
                        return graph[a][c] * res
            return -1

        res = []
        for a, b in queries:
            res.append(dfs(a, b, set()))
        return res


# @lc code=end
