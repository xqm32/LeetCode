#
# @lc app=leetcode.cn id=891 lang=python3
#
# [891] 子序列宽度之和
#

# @lc code=start
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        ans = 0
        pow2 = [1]
        for i in range(1, n):
            pow2.append(pow2[-1] * 2 % MOD)
        for i in range(n):
            ans = (ans + (pow2[i] - pow2[n - 1 - i]) * nums[i]) % MOD
        return ans


# @lc code=end
