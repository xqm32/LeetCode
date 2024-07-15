#
# @lc app=leetcode.cn id=878 lang=python3
#
# [878] 第 N 个神奇数字
#

# @lc code=start
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod = 10**9 + 7
        lcm = a * b // math.gcd(a, b)
        left, right = 2, 10**18
        while left < right:
            mid = (left + right) // 2
            if mid // a + mid // b - mid // lcm < n:
                left = mid + 1
            else:
                right = mid
        return left % mod


# @lc code=end
