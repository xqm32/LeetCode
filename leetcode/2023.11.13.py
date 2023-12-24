#
# @lc app=leetcode.cn id=526 lang=python3
#
# [526] 优美的排列
#


# @lc code=start
class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(i: int) -> int:
            if i == n + 1:
                return 1
            res = 0
            for j in range(1, n + 1):
                if not visited[j] and (j % i == 0 or i % j == 0):
                    visited[j] = True
                    res += backtrack(i + 1)
                    visited[j] = False
            return res

        visited = [False] * (n + 1)
        return backtrack(1)


# @lc code=end
