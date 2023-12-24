#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        s //= 2
        dp = [False] * (s + 1)
        dp[0] = True
        for n in nums:
            for i in range(s, n - 1, -1):
                dp[i] = dp[i] or dp[i - n]
        return dp[s]


# @lc code=end
