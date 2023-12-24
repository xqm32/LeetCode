#
# @lc app=leetcode.cn id=2670 lang=python3
#
# [2670] 找出不同元素数目差数组
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(len(set(nums[: i + 1])) - len(set(nums[i + 1 :])))
        return ans


# @lc code=end
