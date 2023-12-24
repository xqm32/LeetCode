#
# @lc app=leetcode.cn id=921 lang=python3
#
# [921] 使括号有效的最少添加
#


# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack)


# @lc code=end
