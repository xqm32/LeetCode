#
# @lc app=leetcode.cn id=477 lang=python3
#
# [477] 汉明距离总和
#

# @lc code=start
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(30):
            c = sum(((num >> i) & 1) for num in nums)
            ans += c * (n - c)
        return ans


# @lc code=end
