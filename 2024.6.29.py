#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#

# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict

        tickets.sort(reverse=True)
        graph = defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)
        res = []

        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())
            res.append(start)

        dfs("JFK")
        return res[::-1]


# @lc code=end
