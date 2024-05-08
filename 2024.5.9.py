#
# @lc app=leetcode.cn id=464 lang=python3
#
# [464] 我能赢吗
#

# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger >= desiredTotal:
            return True
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False

        def dfs(used, desiredTotal):
            if desiredTotal <= 0:
                return False
            if used in memo:
                return memo[used]
            for i in range(1, maxChoosableInteger + 1):
                cur = 1 << i
                if cur & used:
                    continue
                if not dfs(cur | used, desiredTotal - i):
                    memo[used] = True
                    return True
            memo[used] = False
            return False

        memo = {}
        return dfs(0, desiredTotal)


# @lc code=end
