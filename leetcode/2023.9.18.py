#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#


# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq

        heap = [1]
        seen = set()
        seen.add(1)
        factors = [2, 3, 5]
        for i in range(n):
            ugly = heapq.heappop(heap)
            for factor in factors:
                new_ugly = ugly * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return ugly


# @lc code=end
