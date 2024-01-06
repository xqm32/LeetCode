#
# @lc app=leetcode.cn id=915 lang=python3
#
# [915] 分割数组
#

# @lc code=start
from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        max_left = [0] * n
        min_right = [0] * n
        max_left[0] = nums[0]
        min_right[-1] = nums[-1]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], nums[i])
        for i in range(n - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], nums[i])
        for i in range(1, n):
            if max_left[i - 1] <= min_right[i]:
                return i


# @lc code=end
