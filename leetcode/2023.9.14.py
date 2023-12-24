#
# @lc app=leetcode.cn id=856 lang=python3
#
# [856] 括号的分数
#


# @lc code=start
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    temp = 0
                    while stack[-1] != "(":
                        temp += stack.pop()
                    stack.pop()
                    stack.append(temp * 2)
        return sum(stack)


# @lc code=end
