#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第 N 位数字
#


# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit

        num = start + (n - 1) // digit
        return int(str(num)[(n - 1) % digit])


# @lc code=end
