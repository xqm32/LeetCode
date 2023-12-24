#
# @lc app=leetcode.cn id=957 lang=python3
#
# [957] N 天后的牢房
#

# @lc code=start
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = dict()
        while n > 0:
            seen[str(cells)] = n
            n -= 1
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
            if str(cells) in seen:
                n %= seen[str(cells)] - n
        return cells


# @lc code=end
