#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix[0])
        heights = [0] * n
        ans = 0
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0
            stack = [-1]
            for i in range(n):
                while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)
            while stack[-1] != -1:
                h = heights[stack.pop()]
                w = n - stack[-1] - 1
                ans = max(ans, h * w)
        return ans


# @lc code=end
