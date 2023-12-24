#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        one_word = len(words[0])
        all_len = len(words) * one_word
        n = len(s)
        words = sorted(words)
        res = []
        for i in range(n - all_len + 1):
            tmp = []
            for j in range(i, i + all_len, one_word):
                tmp.append(s[j : j + one_word])
            tmp = sorted(tmp)
            if tmp == words:
                res.append(i)
        return res


# @lc code=end
