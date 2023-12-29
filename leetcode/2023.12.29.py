#
# @lc app=leetcode.cn id=1276 lang=python3
#
# [1276] 不浪费原料的汉堡制作方案
#

# @lc code=start
from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 == 1:
            return []
        if tomatoSlices < 2 * cheeseSlices:
            return []
        if tomatoSlices > 4 * cheeseSlices:
            return []
        return [
            tomatoSlices // 2 - cheeseSlices,
            2 * cheeseSlices - tomatoSlices // 2,
        ]


# @lc code=end
