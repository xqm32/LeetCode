#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[2]
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == target:
                    return tmp
                elif tmp < target:
                    l += 1
                else:
                    r -= 1
                if abs(tmp - target) < abs(res - target):
                    res = tmp
        return res


# @lc code=end
