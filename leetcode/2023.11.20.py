#
# @lc app=leetcode.cn id=554 lang=python3
#
# [554] 砖墙
#

# @lc code=start
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        from collections import defaultdict
        from itertools import accumulate

        d = defaultdict(int)
        for row in wall:
            for i in accumulate(row[:-1]):
                d[i] += 1
        return len(wall) - max(d.values(), default=0)


# @lc code=end
