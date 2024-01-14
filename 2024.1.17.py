#
# @lc app=leetcode.cn id=898 lang=python3
#
# [898] 子数组按位或操作
#


# @lc code=start
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()
        for i in arr:
            cur = {i | j for j in cur} | {i}
            res |= cur
        return len(res)


# @lc code=end
