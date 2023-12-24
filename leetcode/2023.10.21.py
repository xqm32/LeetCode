#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#

# @lc code=start
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def binary_search(target: int) -> int:
            left, right = 0, len(heaters) - 1
            while left <= right:
                mid = (left + right) // 2
                if heaters[mid] == target:
                    return mid
                elif heaters[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        ans = 0
        for house in houses:
            index = binary_search(house)
            if index == 0:
                ans = max(ans, heaters[index] - house)
            elif index == len(heaters):
                ans = max(ans, house - heaters[index - 1])
            else:
                ans = max(ans, min(heaters[index] - house, house - heaters[index - 1]))
        return ans


# @lc code=end
