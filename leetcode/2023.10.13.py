#
# @lc app=leetcode.cn id=1017 lang=python3
#
# [1017] 负二进制转换
#


# @lc code=start
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        res = []
        while n != 0:
            res.append(n & 1)
            n = -(n >> 1)
        return "".join(map(str, res[::-1]))


# @lc code=end
