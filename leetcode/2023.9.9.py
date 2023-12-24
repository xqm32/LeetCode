#
# @lc app=leetcode.cn id=318 lang=python3
#
# [318] 最大单词长度乘积
#

# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        lens = [0] * n
        bitNumber = lambda ch: ord(ch) - ord("a")
        for i in range(n):
            bitmask = 0
            for ch in words[i]:
                bitmask |= 1 << bitNumber(ch)
            masks[i] = bitmask
            lens[i] = len(words[i])
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    ans = max(ans, lens[i] * lens[j])
        return ans


# @lc code=end
