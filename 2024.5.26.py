#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#

# @lc code=start
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        words_set, res = set(words), ""
        for word in words:
            if len(word) > len(res) or len(word) == len(res) and word < res:
                if all(word[:k] in words_set for k in range(1, len(word))):
                    res = word
        return res


# @lc code=end
