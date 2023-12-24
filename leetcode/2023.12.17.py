#
# @lc app=leetcode.cn id=1333 lang=python3
#
# [1333] 餐厅过滤器
#

# @lc code=start
from typing import List


class Solution:
    def filterRestaurants(
        self,
        restaurants: List[List[int]],
        veganFriendly: int,
        maxPrice: int,
        maxDistance: int,
    ) -> List[int]:
        restaurants = filter(
            lambda x: x[2] >= veganFriendly
            and x[3] <= maxPrice
            and x[4] <= maxDistance,
            restaurants,
        )
        restaurants = sorted(restaurants, key=lambda x: (x[1], x[0]), reverse=True)
        return [x[0] for x in restaurants]


# @lc code=end
