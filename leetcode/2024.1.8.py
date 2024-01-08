#
# @lc app=leetcode.cn id=822 lang=python3
#
# [822] 翻转卡片游戏
#

# @lc code=start
from typing import List


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = {x for i, x in enumerate(fronts) if x == backs[i]}
        return min([x for x in set(fronts + backs) if x not in same], default=0)


# @lc code=end
