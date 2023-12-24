#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#

# @lc code=start
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        if len(chars) == 1:
            return 1

        count = 1
        prev = chars[0]
        index = 0
        for i in range(1, len(chars)):
            if chars[i] == prev:
                count += 1
            else:
                chars[index] = prev
                index += 1
                if count > 1:
                    for c in str(count):
                        chars[index] = c
                        index += 1
                prev = chars[i]
                count = 1

        chars[index] = prev
        index += 1
        if count > 1:
            for c in str(count):
                chars[index] = c
                index += 1

        return index


# @lc code=end
