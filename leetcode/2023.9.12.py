#
# @lc app=leetcode.cn id=973 lang=python3
#
# [973] 最接近原点的 K 个点
#

# @lc code=start
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq

        heap = []
        for point in points:
            heapq.heappush(heap, (point[0] ** 2 + point[1] ** 2, point))
        return [heapq.heappop(heap)[1] for _ in range(k)]


# @lc code=end
