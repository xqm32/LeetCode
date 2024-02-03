#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        right = intervals[0][1]
        ans = 0
        for i in range(1, n):
            if intervals[i][0] < right:
                ans += 1
            else:
                right = intervals[i][1]
        return ans


# @lc code=end
