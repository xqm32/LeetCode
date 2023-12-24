#
# @lc app=leetcode.cn id=789 lang=python3
#
# [789] 逃脱阻碍者
#

# @lc code=start
from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        my_distance = distance([0, 0], target)
        for ghost in ghosts:
            ghost_distance = distance(ghost, target)
            if ghost_distance <= my_distance:
                return False
        return True


# @lc code=end
