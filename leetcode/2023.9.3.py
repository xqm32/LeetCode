#
# @lc app=leetcode.cn id=522 lang=python3
#
# [522] 最长特殊序列 II
#

# @lc code=start
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(s: str, t: str) -> bool:
            i = 0
            for c in t:
                if i < len(s) and s[i] == c:
                    i += 1
            return i == len(s)

        strs.sort(key=lambda x: len(x), reverse=True)
        for i, word1 in enumerate(strs):
            if all(not isSubsequence(word1, word2) for j, word2 in enumerate(strs) if i != j):
                return len(word1)
        return -1
# @lc code=end

