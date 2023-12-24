#
# @lc app=leetcode.cn id=2859 lang=python3
#
# [2859] 计算 K 置位下标对应元素的和
#

# @lc code=start
from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            if bin(i).count("1") == k:
                ans += nums[i]
        return ans


# @lc code=end
