#
# @lc app=leetcode.cn id=906 lang=python3
#
# [906] 超级回文数
#

# @lc code=start
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left, right = int(left), int(right)
        MAGIC = 100000
        ans = 0

        for k in range(MAGIC):
            s = str(k)
            t = s + s[-2::-1]
            v = int(t) ** 2
            if v > right:
                break
            if v >= left and self.is_palindrome(v):
                ans += 1

        for k in range(MAGIC):
            s = str(k)
            t = s + s[::-1]
            v = int(t) ** 2
            if v > right:
                break
            if v >= left and self.is_palindrome(v):
                ans += 1

        return ans

    def is_palindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


# @lc code=end
