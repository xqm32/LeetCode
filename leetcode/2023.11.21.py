#
# @lc app=leetcode.cn id=678 lang=python3
#
# [678] 有效的括号字符串
#


# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack, star_stack = [], []
        for i in range(len(s)):
            if s[i] == "(":
                left_stack.append(i)
            elif s[i] == "*":
                star_stack.append(i)
            else:
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        while left_stack and star_stack:
            if left_stack.pop() > star_stack.pop():
                return False
        return not left_stack


# @lc code=end
