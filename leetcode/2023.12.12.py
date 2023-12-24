#
# @lc app=leetcode.cn id=893 lang=python3
#
# [893] 特殊等价字符串组
#

# @lc code=start
from typing import List


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def get_key(word):
            odd = []
            even = []
            for i, c in enumerate(word):
                if i % 2 == 0:
                    even.append(c)
                else:
                    odd.append(c)
            odd.sort()
            even.sort()
            return "".join(odd) + "".join(even)

        return len(set(map(get_key, words)))


# @lc code=end
