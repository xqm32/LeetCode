#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#


# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c**0.5)
        while left <= right:
            tmp = left**2 + right**2
            if tmp == c:
                return True
            elif tmp < c:
                left += 1
            else:
                right -= 1
        return False


# @lc code=end
