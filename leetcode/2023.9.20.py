#
# @lc app=leetcode.cn id=795 lang=python3
#
# [795] 区间子数组个数
#

# @lc code=start
from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound):
            ans = cur = 0
            for num in nums:
                cur = cur + 1 if num <= bound else 0
                ans += cur
            return ans

        return count(right) - count(left - 1)


# @lc code=end
