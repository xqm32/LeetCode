#
# @lc app=leetcode.cn id=525 lang=python3
#
# [525] 连续数组
#

# @lc code=start
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre_sum = 0
        hash_map = {0: -1}
        max_len = 0
        for i, num in enumerate(nums):
            if num == 0:
                pre_sum -= 1
            else:
                pre_sum += 1
            if pre_sum in hash_map:
                max_len = max(max_len, i - hash_map[pre_sum])
            else:
                hash_map[pre_sum] = i
        return max_len


# @lc code=end
