#
# @lc app=leetcode.cn id=1334 lang=python3
#
# [1334] 阈值距离内邻居最少的城市
#

# @lc code=start
class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = dist[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        min_count = n
        res = -1
        for i in range(n):
            count = sum(dist[i][j] <= distanceThreshold for j in range(n)) - 1
            if count <= min_count:
                min_count = count
                res = i
        return res


# @lc code=end
