#
# @lc app=leetcode.cn id=820 lang=python3
#
# [820] 单词的压缩编码
#

# @lc code=start
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted(words, key=lambda x: len(x), reverse=True)
        res = ""
        for word in words:
            if word + "#" not in res:
                res += word + "#"
        return len(res)


# @lc code=end
