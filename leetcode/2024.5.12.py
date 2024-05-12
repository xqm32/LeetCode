#
# @lc app=leetcode.cn id=767 lang=python3
#
# [767] 重构字符串
#

# @lc code=start
class Solution:
    def reorganizeString(self, s: str) -> str:
        import collections
        import heapq

        counter = collections.Counter(s)
        heap = [(-count, char) for char, count in counter.items()]
        heapq.heapify(heap)
        if (-heap[0][0]) * 2 > len(s) + 1:
            return ""
        ans = []
        while len(heap) >= 2:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)
            ans.extend([char1, char2])
            if count1 + 1:
                heapq.heappush(heap, (count1 + 1, char1))
            if count2 + 1:
                heapq.heappush(heap, (count2 + 1, char2))
        return "".join(ans) + (heap[0][1] if heap else "")


# @lc code=end
