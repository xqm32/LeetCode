#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        res = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                res += customers[i]
                customers[i] = 0
        max_res = 0
        for i in range(len(customers)):
            if i < minutes:
                res += customers[i]
                max_res = res
            else:
                res = res + customers[i] - customers[i - minutes]
                max_res = max(max_res, res)
        return max_res


# @lc code=end
