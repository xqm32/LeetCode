#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#


# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        x = 0xFFFFFFFF
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), ((a & b) << 1) & x
        return a if a <= 0x7FFFFFFF else ~(a ^ x)


# @lc code=end
