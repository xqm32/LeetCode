#
# @lc app=leetcode.cn id=910 lang=python3
#
# [910] 最小差值 II
#

# @lc code=start
from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[-1] - nums[0]
        for i in range(n - 1):
            a, b = nums[i], nums[i + 1]
            res = min(res, max(nums[-1] - k, a + k) - min(nums[0] + k, b - k))
        return res


# @lc code=end
