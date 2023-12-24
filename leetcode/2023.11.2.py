#
# @lc app=leetcode.cn id=869 lang=python3
#
# [869] 重新排序得到 2 的幂
#


# @lc code=start
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return sorted(str(n)) in [sorted(str(1 << i)) for i in range(31)]


# @lc code=end
