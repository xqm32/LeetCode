#
# @lc app=leetcode.cn id=1362 lang=python3
#
# [1362] 最接近的因数
#

# @lc code=start
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for i in range(int((num + 2) ** 0.5), 0, -1):
            if (num + 1) % i == 0:
                return [i, (num + 1) // i]
            if (num + 2) % i == 0:
                return [i, (num + 2) // i]


# @lc code=end
