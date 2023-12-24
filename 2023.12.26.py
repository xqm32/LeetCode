#
# @lc app=leetcode.cn id=849 lang=python3
#
# [849] 到最近的人的最大距离
#

# @lc code=start
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left = [0] * n
        right = [0] * n
        for i in range(n):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1e9
        for i in range(n - 1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < n - 1:
                right[i] = right[i + 1] + 1
            else:
                right[i] = 1e9
        res = 0
        for i in range(n):
            res = max(res, min(left[i], right[i]))
        return res


# @lc code=end
