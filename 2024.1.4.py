#
# @lc app=leetcode.cn id=866 lang=python3
#
# [866] 回文素数
#


# @lc code=start
class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            if x < 2 or x % 2 == 0:
                return x == 2
            for i in range(3, int(x**0.5) + 1, 2):
                if x % i == 0:
                    return False
            return True

        if 8 <= n <= 11:
            return 11
        for i in range(10 ** (len(str(n)) // 2), 10**5):
            x = int(str(i) + str(i)[-2::-1])
            if x >= n and is_prime(x):
                return x


# @lc code=end
