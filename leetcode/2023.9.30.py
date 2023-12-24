#
# @lc app=leetcode.cn id=831 lang=python3
#
# [831] 隐藏个人信息
#


# @lc code=start
class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            return self.mask_email(s)
        else:
            return self.mask_phone(s)

    def mask_email(self, s):
        s = s.lower()
        name, domain = s.split("@")
        return name[0] + "*****" + name[-1] + "@" + domain

    def mask_phone(self, s):
        digits = [c for c in s if c.isdigit()]
        local = "***-***-" + "".join(digits[-4:])
        if len(digits) == 10:
            return local
        else:
            return "+" + "*" * (len(digits) - 10) + "-" + local


# @lc code=end
