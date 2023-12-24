#
# @lc app=leetcode.cn id=397 lang=python3
#
# [397] 整数替换
#


# @lc code=start
class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0
        while n != 1:
            if n & 1 == 0:
                n >>= 1
            else:
                if (n + 1) & 2 == 0 and n != 3:
                    n += 1
                else:
                    n -= 1
            res += 1
        return res


# @lc code=end
