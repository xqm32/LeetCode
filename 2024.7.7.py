#
# @lc app=leetcode.cn id=483 lang=python3
#
# [483] 最小好进制
#

# @lc code=start
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        m_max = int(math.log(n) / math.log(2))
        for m in range(m_max, 1, -1):
            k = int(n ** (1 / m))
            if k < 2:
                continue
            if (k ** (m + 1) - 1) // (k - 1) == n:
                return str(k)
        return str(n - 1)

# @lc code=end

