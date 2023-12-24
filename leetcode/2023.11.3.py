#
# @lc app=leetcode.cn id=873 lang=python3
#
# [873] 最长的斐波那契子序列的长度
#

# @lc code=start
from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)
        res = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                a, b = arr[i], arr[j]
                count = 2
                while a + b in s:
                    a, b = b, a + b
                    count += 1
                res = max(res, count)
        return res if res > 2 else 0


# @lc code=end
