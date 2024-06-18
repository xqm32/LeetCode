#
# @lc app=leetcode.cn id=502 lang=python3
#
# [502] IPO
#

# @lc code=start
class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        import heapq

        n = len(profits)
        arr = [(capital[i], profits[i]) for i in range(n)]
        arr.sort(key=lambda x: x[0])

        pq = []
        i = 0
        for _ in range(k):
            while i < n and arr[i][0] <= w:
                heapq.heappush(pq, -arr[i][1])
                i += 1
            if pq:
                w -= heapq.heappop(pq)
            else:
                break
        return w


# @lc code=end
