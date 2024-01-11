#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#


# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        left = right = 0
        res = 0
        max_count = 0
        counter = {}
        while right < len(s):
            counter[s[right]] = counter.get(s[right], 0) + 1
            max_count = max(max_count, counter[s[right]])
            right += 1
            if right - left > max_count + k:
                counter[s[left]] -= 1
                left += 1
            res = max(res, right - left)
        return res


# @lc code=end
