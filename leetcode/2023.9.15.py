#
# @lc app=leetcode.cn id=473 lang=python3
#
# [473] 火柴拼正方形
#

# @lc code=start
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False

        perimeter = sum(matchsticks)
        side = perimeter // 4
        if side * 4 != perimeter:
            return False

        matchsticks.sort(reverse=True)
        sums = [0 for _ in range(4)]

        def dfs(index):
            if index == len(matchsticks):
                return sums[0] == sums[1] == sums[2] == side

            for i in range(4):
                if sums[i] + matchsticks[index] <= side:
                    sums[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sums[i] -= matchsticks[index]
            return False

        return dfs(0)


# @lc code=end
