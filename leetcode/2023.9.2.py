#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# @lc code=start
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        n = len(nums)
        def backtrack(start, path):
            if len(path)>1:
                res.append(path[:])
            used = set()
            for i in range(start, n):
                if nums[i] in used:
                    continue
                if not path or nums[i]>=path[-1]:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtrack(i+1, path)
                    path.pop()
        backtrack(0, [])
        return res
# @lc code=end

