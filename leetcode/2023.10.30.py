#
# @lc app=leetcode.cn id=848 lang=python3
#
# [848] 字母移位
#

# @lc code=start
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i + 1]

        res = []
        for i in range(len(s)):
            res.append(chr((ord(s[i]) - ord("a") + shifts[i]) % 26 + ord("a")))
        return "".join(res)


# @lc code=end
