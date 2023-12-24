#
# @lc app=leetcode.cn id=393 lang=python3
#
# [393] UTF-8 编码验证
#

# @lc code=start
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_len(n: int) -> int:
            if n & 0b10000000 == 0:
                return 1
            elif n & 0b11100000 == 0b11000000:
                return 2
            elif n & 0b11110000 == 0b11100000:
                return 3
            elif n & 0b11111000 == 0b11110000:
                return 4
            else:
                return 0

        i: int = 0
        while i < len(data):
            length: int = get_len(data[i])
            if length == 0:
                return False
            for j in range(i + 1, i + length):
                if j >= len(data):
                    return False
                if data[j] & 0b11000000 != 0b10000000:
                    return False
            i += length
        return True
# @lc code=end

