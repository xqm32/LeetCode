#
# @lc app=leetcode.cn id=330 lang=python3
#
# [330] 按要求补齐数组
#

# @lc code=start
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        x = 1
        length = len(nums)
        index = 0
        while x <= n:
            if index < length and nums[index] <= x:
                x += nums[index]
                index += 1
            else:
                x *= 2
                patches += 1
        return patches


# @lc code=end
