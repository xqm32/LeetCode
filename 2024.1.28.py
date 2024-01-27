#
# @lc app=leetcode.cn id=1208 lang=python3
#
# [1208] 尽可能使字符串相等
#

# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        left = right = 0
        cost = 0
        while right < n:
            cost += abs(ord(s[right]) - ord(t[right]))
            if cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            right += 1
        return right - left
# @lc code=end

