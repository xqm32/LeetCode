#
# @lc app=leetcode.cn id=565 lang=python3
#
# [565] 数组嵌套
#

# @lc code=start
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] != -1:
                start = nums[i]
                count = 0
                while nums[start] != -1:
                    temp = start
                    start = nums[start]
                    count += 1
                    nums[temp] = -1
                res = max(res, count)
        return res


# @lc code=end
