#
# @lc app=leetcode.cn id=532 lang=python3
#
# [532] 数组中的 k-diff 数对
#

# @lc code=start
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        nums.sort()
        i, j = 0, 1
        res = 0
        while j < len(nums):
            if nums[j] - nums[i] == k:
                res += 1
                i += 1
                j += 1
                while j < len(nums) and nums[j] == nums[j - 1]:
                    j += 1
            elif nums[j] - nums[i] < k:
                j += 1
            else:
                i += 1
                if i == j:
                    j += 1
        return res


# @lc code=end
