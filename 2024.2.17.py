#
# @lc app=leetcode.cn id=313 lang=python3
#
# [313] 超级丑数
#

# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1] * n
        pointers = [0] * len(primes)
        for i in range(1, n):
            dp[i] = min([dp[pointers[j]] * primes[j] for j in range(len(primes))])
            for j in range(len(primes)):
                if dp[i] == dp[pointers[j]] * primes[j]:
                    pointers[j] += 1
        return dp[-1]


# @lc code=end
