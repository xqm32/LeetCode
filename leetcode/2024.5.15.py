#
# @lc app=leetcode.cn id=336 lang=python3
#
# [336] 回文对
#

# @lc code=start
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            return s == s[::-1]

        words = {word: i for i, word in enumerate(words)}
        res = []
        for word, i in words.items():
            for j in range(len(word) + 1):
                prefix, suffix = word[:j], word[j:]
                if is_palindrome(prefix):
                    back = suffix[::-1]
                    if back != word and back in words:
                        res.append([words[back], i])
                if j != len(word) and is_palindrome(suffix):
                    back = prefix[::-1]
                    if back != word and back in words:
                        res.append([i, words[back]])
        return res


# @lc code=end
