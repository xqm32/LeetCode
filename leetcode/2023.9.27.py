#
# @lc app=leetcode.cn id=462 lang=python3
#
# [462] 最小操作次数使数组元素相等 II
#

# @lc code=start
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums) // 2]
        res = 0
        for num in nums:
            res += abs(num - mid)
        return res


# @lc code=end
