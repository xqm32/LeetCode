#
# @lc app=leetcode.cn id=2864 lang=python3
#
# [2864] 最大二进制奇数
#


# @lc code=start
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return (s.count("1") - 1) * "1" + s.count("0") * "0" + "1"


# @lc code=end
