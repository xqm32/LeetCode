#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(piles, speed, h):
            time = 0
            for n in piles:
                time += (n // speed) + (1 if n % speed > 0 else 0)
            return time <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if canFinish(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        return left


# @lc code=end
