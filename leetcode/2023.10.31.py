#
# @lc app=leetcode.cn id=853 lang=python3
#
# [853] 车队
#

# @lc code=start
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [(target - p) / s for p, s in cars]
        res = 0
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]:
                res += 1
            else:
                times[-1] = lead
        return res + bool(times)


# @lc code=end
