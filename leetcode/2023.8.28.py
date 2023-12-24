#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        L, R = 1, 1
        for i in range(len(nums)):
            ans[i] *= L
            L *= nums[i]
            ans[len(nums) - 1 - i] *= R
            R *= nums[len(nums) - 1 - i]
        return ans


# @lc code=end
