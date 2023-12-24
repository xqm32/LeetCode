#
# @lc app=leetcode.cn id=2828 lang=python3
#
# [2828] 判别首字母缩略词
#

# @lc code=start
from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return "".join(i[0] for i in words) == s


# @lc code=end
