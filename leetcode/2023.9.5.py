#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            sumOfGas, sumOfCost = 0, 0
            cnt = 0
            while cnt < n:
                j = (i + cnt) % n
                sumOfGas += gas[j]
                sumOfCost += cost[j]
                if sumOfCost > sumOfGas:
                    break
                cnt += 1
            if cnt == n:
                return i
            else:
                i = i + cnt + 1
        return -1
# @lc code=end

