#
# @lc app=leetcode.cn id=514 lang=python3
#
# [514] 自由之路
#

# @lc code=start
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        from collections import defaultdict
        from functools import lru_cache

        n, m = len(ring), len(key)
        pos = defaultdict(list)
        for i, c in enumerate(ring):
            pos[c].append(i)

        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if j == m:
                return 0
            res = float("inf")
            for k in pos[key[j]]:
                d = abs(i - k)
                res = min(res, min(d, n - d) + 1 + dfs(k, j + 1))
            return res

        return dfs(0, 0)


# @lc code=end
