#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] 水壶问题
#


# @lc code=start
class Solution:
    def canMeasureWater(
        self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int
    ) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False

        if jug1Capacity == 0 or jug2Capacity == 0:
            return targetCapacity == 0 or jug1Capacity + jug2Capacity == targetCapacity

        return targetCapacity % self.gcd(jug1Capacity, jug2Capacity) == 0

    def gcd(self, a, b):
        if a < b:
            a, b = b, a

        while b != 0:
            a, b = b, a % b

        return a


# @lc code=end
