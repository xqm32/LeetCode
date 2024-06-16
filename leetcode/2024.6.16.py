#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        digit = 1
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0:
                count += high * digit
            elif cur == 1:
                count += high * digit + low + 1
            else:
                count += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return count


# @lc code=end
