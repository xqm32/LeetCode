#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#


# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            s = self.countAndSay(n - 1)
            i = 0
            j = 0
            res = ""
            while j < len(s):
                if s[i] != s[j]:
                    res += str(j - i) + s[i]
                    i = j
                j += 1
            res += str(j - i) + s[i]
            return res


# @lc code=end
