#
# @lc app=leetcode.cn id=984 lang=python3
#
# [984] 不含 AAA 或 BBB 的字符串
#


# @lc code=start
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        while a > 0 or b > 0:
            if a > b:
                if a > 1:
                    res.append("aa")
                    a -= 2
                else:
                    res.append("a")
                    a -= 1
                if b > 0:
                    res.append("b")
                    b -= 1
            elif a < b:
                if b > 1:
                    res.append("bb")
                    b -= 2
                else:
                    res.append("b")
                    b -= 1
                if a > 0:
                    res.append("a")
                    a -= 1
            else:
                res.append("ab")
                a -= 1
                b -= 1
        return "".join(res)


# @lc code=end
