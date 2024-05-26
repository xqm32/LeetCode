#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        pairs = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                pairs.append((s[i], goal[i]))
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]


# @lc code=end
