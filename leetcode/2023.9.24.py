#
# @lc app=leetcode.cn id=650 lang=python3
#
# [650] 只有两个键的键盘
#


# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        for i in range(2, n):
            if n % i == 0:
                return self.minSteps(n // i) + i
        return n


# @lc code=end
