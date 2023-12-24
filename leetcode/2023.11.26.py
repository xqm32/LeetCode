#
# @lc app=leetcode.cn id=553 lang=python3
#
# [553] 最优除法
#

# @lc code=start
from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        elif n == 2:
            return str(nums[0]) + "/" + str(nums[1])
        else:
            ans = str(nums[0]) + "/(" + str(nums[1])
            for i in range(2, n):
                ans += "/" + str(nums[i])
            ans += ")"
            return ans


# @lc code=end
