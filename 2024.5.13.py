#
# @lc app=leetcode.cn id=218 lang=python3
#
# [218] 天际线问题
#

# @lc code=start
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        import heapq

        points = []
        for l, r, h in buildings:
            points.append((l, -h, r))
            points.append((r, h, 0))
        points.sort()
        res = [[0, 0]]
        heap = [(0, float("inf"))]
        for x, h, r in points:
            while x >= heap[0][1]:
                heapq.heappop(heap)
            if h < 0:
                heapq.heappush(heap, (h, r))
            if res[-1][1] != -heap[0][0]:
                res.append([x, -heap[0][0]])
        return res[1:]


# @lc code=end
