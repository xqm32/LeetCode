#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right = 0, 0
        window, need = {}, {}
        for c in p:
            need[c] = need.get(c, 0) + 1
        res = []
        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1
            while right - left >= len(p):
                if window == need:
                    res.append(left)
                d = s[left]
                left += 1
                window[d] -= 1
                if window[d] == 0:
                    del window[d]
        return res


# @lc code=end
