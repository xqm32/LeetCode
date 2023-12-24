#
# @lc app=leetcode.cn id=792 lang=python3
#
# [792] 匹配子序列的单词数
#

# @lc code=start
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subsequence(word):
            i = 0
            for c in word:
                i = s.find(c, i) + 1
                if not i:
                    return False
            return True

        return sum(is_subsequence(word) for word in words)


# @lc code=end
