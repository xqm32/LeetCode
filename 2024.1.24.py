#
# @lc app=leetcode.cn id=858 lang=python3
#
# [858] 镜面反射
#


# @lc code=start
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0:
            p, q = p // 2, q // 2
        return 1 - p % 2 + q % 2


# @lc code=end
