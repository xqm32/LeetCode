#
# @lc app=leetcode.cn id=2839 lang=python3
#
# [2839] 判断通过操作能否让字符串相等 I
#


# @lc code=start
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        a, b, c, d = list(s1)
        return (
            f"{a}{b}{c}{d}" == s2
            or f"{c}{b}{a}{d}" == s2
            or f"{a}{d}{c}{b}" == s2
            or f"{c}{d}{a}{b}" == s2
        )


# @lc code=end
