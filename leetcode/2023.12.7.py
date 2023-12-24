#
# @lc app=leetcode.cn id=837 lang=python3
#
# [837] 新 21 点
#


# @lc code=start
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0
        dp = [1.0] + [0.0] * n
        Wsum = 1.0
        for i in range(1, n + 1):
            dp[i] = Wsum / maxPts
            if i < k:
                Wsum += dp[i]
            if i >= maxPts:
                Wsum -= dp[i - maxPts]
        return sum(dp[k:])


# @lc code=end
