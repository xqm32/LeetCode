#
# @lc app=leetcode.cn id=880 lang=python3
#
# [880] 索引处的解码字符串
#


# @lc code=start
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for i in s:
            if i.isdigit():
                size *= int(i)
            else:
                size += 1
        for i in reversed(s):
            k %= size
            if k == 0 and i.isalpha():
                return i
            if i.isdigit():
                size /= int(i)
            else:
                size -= 1
        # ?
        return "b"


# @lc code=end
