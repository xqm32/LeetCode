#
# @lc app=leetcode.cn id=646 lang=python3
#
# [646] 最长数对链
#

# @lc code=start
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        cur = float("-inf")
        ans = 0
        for pair in pairs:
            if cur < pair[0]:
                ans += 1
                cur = pair[1]
        return ans


# @lc code=end
