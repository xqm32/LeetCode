#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        a, b = divmod(numerator, denominator)
        res.append(str(a))
        if b == 0:
            return "".join(res)
        res.append(".")
        dic = {}
        while b:
            if b in dic:
                res.insert(dic[b], "(")
                res.append(")")
                break
            dic[b] = len(res)
            a, b = divmod(b * 10, denominator)
            res.append(str(a))
        return "".join(res)


# @lc code=end
