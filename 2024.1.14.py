#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        visited = set()
        res = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                res += 1
        return res


# @lc code=end
