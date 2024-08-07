#
# @lc app=leetcode.cn id=899 lang=python3
#
# [899] 有序队列
#

# @lc code=start
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        return "".join(sorted(s))


# @lc code=end
